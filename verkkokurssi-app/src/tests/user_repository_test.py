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
        self.user_repository = UserRepository(self.connection)
        initialize_database()

    def tearDown(self):
        self.user_repository.delete_all_users()
    
    def _cleanup(self):
        self.connection.close()

    def test_create_user(self):
        user = User("TestiKayttaja", "Salasana", False)
        created_user = self.user_repository.create_user(user)
        self.assertIsNotNone(created_user.id) 
        self.assertEqual(created_user.username, "TestiKayttaja")
        self.assertEqual(created_user.password, "Salasana")
        self.assertEqual(created_user.admin, False)

    def test_get_user_by_username_and_password(self):
        user = User("TestiKayttaja", "Salasana", False)
        self.user_repository.create_user(user)
        
        retrieved_user = self.user_repository.get_user_by_username_and_password("TestiKayttaja", "Salasana")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, "TestiKayttaja")
        self.assertEqual(retrieved_user.password, "Salasana")
        self.assertEqual(retrieved_user.admin, False)

    def test_get_all_users(self):
        users_data = [
            ("Testi1", "Sala1", True),
            ("Testi2", "Sala2", False),
            ("Testi3", "Sala3", True)
        ]
        for username, password, admin in users_data:
            user = User(username, password, admin)
            self.user_repository.create_user(user)

        all_users = self.user_repository.get_all_users()
        self.assertEqual(len(all_users), len(users_data))

        for i, user_data in enumerate(users_data):
            self.assertEqual(all_users[i].username, user_data[0])
            self.assertEqual(all_users[i].password, user_data[1])
            self.assertEqual(all_users[i].admin,    user_data[2])