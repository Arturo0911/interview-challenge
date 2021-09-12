from app import ma


class ChallengeSchema(ma.Schema):

    class Meta:
        fields = ("index","datetime",
                  "euro_currency", "chilean_currency",
                  "peruvian_currency")

challenge_schema = ChallengeSchema()
challenge_schemas = ChallengeSchema(many=True)