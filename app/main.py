import http
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import QuestionModel
from app.tasks import get_questions_from_jService

app = FastAPI()


@app.get('/questions/', response_model=List[QuestionModel])
async def get_questions(db: Session = Depends(get_db)):
    questions = crud.get_questions(db)
    return questions

@app.get('/questions/{id}/', response_model=QuestionModel)
async def get_question_by_id(id: int, db: Session = Depends(get_db)):
    question = crud.get_question_by_id(db, id)
    return question


@app.get("/load-questions/{amount}/")
async def post_questions(amount: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    background_tasks.add_task(lambda a=amount: get_questions_from_jService(db, a))
    return {"message": http.HTTPStatus.OK}



if __name__ == '__main__':
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)
