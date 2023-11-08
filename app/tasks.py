from pprint import pprint

import requests
from sqlalchemy.orm import Session

from app.database import get_or_create
from app.models import Question, Category

JSERVICE_URL: str = "https://jservice.io/api/random"

def get_questions_from_jService(db: Session, amount: int = 1):
    response = requests.get(JSERVICE_URL, params={"count": amount}).json()
    pprint(response)

    for question in response:
        category = get_or_create(db, Category, title=question['category']['title'])
        _ = get_or_create(
            db, Question,
            question_id=question['id'],
            text=question['question'],
            answer=question['answer'][3:-4],
            tip_cost=question['value'],
            category=category
        )

