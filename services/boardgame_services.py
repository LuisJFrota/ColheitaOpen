from database.database import BoardGame
from database.models.boardgame import BoardGameData
from peewee import DoesNotExist

def create_boardgame(new_game: BoardGameData) -> BoardGame:  
    return BoardGame.create(
        boardGameName = new_game.boardGameName, 
        cost = new_game.cost,
        playerCount = new_game.playerCount
        )


def edit_boardgame(id: int, new_game: BoardGameData) -> BoardGame | None:
    try:
        old_game = BoardGame.get_by_id(id)
    except DoesNotExist:
        return None
    
    old_game.boardGameName = new_game.boardGameName, 
    old_game.cost = new_game.cost,
    old_game.playerCount = new_game.playerCount
    old_game.save()

    return old_game


def get_boardgame(id: int) -> BoardGame | None:
    try:
        return BoardGame.get_by_id(id)
    except DoesNotExist:
        return None


def delete_boardgame(id: int) -> bool:
    try:
        old_game = BoardGame.get_by_id(id)
    except DoesNotExist:
        return False
    
    old_game.delete_instance()
    return True


def getA_all_boardgames() -> list[BoardGame] | None:
    try:
        return list(BoardGame.select())
    except DoesNotExist:
        return None