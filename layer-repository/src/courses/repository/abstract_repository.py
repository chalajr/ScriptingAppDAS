from abc import ABC, abstractmethod

class AbstractCourseRepository(ABC):

    @abstractmethod
    def add(self, course):
        pass

    @abstractmethod
    def get_by_id(self, course_id):
        pass
