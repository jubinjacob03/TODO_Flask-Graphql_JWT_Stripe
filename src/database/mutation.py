import graphene
from modules.core import db, TodosTable, UsersTable
from database.models import Todos, AddTodosFields, Users, AddUsersFields

class AddTodo(graphene.Mutation):
    todo = graphene.Field(lambda: Todos)
    status = graphene.Boolean()

    class Arguments:
        user_id = graphene.String(required = True)
        input = AddTodosFields(required = True)

    @staticmethod
    def mutate(self, info, user_id, input):
        todo = TodosTable(**input, user_id = user_id)
        db.session.add(todo)
        db.session.commit()
        status = True
        return AddTodo(todo = todo, status = status)
    
class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(lambda: Todos)
    status = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)
        user_id = graphene.String(required=True)
        input = AddTodosFields(required=True)

    @staticmethod
    def mutate(self, info, id, user_id, input):
        todo = db.session.query(TodosTable).filter_by(id=id, user_id=user_id).first()

        if todo:
            for field, value in input.items():
                setattr(todo, field, value)
            db.session.commit()
            status = True
        else:
            status = False
        return UpdateTodo(todo=todo, status=status)

class DeleteTodo(graphene.Mutation):
    id = graphene.Int()
    status = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)
        user_id = graphene.String(required=True)

    @staticmethod
    def mutate(self, info, id, user_id):
        todo = db.session.query(TodosTable).filter_by(id=id, user_id=user_id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
            status = True
        else:
            status = False
        return DeleteTodo(id=id, status=status)
    

class AddUser(graphene.Mutation):
    user = graphene.Field(lambda: Users)
    status = graphene.Boolean()

    class Arguments:
        input = AddUsersFields(required = True)


    @staticmethod
    def mutate(self, info, input):
        user = UsersTable(**input)
        db.session.add(user)
        db.session.commit()
        status = True
        return AddUser(user = user, status = status)
    

class Mutation(graphene.ObjectType):
    addTodo = AddTodo.Field()
    updateTodo = UpdateTodo.Field()
    deleteTodo = DeleteTodo.Field()

    addUser = AddUser.Field()
