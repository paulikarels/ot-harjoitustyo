import unittest
import sqlite3
from entities.exercise import Exercise
from databaselogic.database import get_database_connection
from databaselogic.initialize_database import initialize_database
from repositories.exercise_repository import ExerciseRepository


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.exercise_repository = ExerciseRepository(self.connection)
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

if __name__ == '__main__':
    unittest.main()
