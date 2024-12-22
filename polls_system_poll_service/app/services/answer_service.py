from app.api.user_service_client import UserServiceClient
from app.repositories.answer_repository import AnswerRepository
from fastapi import HTTPException


class AnswerService:

    @staticmethod
    async def save_answer(db, answer_data: dict):
        user_id = answer_data.get("user_id")
        question_id = answer_data.get("question_id")

        # Validate user registration
        is_registered = await UserServiceClient.is_user_registered(user_id)
        if not is_registered:
            raise HTTPException(status_code=403, detail="User is not registered")

        # Validate if the user has already answered the question
        existing_answers = await AnswerRepository.get_answers_by_user(db, user_id)
        if any(answer.question_id == question_id for answer in existing_answers):
            raise HTTPException(status_code=400, detail="User has already answered this question")

        # Save the answer
        return await AnswerRepository.save_answer(db, answer_data)

    @staticmethod
    async def update_answer(db, answer_id, new_option):
        return await AnswerRepository.update_answer(db, answer_id, new_option)

    @staticmethod
    async def get_answers_by_user(db, user_id):
        return await AnswerRepository.get_answers_by_user(db, user_id)

    @staticmethod
    async def delete_answers_by_user(db, user_id):
        await AnswerRepository.delete_answers_by_user(db, user_id)

    @staticmethod
    async def get_answers_by_question(db, question_id):
        return await AnswerRepository.get_answers_by_question(db, question_id)

    @staticmethod
    async def delete_answers_by_question(db, question_id):
        await AnswerRepository.delete_answers_by_question(db, question_id)

    @staticmethod
    async def get_answers(db):
        return await AnswerRepository.get_answers(db)

