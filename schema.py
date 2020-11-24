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

class QuerySearchBoth(graphene.Union):
    class Meta:
        types = (Student, StudentMetaData)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    search = graphene.List(QuerySearchBoth, q=graphene.String())  # List field for search results

    # Normal Fields
    all_student = SQLAlchemyConnectionField(Student.connection)
    all_student_meta = SQLAlchemyConnectionField(StudentMetaData.connection)


    def resolve_search(self, info, **args):
        q = args.get("q")

        student_query = Student.get_query(info)
        student_meta_query = StudentMetaData.get_query(info)

        students = student_meta_query.filter((StudentMetaData.id.contains(q)) |
                                        (StudentMetaData.student_id.any(StudentModel.id.contains(q)))).all()

        students_meta = student_meta_query.filter(StudentMetaDataModel.id.contains(q)).all()

        return students + students_meta

schema = graphene.Schema(query=Query,types=[Student, StudentMetaData, QuerySearchBoth],  mutation=Mutation)
