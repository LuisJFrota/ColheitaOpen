from database.database import RentBoardGame
from database.models.rentboardgame import RentBoardGameData
from peewee import DoesNotExist

def create_rentboardgame(new_rent: RentBoardGameData) -> RentBoardGame:  
    return RentBoardGame.create(
        date = new_rent.date, 
        totalCost = new_rent.totalCost,
        client = new_rent.client
        )


def edit_rentboardgame(id: int, new_rent: RentBoardGameData) -> RentBoardGame | None:
    try:
        old_rent = RentBoardGame.get_by_id(id)
    except DoesNotExist:
        return None
    
    old_rent.date = new_rent.date
    old_rent.totalCost = new_rent.totalCost
    old_rent.client = new_rent.client
    old_rent.save()

    return old_rent


def get_rentboardgame(id: int) -> RentBoardGameData | None:
    try:
        return RentBoardGameData.get_by_id(id)
    except DoesNotExist:
        return None


def delete_rentboardgame(id: int) -> bool:
    try:
        old_rent = RentBoardGameData.get_by_id(id)
    except DoesNotExist:
        return False
    
    old_rent.delete_instance()
    return True


def get_all_rentboardgames() -> list[RentBoardGameData] | None:
    try:
        return list(RentBoardGameData.select())
    except DoesNotExist:
        return None