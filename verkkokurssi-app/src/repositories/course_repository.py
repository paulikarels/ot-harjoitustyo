from entities.course import Course
from repositories.user_repository import user_repository
from database import get_database_connection

class CourseRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_course(self, course):
        cursor = self._connection.cursor()
        cursor.execute("insert into courses (title, credits, user) values (?, ?, ?)", (course.title, course.credits, course.user))

        self._connection.commit()

        return course

    def get_all_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from courses")
        courses = cursor.fetchall()

        return [Course(row["title"],row["credits"], row["user"]) if row else None for row in courses]

    def delete_all_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from courses")
        self._connection.commit()

course_repository = CourseRepository(get_database_connection())
