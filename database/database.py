from peewee import *
import datetime
from dotenv import load_dotenv
import os

db = SqliteDatabase(os.getenv("DATABASE_NAME"))

class BaseModel(Model):
    updatedAt = DateTimeField(default=datetime.datetime.now)
    createdAt = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Client(BaseModel):
    name = CharField()
    email = CharField(unique=True)


class BoardGame(BaseModel):
    boardGameName = CharField()
    cost = FloatField()
    playerCount = IntegerField()


class Rent(BaseModel):
    date = DateField()
    totalCost = FloatField()
    client = ForeignKeyField(Client, backref="rents")

class RentBoardGame(BaseModel):
    rent = ForeignKeyField(Rent, backref="games")
    boardGame = ForeignKeyField(BoardGame, backref="rents")
    quantity = IntegerField(default=1)
