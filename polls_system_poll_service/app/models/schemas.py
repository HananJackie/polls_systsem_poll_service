from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class QuestionCreate(BaseModel):
    question_text: str
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None

class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None

class QuestionResponse(BaseModel):
    id: int
    question_text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None

    class Config:
        orm_mode = True

class Choice(Enum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"

class AnswerCreate(BaseModel):
    user_id: int
    question_id: int
    selected_option: Choice

    class Config:
        use_enum_values = True

class AnswerResponse(BaseModel):
    id: int
    user_id: int
    question_id: int
    selected_option: Choice

    class Config:
        orm_mode = True
        use_enum_values = True

class ChoicesStats(BaseModel):
    a: int
    b: int
    c: int
    d: int

class QuestionChoicesStats(BaseModel):
    question_id: int
    choices_stats: ChoicesStats

class QuestionTotalAnswers(BaseModel):
    question_id: int
    total_answers: int

class UserAnswer(BaseModel):
    question_id: int
    selected_option: str

class UserAnswers(BaseModel):
    user_id: int
    answers: List[UserAnswer]

class UserTotalAnswers(BaseModel):
    user_id: int
    total_answers: int