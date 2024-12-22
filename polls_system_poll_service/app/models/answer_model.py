from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base


class Answer(Base):
    __tablename__ = 'users_answers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # Foreign key can be added if tied to UserService DB
    question_id = Column(Integer, ForeignKey('questions.id', ondelete="CASCADE"), nullable=False)
    selected_option = Column(String(1), nullable=False)

    # Unique constraint to ensure users answer each question only once
    __table_args__ = (UniqueConstraint('question_id', 'user_id', name='_question_user_uc'),)

    # poll = relationship("Question", back_populates="answers")
