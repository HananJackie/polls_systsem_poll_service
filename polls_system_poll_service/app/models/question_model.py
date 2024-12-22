from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String(255), nullable=False)
    option_a = Column(String(100), nullable=False)
    option_b = Column(String(100), nullable=False)
    option_c = Column(String(100), nullable=False)
    option_d = Column(String(100), nullable=False)

    # answers = relationship("Answer", back_populates="poll", cascade="all, delete-orphan")