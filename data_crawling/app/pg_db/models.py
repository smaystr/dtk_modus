from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.as_dict().items()
        })

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Position(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column('doc_id', db.Integer)
    number = db.Column('number', db.Integer)
    iddirection = db.Column('iddirection', db.Integer)
    directionname = db.Column('directionname', db.Text)
    init_price = db.Column('init_price', db.Float)
    price = db.Column('price', db.Float)
    amount = db.Column('amount', db.Integer)
    lotSize = db.Column('lotSize', db.Integer)
    fullsize = db.Column('fullsize', db.Integer)
    cost = db.Column('cost', db.Float)
    lotcost = db.Column('lotcost', db.Float)
    idstate = db.Column('idstate', db.Integer)
    statename = db.Column('statename', db.Text)
    idtrade_type = db.Column('idtrade_type', db.Integer)
    goods = db.Column('goods', db.Text)
    unit = db.Column('unit', db.Text)
    deliverytype = db.Column('deliverytype', db.Text)
    idgoods = db.Column('dgoods', db.Integer)
    iddelivery = db.Column('iddelivery', db.Integer)
    comments = db.Column('comments', db.Text)
    ownername = db.Column('ownername', db.Text)
    idowner = db.Column('idowner', db.Integer)
    paymentcondition = db.Column('paymentcondition', db.Text)
    loaddatefrom = db.Column('loaddatefrom', db.Text)
    loaddateto = db.Column('loaddateto', db.Text)
    step = db.Column('step', db.Integer)
    hours_from = db.Column('hours_from', db.Integer)
    hours_till = db.Column('hours_till', db.Integer)
    days = db.Column('days', db.Integer)
    peak_type = db.Column('peak_type', db.Integer)
    withvat = db.Column('withvat', db.Text)
    pawn_typename = db.Column('pawn_typename', db.Text)
    idpawn_type = db.Column('idpawn_type', db.Integer)
    pawn_size = db.Column('pawn_size', db.Integer)
    usd_pawn_size = db.Column('usd_pawn_size', db.Integer)
    pawncomment = db.Column('pawncomment', db.Text)
    minprice = db.Column('minprice', db.Integer)
    maxprice = db.Column('maxprice', db.Integer)
    avgprice = db.Column('avgprice', db.Integer)
    agreecount = db.Column('agreecount', db.Integer)
    resultcost = db.Column('resultcost', db.Integer)
    resultamount = db.Column('resultamount', db.Integer)
    resultfullsize = db.Column('esultfullsize', db.Integer)
    files = db.Column('files', JSON)
