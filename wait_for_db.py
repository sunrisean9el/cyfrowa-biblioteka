import time
import psycopg2
from psycopg2 import OperationalError

MAX_RETRIES = 10

while MAX_RETRIES > 0:
    try:
        conn = psycopg2.connect(
            dbname="bibliodb",
            user="bibliouser",
            password="bibliopass",
            host="db",
            port="5432"
        )
        conn.close()
        print("PostgreSQL is ready!")
        break
    except OperationalError:
        print("Waiting for PostgreSQL...")
        MAX_RETRIES -= 1
        time.sleep(2)

if MAX_RETRIES == 0:
    print("Failed to connect to PostgreSQL. Exiting.")
    exit(1)
