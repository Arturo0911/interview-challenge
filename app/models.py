from app import db



class PythonChallenge(db.Model):
    __tablename__ = "python_challenge"
    index = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(20), index=True, nullable=False)
    currencys = db.Column(db.Float, index=True, nullable=False)

    def __init__(self, datetime: str,currencys: float,) -> None:
                
        self.datetime  = datetime
        self.currencys  = currencys