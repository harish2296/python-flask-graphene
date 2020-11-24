from models import StudentModel
from models import StudentMetaDataModel
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db_config import db_session


class Student(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel
        interfaces = (relay.Node, )


class StudentMetaData(SQLAlchemyObjectType):
    class Meta:
        model = StudentMetaDataModel
        interfaces = (relay.Node, )

class CreateStudent(graphene.Mutation):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    student = graphene.Field(Student)

    def mutate(root, info, id, name, email):
        student = Student(
            id=id,
            name=name,
            email=email
        )
        model = StudentModel(id=id,name=name,email=email)
        db_session.add(model)
        db_session.commit()
        return CreateStudent(
            id=student.id,
            name=student.name,
            email=student.email)

class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()

class Query(graphene.ObjectType):
    all_student = SQLAlchemyConnectionField(Student.connection)
    all_student_meta = SQLAlchemyConnectionField(StudentMetaData.connection)
    student = relay.Node.Field(Student)

    find_student = graphene.Field(lambda: Student, id=graphene.Int())
    def resolve_find_student(self, info, **kwargs):
        query = Student.get_query(info)
        id = kwargs.get("id")
        return query.filter(StudentModel.id == id).first()



schema = graphene.Schema(query=Query, mutation=Mutation)
