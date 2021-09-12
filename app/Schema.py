from app import ma


class ChallengeSchema(ma.Schema):

    class Meta:
        fields = ("index","datetime",
                  "currencys")

challenge_schema = ChallengeSchema()
challenge_schemas = ChallengeSchema(many=True)