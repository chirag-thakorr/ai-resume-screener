import time
import psycopg2
import os

while True:
    try:
        psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=5432,
        )
        print("✅ DB Ready!")
        break
    except psycopg2.OperationalError:
        print("⏳ Waiting for DB...")
        time.sleep(2)
