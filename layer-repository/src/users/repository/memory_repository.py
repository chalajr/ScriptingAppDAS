from src.users.repository.abstract_repository import AbstractUserRepository
from src.users.model.user_model import User

class MemoryUserRepository(AbstractUserRepository):

    def __init__(self):
        self._users = []
        self._current_id = 1

    def add(self, user: User):
        user.id = self._current_id
        self._users.append(user)
        self._current_id += 1

    def get_by_id(self, user_id: int) -> User:
        return next((user for user in self._users if user.id == user_id), None)

