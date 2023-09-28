from abc import ABC, abstractmethod

class AbstractUserRepository(ABC):

    @abstractmethod
    def add(self, user):
        pass

    @abstractmethod
    def get_by_id(self, user_id):
        pass
