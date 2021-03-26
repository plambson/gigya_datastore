from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Payload(Base):
    __tablename__ = "payload"
    id = Column(Integer, primary_key=True)
    gigya_id = Column(String(100))
    payload = Column(String(1000))
    created = Column('created', DateTime, default=datetime.datetime.now)
    last_updated = Column('last_updated', DateTime, onupdate=datetime.datetime.now)

    def __init__(self, gigya_id, payload):
        self.gigya_id = gigya_id
        self.payload = payload