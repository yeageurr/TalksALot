from pathlib import Path

psql_config = {
  "username": "postgres",
  "password": "mypsql_db",
  "host": "localhost",
  "port": 5432,
  "db": "talksalot"
}

BASE = Path(__file__).resolve().parent