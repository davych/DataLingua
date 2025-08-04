"""
数据库服务：负责执行 SQL 查询，返回结果。
设计原则：接口简单，便于后续扩展多种数据库。
"""
import sqlite3
from typing import Any, List

class DBService:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def query(self, sql: str) -> List[Any]:
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            return [{col: val for col, val in zip(columns, row)} for row in data]
        finally:
            conn.close()
