from sqlalchemy.orm import Session
from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionsRepository
from app.models.schemas import QuestionChoicesStats, ChoicesStats, QuestionTotalAnswers, UserAnswers, UserAnswer, \
    UserTotalAnswers


class AnalyticsService:
    @staticmethod
    async def get_question_options_stats(db: Session, question_id: int):
        answers = await AnswerRepository.get_answers_by_question(db, question_id)
        stats = await AnalyticsService.calculate_choices_stats(answers)
        return QuestionChoicesStats(question_id=question_id, choices_stats=ChoicesStats(**stats))

    @staticmethod
    async def get_total_answers(db: Session, question_id: int):
        answers = await AnswerRepository.get_answers_by_question(db, question_id)
        return QuestionTotalAnswers(question_id=question_id, total_answers=len(answers))

    @staticmethod
    async def get_user_answers(db: Session, user_id: int):
        answers = await AnswerRepository.get_answers_by_user(db, user_id)
        user_answers = [UserAnswer(question_id=answer.question_id, selected_option=answer.selected_option) for answer in answers]
        return UserAnswers(user_id=user_id, answers=user_answers)

    @staticmethod
    async def get_total_questions_answered(db: Session, user_id: int):
        answers = await AnswerRepository.get_answers_by_user(db, user_id)
        return UserTotalAnswers(user_id=user_id, total_answers=len(answers))

    @staticmethod
    async def get_all_questions_stats(db: Session):
        questions = await QuestionsRepository.get_all_questions(db)
        result = []
        for question in questions:
            answers = await AnswerRepository.get_answers_by_question(db, question.id)
            stats = await AnalyticsService.calculate_choices_stats(answers)
            result.append({
                "question_id": question.id,
                "question_text": question.question_text,
                "options": {
                    "a": question.option_a,
                    "b": question.option_b,
                    "c": question.option_c,
                    "d": question.option_d,
                },
                "stats": ChoicesStats(**stats)
            })
        return result

    @staticmethod
    async def calculate_choices_stats(answers):
        stats = {"a": 0, "b": 0, "c": 0, "d": 0}
        for answer in answers:
            stats[answer.selected_option] += 1
        return stats
