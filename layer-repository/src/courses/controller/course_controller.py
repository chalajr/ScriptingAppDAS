from flask import Blueprint, jsonify, request
from src.courses.model.course_model import Courses
from src.courses.repository.memory_repository import MemoryCourseRepository


blueprint = Blueprint('course_controller', __name__)
course_repository = MemoryCourseRepository()

# Endpoint to insert courses
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    # Get the course data from the request
    course_data = request.get_json()

    # Check if the course exists
    course = Courses(name=course_data["name"], description=course_data["description"])
    if any(c.name == course.name for c in course_repository._courses):
        # If the course exists, return a 400 error
        return jsonify({"message": "Course already exists"}), 400
    
    # Add the new course to the repository
    course_repository.add(course)

    # Return the newly inserted course  
    return jsonify(course)

# Endpoint to retrieve courses based on course_id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    # Find the course with the given course_id
    course = course_repository.get_by_id(int(course_id))

    # If the course is not found, return a 404 error
    if course is None:
        return jsonify({"message": "Course not found"}), 404

    # Return the retrieved course
    return jsonify(course)
