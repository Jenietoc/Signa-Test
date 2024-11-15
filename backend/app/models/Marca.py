from datetime import datetime
from app.extension import db

class Marca(db.Model):
    __tablename__ = "marca"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
