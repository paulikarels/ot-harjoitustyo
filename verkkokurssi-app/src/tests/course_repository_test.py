import unittest
from entities.user import User
from entities.course import Course
from repositories.course_repository import CourseRepository
from repositories.user_repository import UserRepository
from databaselogic.database import get_database_connection
from databaselogic.initialize_database import initialize_database

class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.course_repository = CourseRepository(self.connection)
        self.user_repository = UserRepository(self.connection)
        self.user = User(2,"TestiKayttaja", "Salasana", False)
        initialize_database()

    def tearDown(self):
        self.course_repository.delete_all_courses()
    
    def _cleanup(self):
        self.connection.close()

    def test_create_course(self):
        created_user = self.user_repository.create_user(self.user)
        course = Course("Testi Kurssi", 3, created_user.id)
        created_course = self.course_repository.create_course(course, created_user.id)
        self.assertIsNotNone(created_course.id)
        self.assertEqual(created_course.title, "Testi Kurssi")
        self.assertEqual(created_course.credits, 3)
        self.assertEqual(created_course.user, created_user.id)

    def test_get_all_courses(self):
        courses_data = [
            ("Kurssi1", 3, "Kayttaja1"),
            ("Kurssi2", 4, "Kayttaja2"),
            ("Kurssi3", 5, "Kayttaja3")
        ]

        users_data = [
            (3,"Testi1", "Sala1", True),
            (4,"Testi2", "Sala2", False),
            (5,"Testi3", "Sala3", True)
        ]
        
        user_ids = []
        for ids, username, password, admin in users_data:
            user = User(ids, username, password, admin)
            created_user = self.user_repository.create_user(user)
            user_ids.append(created_user.id)

        for title, credits, user_id in courses_data:
            course = Course(title, credits, user_id)
            created_course = self.course_repository.create_course(course, user_ids[courses_data.index((title, credits, user_id))])

        all_courses = self.course_repository.get_all_courses()
        self.assertEqual(len(all_courses), len(courses_data))
        for i, course_data in enumerate(courses_data):
            self.assertEqual(all_courses[i].title, course_data[0])
            self.assertEqual(all_courses[i].credits, course_data[1])
            self.assertEqual(all_courses[i].user, user_ids[i])

    def test_delete_course(self):
        created_user = self.user_repository.create_user(self.user)
        test_course = Course("Testi Kurssi", 3, created_user.id)
        self.course_repository.create_course(test_course, created_user.id)

        self.course_repository.delete_course(test_course)

        all_courses = self.course_repository.get_all_courses()
        self.assertNotIn(test_course, all_courses)
        