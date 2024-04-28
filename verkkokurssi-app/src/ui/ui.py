import secrets
from tkinter import Tk 
from .login_view import LoginView
from .sign_up_view import SignupView
from .online_course_view import OnlineCourseView
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
from repositories.exercise_repository import ExerciseRepository
from .exercise_view import ExerciseView
from entities.user import User
from entities.course import Course
from databaselogic.database import get_database_connection

class UI:
    def __init__(self, root, user_repository, course_repository, exercise_repository):
        self._user_repository = user_repository
        self._course_repository = course_repository
        self._exercise_repository = exercise_repository
        self._root = root
        self._current_view = None
        self._current_user = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_handle_sign_up_view
        )
        self._current_view.pack()

    def _handle_login(self, username, password):
        user = self._user_repository.get_user_by_username_and_password(username, password)
        if user:
            if user.password == password:
                print("Login successful!")
                self._current_user = user
                self._show_online_course_view()
                return

            error_message = "Incorrect password"
        else:
            error_message = "Username not found"
        print("Login failed:", error_message)
        self._current_view.clear_password_field()

    def _show_handle_sign_up_view(self):
        self._hide_current_view()

        self._current_view = SignupView(
            self._root,
            self._handle_signup,
            self._show_login_view
        )
        self._current_view.pack()

    def _handle_signup(self, username, password, admin):
        new_user = User(self.generate_random_id(), username, password, admin)

        user_repository = UserRepository(get_database_connection())

        user_repository.create_user(new_user)

    def _show_online_course_view(self):
        self._hide_current_view()

        exercise_view = ExerciseView(self._root, self._show_online_course_view)

        self._current_view = OnlineCourseView(
            self._root, self._handle_course,
            self._get_courses, exercise_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _handle_course(self, title, creditss):
        new_course = Course(self.generate_random_id() ,title, creditss, self._current_user)

        course_repository = CourseRepository(get_database_connection())

        course_repository.create_course(new_course, self._current_user.id)

    def _show_exercise_view(self):
        self._hide_current_view()

        self._current_view = ExerciseView(self._root, self._show_online_course_view)

        self._current_view.pack()

    def _get_courses(self):
        if self._current_user:
            user_id = self._current_user.id
            return self._course_repository.get_course_with_userid(user_id)

        return []

    @staticmethod
    def generate_random_id(length=10):
        return ''.join(
                secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                for _ in range(length)
            )
