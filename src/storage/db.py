from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "data" / "db" / "space_weather.db"


def _connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(str(DB_PATH))
def init_db():
    con = _connect()
    cursor = con.cursor()
    cursor.executescript('''
                    CREATE TABLE IF NOT EXISTS plasma (
                        time_tag TEXT PRIMARY KEY,
                        density REAL,
                        speed REAL
                    );

                    CREATE TABLE IF NOT EXISTS mag (
                        time_tag TEXT PRIMARY KEY,
                        bz_gsm REAL
                    );

                    CREATE TABLE IF NOT EXISTS kp (
                        time_tag TEXT PRIMARY KEY,
                        kp_index REAL
                    );
                ''')

    con.commit()
    con.close()


def insert_plasma(plasma_data):
    con = _connect()
    cursor = con.cursor()

    cursor.executemany(
        "INSERT OR IGNORE INTO plasma (time_tag, density, speed) VALUES (?, ?, ?)",
        plasma_data
    )
    con.commit()

    count = cursor.execute("SELECT COUNT(*) FROM plasma;").fetchone()
    print(f"Inserted {count[0]} plasma records.")

    minimum = cursor.execute("SELECT MIN(speed) FROM plasma;").fetchone()
    print(f"Minimum speed: ", minimum[0])

    maximum = cursor.execute("SELECT MAX(speed) FROM plasma;").fetchone()
    print(f"Maximum speed: ", maximum[0])

    con.close()


def insert_mag(mag_data):
    con = _connect()
    cursor = con.cursor()

    cursor.executemany(
        "INSERT OR IGNORE INTO mag (time_tag, bz_gsm) VALUES (?, ?)",
        mag_data
    )
    con.commit()

    count = cursor.execute("SELECT COUNT(*) FROM mag;").fetchone()
    print(f"\nInserted {count[0]} mag records.")

    minimum = cursor.execute("SELECT MIN(bz_gsm) FROM mag;").fetchone()
    print(f"Minimum bz: ", minimum[0])

    maximum = cursor.execute("SELECT MAX(bz_gsm) FROM mag;").fetchone()
    print(f"Maximum bz: ", maximum[0])

    con.close()


def insert_kp(kp_data):
    con = _connect()
    cursor = con.cursor()

    cursor.executemany(
        "INSERT OR IGNORE INTO kp (time_tag, kp_index) VALUES (?, ?)",
        kp_data
    )
    con.commit()

    count = cursor.execute("SELECT COUNT(*) FROM kp;").fetchone()
    print(f"\nInserted {count[0]} kp records.")

    minimum = cursor.execute("SELECT MIN(kp_index) FROM kp;").fetchone()
    print(f"Minimum kp: ", minimum[0])

    maximum = cursor.execute("SELECT MAX(kp_index) FROM kp;").fetchone()
    print(f"Maximum kp: ", maximum[0])

    con.close()


def get_latest_n_plasma(n):
    con = _connect()
    cursor = con.cursor()

    cursor.execute(
        "SELECT time_tag, density, speed FROM plasma ORDER BY time_tag DESC LIMIT ?",
        (n,)
    )

    rows = cursor.fetchall()
    rows.reverse()
    con.close()
    return rows


def get_latest_n_mag(n):
    con = _connect()
    cursor = con.cursor()

    cursor.execute(
        "SELECT time_tag, bz_gsm FROM mag ORDER BY time_tag DESC LIMIT ?",
        (n,)
    )

    rows = cursor.fetchall()
    rows.reverse()
    con.close()
    return rows

def get_latest_n_kp(n):
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()

    cursor.execute(
        "SELECT time_tag, kp_index FROM kp ORDER BY time_tag DESC LIMIT ?",
        (n,)
    )

    rows = cursor.fetchall()
    rows.reverse()
    con.close()
    return rows
