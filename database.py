import sqlite3
from datetime import datetime

DB = "logs/speed_history.db"

def init_db():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results(
        time TEXT,
        download REAL,
        upload REAL,
        ping REAL,
        jitter REAL,
        packet_loss REAL
    )
    """)

    conn.commit()
    conn.close()


def save_result(download,upload,ping,jitter,loss):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO results VALUES(?,?,?,?,?,?)
    """,(datetime.now(),download,upload,ping,jitter,loss))

    conn.commit()
    conn.close()