# インポート
import sqlite3


def connect_db():
    # データベースに接続
    file_name = "d_bot.sqlite"
    conn = sqlite3.connect(file_name)
    return conn


def create_table(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE roles_grant(
        roles_grant_id INTEGER PRIMARY KEY,
        user_id TEXT,
        role_id TEXT,
        created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
        updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
        )""")
