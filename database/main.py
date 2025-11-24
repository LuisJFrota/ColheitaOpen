from database.database import db, Client, BoardGame, Rent, RentBoardGame
from .models.client import ClientData
from peewee import DoesNotExist
from typing import List, Optional

def init_db():
    if(db.is_closed()):
        db.connect()

    db.create_tables([Client, BoardGame, Rent, RentBoardGame])

def createClient(newClient: ClientData) -> Client:  
    return Client.create(
        name = newClient.name, 
        email = newClient.email
        )

def editClient(id: int, newClient: ClientData) -> Client | None:
    try:
        oldClient = Client.get_by_id(id)
    except DoesNotExist:
        return None
    
    oldClient.name = newClient.name
    oldClient.email = newClient.email
    oldClient.save()

    return oldClient

def getClient(id: int) -> Client | None:
    try:
        return Client.get_by_id(id)
    except DoesNotExist:
        return None

def deleteClient(id: int) -> bool:
    try:
        oldClient = Client.get_by_id(id)
    except DoesNotExist:
        return False
    
    oldClient.delete_instance()
    return True

def getAllClient() -> list[Client] | None:
    try:
        return list(Client.select())
    except DoesNotExist:
        return None