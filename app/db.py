"""Initialises database connection and implements maintenance operations
like creating database structure on new installation

"""
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import path

import config

# build connection string
if config.get('db', 'type') == 'sqlite':
    _connection_string = 'sqlite:///' + path.join(config.DATA_PATH, config.get('db', 'file'))
else:
    raise KeyError("Unrecognised database type in configuration file")

# initialise db connection
engine = create_engine(_connection_string)
# initialise db session to handle threads for us
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# so we can inherit our model classes from Base...
Base = declarative_base()
# ..now define these model classes
import models

def init_db():
    """Initialises db schema, use on first install"""

    print("Creating database tables and default config")

    # re-create tables for all the models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    admin = models.User('admin@localhost', 'admin')
    print(admin)
    session.add(admin)

    session.commit()
    print("Database initialised")

if __name__ == '__main__':
    init_db()
    print("Database schema initialised")
