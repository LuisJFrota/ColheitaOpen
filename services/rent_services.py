from database.database import Rent
from database.models.rent import RentData
from peewee import DoesNotExist

def create_rent(new_rent: RentData) -> Rent:  
    return Rent.create(
        date = new_rent.date, 
        totalCost = new_rent.totalCost,
        client = new_rent.client
        )


def edit_rent(id: int, new_rent: RentData) -> Rent | None:
    try:
        old_rent = Rent.get_by_id(id)
    except DoesNotExist:
        return None
    
    old_rent.date = new_rent.date
    old_rent.totalCost = new_rent.totalCost
    old_rent.client = new_rent.client
    old_rent.save()

    return old_rent


def get_rent(id: int) -> RentData | None:
    try:
        return RentData.get_by_id(id)
    except DoesNotExist:
        return None


def delete_rent(id: int) -> bool:
    try:
        old_rent = RentData.get_by_id(id)
    except DoesNotExist:
        return False
    
    old_rent.delete_instance()
    return True


def get_all_rents() -> list[RentData] | None:
    try:
        return list(RentData.select())
    except DoesNotExist:
        return None