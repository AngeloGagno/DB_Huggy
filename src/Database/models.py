from sqlalchemy import Column, String, Integer
from Database.database import Base

class DB_huggy(Base):
    __tablename__ = 'huggy_chats_data'
    id = Column(Integer, primary_key = True, autoincrement=True)
    chat_id = Column(String)
    agent_id = Column(String)
    tabulation_id = Column(String)
    client_id = Column(String)
    status_chat = Column(String)
    creation_date = Column(String)
    update_date = Column(String)
    attended_at_date = Column(String)
    closed_date = Column(String)
