from typing import Optional
from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class QuestionModel(BaseModel):
    id: int
    question_id: int
    text: str
    category: CategoryModel
    answer: str
    tip_cost: Optional[int] = None

    class Config:
        orm_mode = True
