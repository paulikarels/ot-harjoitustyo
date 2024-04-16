import bcrypt
from entities.course import Course
from entities.user import User

class AppService:

    def __init__(self, course_repository=None, exercise_repository=None, user_repository=None):
        self._user = None
        self._course_repository = course_repository
        self._exercise_repository = exercise_repository
        self._user_repository = user_repository

    def create_user(self, username, password, admin=True):
        if self._user_repository.find_by_username(username):
            raise ValueError("Username already exists")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'),
            bcrypt.gensalt())

        user = User(username, hashed_password, admin)

        return self._user_repository.create(user)

    def create_course(self, title, creditss):
        course = Course(title, creditss, user = self._user)

        return self._course_repository.create(course)

app_service = AppService()
