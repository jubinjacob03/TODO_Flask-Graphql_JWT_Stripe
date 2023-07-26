import graphene
from database.query import Query
from database.models import Todos, Users
from database.mutation import Mutation

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[Todos, Users]
)