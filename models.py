from db_config import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

class StudentModel(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

class StudentMetaDataModel(Base):
    __tablename__ = 'student_meta'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    course = Column(String(50))
    department = relationship(
        StudentModel,
        backref=backref('student_meta',
                        uselist=True,
                        cascade='delete,all'))