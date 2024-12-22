from fastapi import FastAPI
from app.controllers.questions_controller import router as questions_router
from app.controllers.answer_controller import router as answer_router
from app.controllers.analytics_controller import router as analytics_router
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(questions_router, prefix="/questions", tags=["Questions"])
app.include_router(answer_router, prefix="/answers", tags=["Answers"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
