from database import db, BaseModel, Client, BoardGame, Rent, RentBoardGame
from model.client import ClientData

db.connect()

db.create_tables([BaseModel,Client, BoardGame, Rent, RentBoardGame])

def createClient(newClient):  
    Client.create(name = newClient.name, email = newClient.email)
    pass

def editClient(id, newClient):
    oldClient = Client.get_by_id(id)
    oldClient.name = newClient.name
    oldClient.email = newClient.email
    oldClient.save()
    pass

def getClient(id):
    pass

def deleteClient(id):
    pass

obj = ClientData(name="editName", email="editEmail@gmail.com")
editClient(1,obj)

listClient = Client.select()
for c in listClient: 
    print(c.name)