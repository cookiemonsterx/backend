import graphene
import music.schema

class Query(music.schema.Query, graphene.ObjectType):
    #this class will inherit from multiple queries as we add more apps to project
    pass

class Mutation(music.schema.Mutation, graphene.ObjectType):
    #this class will inherit from multiple queries as we add more apps to project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)



