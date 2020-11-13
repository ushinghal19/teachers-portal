import graphene

s = "goodbye"

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    new_field = graphene.String(default_value=s)


schema = graphene.Schema(query=Query)
