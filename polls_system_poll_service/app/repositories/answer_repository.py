from sqlalchemy.orm import Session
from app.models.answer_model import Answer

class AnswerRepository:
    @staticmethod
    async def save_answer(db: Session, answer_data: dict):
        new_answer = Answer(**answer_data)
        db.add(new_answer)
        db.commit()
        db.refresh(new_answer)
        return new_answer

    @staticmethod
    async def update_answer(db: Session, answer_id: int, new_option: str):
        print()
        answer = db.query(Answer).filter(Answer.id == answer_id).first()
        if answer:
            answer.selected_option = new_option
            db.commit()
            db.refresh(answer)
        return answer

    @staticmethod
    async def get_answers_by_user(db: Session, user_id: int):
        return db.query(Answer).filter(Answer.user_id == user_id).all()

    @staticmethod
    async def delete_answers_by_user(db: Session, user_id: int):
        db.query(Answer).filter(Answer.user_id == user_id).delete()
        db.commit()

    @staticmethod
    async def get_answers_by_question(db: Session, question_id: int):
        return db.query(Answer).filter(Answer.question_id == question_id).all()

    @staticmethod
    async def delete_answers_by_question(db: Session, question_id: int):
        db.query(Answer).filter(Answer.question_id == question_id).delete()
        db.commit()

    @staticmethod
    async def get_answers(db: Session):
        return db.query(Answer).all()
