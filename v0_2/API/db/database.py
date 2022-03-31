from db_secret_data import DB_user
from db_secret_data import DB_passwd
from db_secret_data import DB_host
from db_secret_data import DB_port
from db_secret_data import DB_name

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = f'postgresql://{DB_user}:{DB_passwd}@{DB_host}:{DB_port}/{DB_name}'
engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base = declarative_base
