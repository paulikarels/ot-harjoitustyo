import unittest
from entities.user import User
from entities.course import Course
from entities.exercise import Exercise
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
from repositories.exercise_repository import ExerciseRepository
from databaselogic.database import get_database_connection
from databaselogic.initialize_database import initialize_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.repository = UserRepository(self.connection)
        initialize_database()

    def tearDown(self):
        self.repository.delete_all_users()
        self.connection.close()

    def test_create_user(self):
        user = User("TestiKayttaja", "Salasana", False)
        created_user = self.repository.create_user(user)
        self.assertIsNotNone(created_user.id) 
        self.assertEqual(created_user.username, "TestiKayttaja")
        self.assertEqual(created_user.password, "Salasana")
        self.assertEqual(created_user.admin, False)