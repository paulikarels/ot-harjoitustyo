from entities.course import Course
from entities.exercise import Exercise
from entities.user import User

from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
from repositories.exercise_repository import ExerciseRepository

class AppService:

    def __init__(self, course_repository=None, exercise_repository=None, user_repository=None):
        self._user = None
        self._course_repository = course_repository
        self._exercise_repository = exercise_repository
        self._user_repository = user_repository

    def create_user(self, username, password, admin=True):
        if self._user_repository.find_by_username(username):
            raise ValueError("Username already exists")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = User(username, hashed_password, admin)

        return self._user_repository.create(user)


    def create_course(self, title, credits):
        course = Course(title, credits, user = self._user)

        return self._course_repository.create(course)
        

app_service = AppService()