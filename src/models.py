from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, DateTime, Float
from database import Base
import datetime


class Interface(Base):
    __tablename__ = "interfaces"
    id = Column(Integer, primary_key=True)
    connection = Column(Integer)
    name = Column(String(250), nullable = False)
    description = Column(String(250))
    config = Column(Float)
    type = Column(String(50))
    infra_type = Column(String(50))
    port_channel_id = Column(Integer)
    max_frame_size = Column(Integer)


    def __init__(self, name=None, description=None, max_frame_size=None, config=None, port_channel_id=None):
        self.name = name
        self.description = description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id



