from app import Base
from sqlalchemy import Column, Integer, String
from yourapplication.database import Base
import hashlib, uuid

class User(Base):
    """System user record"""

    __tablename__ = 'users'
    id = dColumn(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(128), nullable = False)
    salt = Column(String(36), nullable = False)

    def _encrypt_password(password):
        """hashes the given password with a random salt, returns both"""
        salt = uuid.uuid4().hex
        return {salt: salt, hashed: hashlib.sha512(password + salt).hexdigest()}

    def __init__(self, email, password):
        self.username = username
        self.email = email
        password_data = self._encrypt_password(password)
        self.password = password_data['hashed']
        self.salt = password_data['salt']

    def __repr__(self):
        return '<User %r>' % self.email