from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from database import Base


class Interface(Base):
    __tablename__ = "interfaces"
    id = Column(Integer, primary_key=True)
    connection = Column(Integer)
    name = Column(String(250), nullable = False)
    description = Column(String(250))
    config = Column(MutableDict.as_mutable(JSONB))
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



