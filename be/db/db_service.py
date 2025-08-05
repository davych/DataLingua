"""
数据库服务：负责执行 SQL 查询，返回结果。
设计原则：接口简单，便于后续扩展多种数据库。
"""
import sqlite3
import os
from typing import Any, List

class DBService:
    def __init__(self, db_path: str):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_path)
        
        # 验证数据库文件是否存在
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found: {self.db_path}")

    def query(self, sql: str) -> List[Any]:
        """
        执行SQL查询并返回结果
        
        Args:
            sql: 要执行的SQL语句
            
        Returns:
            查询结果的字典列表
            
        Raises:
            sqlite3.Error: 当SQL执行出错时
            Exception: 其他执行错误
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            return [{col: val for col, val in zip(columns, row)} for row in data]
        except sqlite3.Error as e:
            # 抛出SQLite特定错误，包括表不存在等
            raise sqlite3.Error(f"Database error executing SQL '{sql}': {str(e)}") from e
        except Exception as e:
            # 抛出其他类型的错误
            raise Exception(f"Unexpected error executing SQL '{sql}': {str(e)}") from e
        finally:
            if conn:
                conn.close()
