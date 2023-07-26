import graphene
from modules.core import TodosTable, UsersTable
from database.models import Todos, Users

class Query(graphene.ObjectType):
    get_todos = graphene.List(Todos, user_id = graphene.String())
    get_user_by_email = graphene.Field(Users, email = graphene.String())
    
    @staticmethod
    def resolve_get_todos(parent, info, **kwargs):
        user_id = kwargs.get("user_id")
        return Todos.get_query(info).filter(TodosTable.user_id.contains(user_id)).all()

    @staticmethod
    def resolve_get_user_by_email(parent, info, **kwargs):
        email = kwargs.get("email")
        return Users.get_query(info).filter(UsersTable.email.contains(email)).first()