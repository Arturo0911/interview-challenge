from app import db



class PythonChallenge(db.Model):
    __tablename__ = "python_challenge"
    index = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(20), index=True, nullable=False)
    euro_currency = db.Column(db.Float, index=True, nullable=False)
    chilean_currency = db.Column(db.Float, index=True, nullable=False)
    peruvian_currency = db.Column(db.Float, index=True, nullable=False)

    def __init__(self, datetime: str,euro_currency: float, chilean_currency: float, peruvian_currency: float,) -> None:
                
        self.datetime  = datetime
        self.euro_currency  = euro_currency
        self.chilean_currency  = chilean_currency
        self.peruvian_currency  = peruvian_currency
