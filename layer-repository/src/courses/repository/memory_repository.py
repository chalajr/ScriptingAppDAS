from src.courses.repository.abstract_repository import AbstractCourseRepository
from src.courses.model.course_model import Courses

class MemoryCourseRepository(AbstractCourseRepository):

    def __init__(self):
        self._courses = []
        self._current_id = 1

    def add(self, course: Courses):
        course.id = self._current_id
        self._courses.append(course)
        self._current_id += 1

    def get_by_id(self, course_id: int) -> Courses:
        return next((course for course in self._courses if course.id == course_id), None)