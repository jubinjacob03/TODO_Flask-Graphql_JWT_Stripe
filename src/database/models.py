import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from modules.core import TodosTable, UsersTable

# Todo Models

class Todos(SQLAlchemyObjectType):
    class Meta:
        model = TodosTable


class TodosFields:
    id = graphene.Int()
    title = graphene.String(required = True)
    description = graphene.String(required = True)
    time = graphene.DateTime()


class AddTodosFields(graphene.InputObjectType, TodosFields):
    pass


# Users Models

class Users(SQLAlchemyObjectType):
    class Meta:
        model = UsersTable


class UsersFields:
    id = graphene.String()
    email = graphene.String(required = True)
    pass_hash = graphene.String(required = True)
    premium = graphene.Boolean()


class AddUsersFields(graphene.InputObjectType, UsersFields):
    pass
