'''
This file is used to create the database
'''

from sqlalchemy.orm import sessionmaker
from Portfolio_API.srs.enums import CONNECTION_ROW
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Model = declarative_base(name="Model")

engine = create_engine(CONNECTION_ROW)

Session = sessionmaker(engine, autocommit=False, autoflush=False)

# session = Session()
