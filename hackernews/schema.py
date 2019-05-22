import graphene

import links.schema

class Query(links.schema.Query, graphene.ObjectType):
    ...

class Mutation(links.schema.Mutation, graphene.ObjectType):
    ...

schema = graphene.Schema(query=Query, mutation=Mutation)