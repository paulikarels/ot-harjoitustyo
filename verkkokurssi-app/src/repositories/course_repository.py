from entities.course import Course

class CourseRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def create_course(self, course):
        from entities.user import User
        
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO courses (title, credits, user) VALUES (?, ?, ?)", (course.title, course.credits, course.user))
        self._connection.commit()

        return course

    def get_all_courses(self):
        from entities.user import User
        
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()

        return [Course(row["title"], row["credits"], row["user"]) if row else None for row in courses]

    def delete_all_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM courses")
        self._connection.commit()