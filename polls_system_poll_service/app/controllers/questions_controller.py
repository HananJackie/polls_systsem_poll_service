from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.question_service import QuestionService
from app.database import get_db
from app.models.schemas import QuestionCreate, QuestionUpdate, QuestionResponse

router = APIRouter()

@router.post("/", response_model=QuestionResponse)
async def create_question(question_data: QuestionCreate, db: Session = Depends(get_db)):
    return QuestionResponse.from_orm(await QuestionService.create_question(db, question_data))

@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int, db: Session = Depends(get_db)):
    question = await QuestionService.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionResponse.from_orm(question)

@router.get("/", response_model=list[QuestionResponse])
async def get_all_questions(db: Session = Depends(get_db)):
    questions = await QuestionService.get_all_questions(db)
    if not questions:
        raise HTTPException(status_code=404, detail="There are no questions")
    return [QuestionResponse.from_orm(question) for question in questions]

@router.put("/{question_id}", response_model=QuestionResponse)
async def update_question(question_id: int, updates: QuestionUpdate, db: Session = Depends(get_db)):
    return QuestionResponse.from_orm(await QuestionService.update_question(db, question_id, updates))

@router.delete("/{question_id}", response_model=dict)
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    await QuestionService.delete_question(db, question_id)
    return {"message": "Question and associated answers were deleted successfully"}
