from database import db, BaseModel, Client, BoardGame, Rent, RentBoardGame
from model.client import ClientData

db.connect()

db.create_tables([BaseModel,Client, BoardGame, Rent, RentBoardGame])

def createClient(newClient):
    
    Client.create(name = newClient.name, email = newClient.email)
    pass

obj = ClientData(name="example", email="example@gmail.com")
createClient(obj)

listClient = Client.select()

for c in listClient:
    print(c.name)