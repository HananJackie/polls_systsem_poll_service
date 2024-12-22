from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/questions/{question_id}/choices")
async def get_question_choices_stats(question_id: int, db: Session = Depends(get_db)):
    try:
        stats = await AnalyticsService.get_question_options_stats(db, question_id)
        return stats
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/questions/{question_id}/total")
async def get_total_answers(question_id: int, db: Session = Depends(get_db)):
    try:
        total_answers = await AnalyticsService.get_total_answers(db, question_id)
        return total_answers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}/answers")
async def get_user_answers(user_id: int, db: Session = Depends(get_db)):
    try:
        user_answers = await AnalyticsService.get_user_answers(db, user_id)
        return user_answers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}/total_answers")
async def get_total_questions_answered(user_id: int, db: Session = Depends(get_db)):
    try:
        total_questions_answered = await AnalyticsService.get_total_questions_answered(db, user_id)
        return total_questions_answered
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/questions/")
async def get_all_questions_stats(db: Session = Depends(get_db)):
    try:
        all_questions_stats = await AnalyticsService.get_all_questions_stats(db)
        return all_questions_stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
