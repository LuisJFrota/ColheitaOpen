from database.database import Client
from database.models.client import ClientData
from peewee import DoesNotExist

def create_client(new_client: ClientData) -> Client:  
    return Client.create(
        name = new_client.name, 
        email = new_client.email
        )


def edit_client(id: int, new_client: ClientData) -> Client | None:
    try:
        old_client = Client.get_by_id(id)
    except DoesNotExist:
        return None
    
    old_client.name = new_client.name
    old_client.email = new_client.email
    old_client.save()

    return old_client


def get_client(id: int) -> Client | None:
    try:
        return Client.get_by_id(id)
    except DoesNotExist:
        return None


def delete_client(id: int) -> bool:
    try:
        old_client = Client.get_by_id(id)
    except DoesNotExist:
        return False
    
    old_client.delete_instance()
    return True


def get_all_clients() -> list[Client] | None:
    try:
        return list(Client.select())
    except DoesNotExist:
        return None