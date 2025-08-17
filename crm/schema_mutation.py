# crm/schema_mutation.py

import graphene

# Define a simple mutation
class CreateMessage(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    # Output fields
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, text):
        return CreateMessage(success=True, message=f"You said: {text}")


# Mutation class wrapper
class Mutation(graphene.ObjectType):
    create_message = CreateMessage.Field()
