#!/usr/bin/env python3
"""This module contains the User class for the user_authentication_service."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """The User class for the user_authentication_service."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
