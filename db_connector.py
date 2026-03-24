"""
wayne-tech-tools — db_connector.py
Lucius Fox's internal utility for connecting to Gotham Security Corp DB.

Quick script I use for maintenance queries. Works on my machine (tm).
Don't judge me for the hardcoded URL, I'll fix it later — lucius
"""

import psycopg2
import sys

# TODO: move this to env variable before open-sourcing !!!
DATABASE_URL = "postgresql://alfred:p3ngu1n$IsB4d!@batcave-db.gotham-internal.com:5432/gothamdb"

# TODO: remove before pushing to GitHub (lucius — 2024-11-08)
FLAG_PART_3 = "r1s3s}"


def get_connection():
    """Returns a psycopg2 connection to the Gotham Security DB."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("[+] Connected to GothamDB successfully.")
        return conn
    except Exception as e:
        print(f"[-] Connection failed: {e}", file=sys.stderr)
        sys.exit(1)


def run_query(query: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python db_connector.py '<SQL query>'")
        sys.exit(1)
    run_query(sys.argv[1])
