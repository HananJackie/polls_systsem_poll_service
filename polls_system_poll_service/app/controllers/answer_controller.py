from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.services.answer_service import AnswerService
from app.database import get_db
from app.models.schemas import AnswerCreate, AnswerResponse, Choice

router = APIRouter()

@router.post("/", response_model=AnswerResponse)
async def save_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    try:
        result = await AnswerService.save_answer(db, answer.dict())
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{answer_id}", response_model=AnswerResponse)
async def update_answer(answer_id: int, new_answer: Choice = Query(...), db: Session = Depends(get_db)):
    return await AnswerService.update_answer(db, answer_id, new_answer.value)

@router.get("/", response_model=list[AnswerResponse])
async def get_answers(db: Session = Depends(get_db)):
    answers = await AnswerService.get_answers(db)
    if not answers:
        raise HTTPException(status_code=404, detail="No answers yet")
    return [AnswerResponse.from_orm(answer) for answer in answers]

@router.get("/user/{user_id}", response_model=list[AnswerResponse])
async def get_answers_by_user(user_id: int, db: Session = Depends(get_db)):
    answers = await AnswerService.get_answers_by_user(db, user_id)
    return [AnswerResponse.from_orm(answer) for answer in answers]

@router.delete("/user/{user_id}", response_model=dict)
async def delete_answers_by_user(user_id: int, db: Session = Depends(get_db)):
    await AnswerService.delete_answers_by_user(db, user_id)
    return {"message": f"All user {user_id} related Answers were deleted successfully"}

@router.get("/question/{question_id}", response_model=list[AnswerResponse])
async def get_answers_by_question(question_id: int, db: Session = Depends(get_db)):
    answers = await AnswerService.get_answers_by_question(db, question_id)
    return [AnswerResponse.from_orm(answer) for answer in answers]

@router.delete("/question/{question_id}", response_model=dict)
async def delete_answers_by_question(question_id: int, db: Session = Depends(get_db)):
    await AnswerService.delete_answers_by_question(db, question_id)
    return {"message": f"All question {question_id} related Answers were deleted successfully"}
