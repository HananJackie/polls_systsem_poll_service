from sqlalchemy.orm import Session
from app.models.question_model import Question

class QuestionsRepository:
    @staticmethod
    async def create_question(db: Session, question: Question):
        db.add(question)
        db.commit()
        db.refresh(question)
        return question

    @staticmethod
    async def get_question_by_id(db: Session, question_id: int):
        return db.query(Question).filter(Question.id == question_id).first()

    @staticmethod
    async def update_question(db: Session, question_id: int, updates: dict):
        question = db.query(Question).filter(Question.id == question_id).first()
        if question:
            for key, value in updates.items():
                setattr(question, key, value)
            db.commit()
            db.refresh(question)
        return question

    @staticmethod
    async def delete_question(db: Session, question_id: int):
        question = db.query(Question).filter(Question.id == question_id).first()
        if question:
            db.delete(question)
            db.commit()

    @staticmethod
    async def get_all_questions(db: Session):
        return db.query(Question).all()
