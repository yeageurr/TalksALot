from app.db_config.database_handler import engine, Base

from app.models.messages import Messages
from app.models.users import Accounts

Base.metadata.create_all(engine)