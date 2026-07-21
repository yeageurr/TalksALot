from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from conf import psql_config as config
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
  pass


def generate_engine(*, username, passwd, host, port, db_name):
  url = f"postgresql+psycopg2://{username}:{passwd}@{host}:{port}/{db_name}"

  if not database_exists(url):
    create_database(url, encoding="utf8", template=None)

  try:
    engine = create_engine(url, pool_size=20, echo=True)
    return engine
  except Exception as e:
    print(e)


engine = generate_engine(
  username=config["username"],
  passwd=config["password"],
  host=config["host"],
  port=config["port"],
  db_name=config["db"],
)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def my_database():
  db = session()
  try:
    yield db
  finally:
    db.close()
