import graphene
import crm.schema
from crm.models import Product


class Query(crm.schema.Query, graphene.ObjectType):
    # Project-level Query that inherits from app-level Query
    pass


class Mutation(crm.schema.Mutation, graphene.ObjectType):
    # Project-level Mutation that inherits from app-level Mutation
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
