from app.repositories.question_repository import QuestionsRepository
from app.repositories.answer_repository import AnswerRepository
from app.models.question_model import Question

class QuestionService:
    @staticmethod
    async def create_question(db, question_data):
        question = Question(**question_data.dict())
        return await QuestionsRepository.create_question(db, question)

    @staticmethod
    async def update_question(db, question_id, updates):
        return await QuestionsRepository.update_question(db, question_id, updates.dict())

    @staticmethod
    async def delete_question(db, question_id):
        await AnswerRepository.delete_answers_by_question(db, question_id)
        await QuestionsRepository.delete_question(db, question_id)

    @staticmethod
    async def get_question(db, question_id):
        return await QuestionsRepository.get_question_by_id(db, question_id)

    @staticmethod
    async def get_all_questions(db):
        return await QuestionsRepository.get_all_questions(db)
