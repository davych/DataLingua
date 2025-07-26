

from langchain_community.llms import Ollama
import asyncio
import re
import textwrap

ollama = Ollama(model="deepseek-r1:32b", base_url="http://localhost:11434")

DB_SCHEMA_DDL = textwrap.dedent('''
数据库表结构如下（SQLite DDL）：
CREATE TABLE user (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);
CREATE TABLE artist (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);
CREATE TABLE album (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  artist_id INTEGER,
  FOREIGN KEY(artist_id) REFERENCES artist(id)
);
CREATE TABLE song (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  album_id INTEGER,
  artist_id INTEGER,
  FOREIGN KEY(album_id) REFERENCES album(id),
  FOREIGN KEY(artist_id) REFERENCES artist(id)
);
CREATE TABLE like (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  song_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES user(id),
  FOREIGN KEY(song_id) REFERENCES song(id)
);
''')

def extract_sql_from_text(text: str) -> str:
    """
    提取 LLM 输出中的 SQL 代码块或首个 SQL 语句，剥离 <think>、标签、解释性内容，只保留 SQL。
    """
    # 1. 去除 <think>...</think> 及所有 HTML/XML 标签
    text = re.sub(r'<[^>]+>', '', text)
    # 2. 去除常见解释性前缀
    text = re.sub(r'(?i)(SQL如下|查询语句|SQL语句|如下SQL|SQL:|Query:|查询:)[：:]*', '', text)
    # 3. 提取 ```sql ... ``` 或 ``` ... ``` 代码块
    code_block = re.search(r'```sql\s*([\s\S]+?)```', text, re.IGNORECASE)
    if not code_block:
        code_block = re.search(r'```\s*([\s\S]+?)```', text, re.IGNORECASE)
    if code_block:
        return code_block.group(1).strip()
    # 4. 按行分割，找到第一个以 SQL 关键字开头的行，收集连续 SQL 行
    lines = text.strip().splitlines()
    sql_keywords = ("SELECT", "WITH", "INSERT", "UPDATE", "DELETE")
    sql_lines = []
    collecting = False
    for line in lines:
        lstripped = line.lstrip()
        if not collecting and any(lstripped.upper().startswith(k) for k in sql_keywords):
            collecting = True
        if collecting:
            # 只收集非空行，遇到纯解释性内容或空行则停止
            if lstripped == '' or lstripped.startswith('--') or lstripped.startswith('#'):
                break
            sql_lines.append(line)
    if sql_lines:
        return '\n'.join(sql_lines).strip()
    # 5. fallback: 返回原始文本
    return text.strip()

def _is_sqlite_compatible(sql: str) -> bool:
    # 检查常见不兼容 SQLite 的写法
    # 例如 SUM(COUNT(...)), 嵌套聚合等
    if re.search(r'SUM\s*\(\s*COUNT', sql, re.IGNORECASE):
        return False
    if re.search(r'GROUP BY.*GROUP BY', sql, re.IGNORECASE):
        return False
    # 检查 GROUP BY 是否聚合结果（如 GROUP BY album_count）
    if re.search(r'GROUP BY\s+(album_count|count|sum|avg|max|min)', sql, re.IGNORECASE):
        return False
    return True

async def nl_to_sql(question: str) -> str:
    base_prompt = (
        f"你是SQL专家。请根据下方数据库表结构（DDL），将自然语言问题转为针对音乐业务数据库的SQLite SQL语句，只返回SQL，不要解释。\n"
        f"{DB_SCHEMA_DDL}"
        "注意：1. 字段名、表名必须与DDL完全一致，2. 所有表的主键都叫 id，没有 artist_id/album_id/song_id 这类前缀字段，3. 外键字段才会用 *_id，4. GROUP BY 必须是原始分组字段，不能是聚合结果（如 album_count），只能是表中的实际字段。"
    )
    prompt = f"{base_prompt} 问题：{question}"
    loop = asyncio.get_event_loop()
    last_sql = ""
    for _ in range(2):
        raw = await loop.run_in_executor(None, ollama.invoke, prompt)
        print(f"Generated SQL: {raw}")
        sql = extract_sql_from_text(raw)
        print(f"Generated SQL: {sql}")
        last_sql = sql
        if _is_sqlite_compatible(sql):
            return sql
        # 如果不兼容，补充提示重试
        prompt += "\n注意：上次SQL不兼容SQLite，GROUP BY 只能用原始字段，不能用聚合结果或别名。请严格用CTE或两步法，不能用嵌套聚合。"
    return last_sql  # 始终有返回值
