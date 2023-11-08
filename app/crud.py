from sqlalchemy.orm import Session

from app import models


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

def get_question_by_id(db: Session, id: int):
    return db.query(models.Question).filter(models.Question.id == id).first()
