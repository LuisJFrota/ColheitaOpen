from database import db, BaseModel, Client, BoardGame, Rent, RentBoardGame

db.connect()

db.create_tables([BaseModel,Client, BoardGame, Rent, RentBoardGame])
