import http
from typing import List

from fastapi import Depends, BackgroundTasks, APIRouter
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import QuestionModel
from app.tasks import load_questions_from_jService


router = APIRouter(
    prefix='/api',
    tags=['questions']
)


@router.get('/questions/', response_model=List[QuestionModel])
async def get_questions(db: Session = Depends(get_db)):
    questions = crud.get_questions(db)
    return questions


@router.get('/questions/{id}/', response_model=QuestionModel)
async def get_question_by_id(id: int,
                             db: Session = Depends(get_db)):
    question = crud.get_question_by_id(db, id)
    return question


@router.get("/load-questions/{amount}/")
async def post_questions(amount: int,
                         background_tasks: BackgroundTasks,
                         db: Session = Depends(get_db)):
    background_tasks.add_task(lambda: load_questions_from_jService(db, amount))
    return {
        "message": f"{amount} questions loaded",
        "status": http.HTTPStatus.OK
    }
