import io
import os
import sqlite3
import time
from typing import Optional

import pandas as pd
from openbb_core.app.utils import get_user_cache_directory


class SQLiteCache:
    def __init__(self, db_path: str, expire: int = 3600):
        self.db_path = db_path
        self.expire = expire
        self._ensure_directory_exists()
        self._initialize_table()

    def _ensure_directory_exists(self):
        """确保数据库目录存在"""
        directory = os.path.dirname(self.db_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _initialize_table(self):
        """初始化缓存表"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    data BLOB,
                    timestamp INTEGER
                )
                """
            )

    def get(self, key: str) -> Optional[pd.DataFrame]:
        """获取缓存"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT data, timestamp FROM cache WHERE key = ?",
                (key,),
            )
            result = cursor.fetchone()
            if result:
                data, timestamp = result
                if int(time.time()) < timestamp:  # 检查缓存是否过期
                    return pd.read_pickle(io.BytesIO(data))  # 从字节流加载 DataFrame
                else:
                    self.delete(key)  # 如果过期，删除缓存
        return None

    def set(self, key: str, df: pd.DataFrame):
        """设置缓存"""
        with sqlite3.connect(self.db_path) as conn:
            timestamp = int(time.time()) + self.expire
            buffer = io.BytesIO()
            df.to_pickle(buffer)  # 将 DataFrame 序列化到字节流
            buffer.seek(0)
            data = buffer.read()
            conn.execute(
                "INSERT OR REPLACE INTO cache (key, data, timestamp) VALUES (?, ?, ?)",
                (key, data, timestamp),
            )

    def delete(self, key: str):
        """删除指定键的缓存"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache WHERE key = ?", (key,))

    def clear_expired(self):
        """清理过期的缓存"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM cache WHERE timestamp < ?", (int(time.time()),))


# 使用示例
if __name__ == "__main__":
    cache = SQLiteCache(
        db_path=f"{get_user_cache_directory()}/ddb/etf_fund.db", expire=24 * 3600 * 2
    )  # 创建缓存实例，缓存有效期为两天
