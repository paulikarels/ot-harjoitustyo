import unittest
import sqlite3
from entities.exercise import Exercise
from entities.user import User
from entities.course import Course
from databaselogic.database import get_database_connection
from databaselogic.initialize_database import initialize_database
from repositories.course_repository import CourseRepository
from repositories.user_repository import UserRepository
from repositories.exercise_repository import ExerciseRepository


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.exercise_repository = ExerciseRepository(self.connection)
        self.course_repository = CourseRepository(self.connection)
        self.user_repository = UserRepository(self.connection)
        initialize_database()

    def tearDown(self):
        self.exercise_repository.delete_all_exercises()

    def test_create_exercise(self):
        exercise = Exercise(1, "Question 1", False, 1)
        created_exercise = self.exercise_repository.create(exercise)
        self.assertIsNotNone(created_exercise.id)

    def test_get_all_exercises(self):
        exercise = Exercise(1, "Question 1", False, 1)
        self.exercise_repository.create(exercise)
        exercises = self.exercise_repository.get_all_exercises()
        self.assertTrue(len(exercises) > 0)

    def test_get_all_exercises2(self):
        user = User(123,"TestiKayttaja", "Salasana", False)
        created_user = self.user_repository.create_user(user)
        course = Course(1, "Testi Kurssi", 5, created_user.id)
        created_course = self.course_repository.create_course(course, created_user.id)
        exercise = Exercise(1, "Question 1", False, 1)
        self.exercise_repository.create(exercise)
        exercises = self.exercise_repository.get_all_exercises()
        self.assertTrue(len(exercises) > 0)

if __name__ == '__main__':
    unittest.main()
