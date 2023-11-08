from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, nullable=False, unique=True)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question_id = Column(Integer, index=True, unique=True)
    text = Column(String)
    category_id = Column(ForeignKey("categories.id", ondelete="CASCADE"))
    answer = Column(String)
    tip_cost = Column(Integer, nullable=True)

    category = relationship("Category", backref='questions', uselist=False)