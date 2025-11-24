from database.database import db, Client, BoardGame, Rent, RentBoardGame

def init_db():
    if(db.is_closed()):
        db.connect()

    db.create_tables([Client, BoardGame, Rent, RentBoardGame])