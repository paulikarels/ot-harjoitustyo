from tkinter import Tk 
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
from repositories.exercise_repository import ExerciseRepository
from ui.ui import UI
from databaselogic.database import get_database_connection

class AppService:
    def __init__(self, root):
        """
        Luokan konstruktori joka alustaa uuden AppService-esiintymän.

        Args:
            root: Tkinterin juuriikkunaobjekti..
        """
        self._user_repository = UserRepository(get_database_connection())
        self._course_repository = CourseRepository(get_database_connection())
        self._exercise_repository = ExerciseRepository(get_database_connection())
        self._root = root
        self._ui = UI(
            self._root,
            self._user_repository,
            self._course_repository,
            self._exercise_repository
        )

    def start(self):
        """
        Aloittaa applikaation UI (käyttöliittymän).

        """
        self._ui.start()
