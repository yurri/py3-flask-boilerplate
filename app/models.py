"""All models are defined in the same module
Looks ineffective, but that's more Pythonic.

"""

from sqlalchemy import Column, Integer, String
import hashlib, uuid

from db import Base

class User(Base):
    """System user record"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)

    """As the fields below shouldn't be set directly (they should be both set
    via self.new_password property) they should really be prefixed
    with _, but we don't want the underscore to be propagated to table column name
    """
    password = Column(String(128), nullable = False)
    salt = Column(String(36), nullable = False)

    @property
    def new_password(self):
        return self.password

    @new_password.setter
    def new_password(self, new_password):
        # generating a new encoded password with a new salt
        self.salt = uuid.uuid4().hex
        self.password = hashlib.sha512((new_password + self.salt).encode()).hexdigest()

    def __init__(self, email, password):
        self.email = email
        self.new_password = password

    def __repr__(self):
        return '<User %r>' % self.email
