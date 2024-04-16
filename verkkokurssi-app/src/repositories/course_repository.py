from entities.course import Course

class CourseRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def create_course(self, course, user_id):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO courses (title, credits, userID) VALUES (?, ?, ?)",
            (course.title, course.credits, user_id))

        course.id = cursor.lastrowid

        self._connection.commit()
        return course

    def get_all_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()

        return ([Course(row["title"], row["credits"],
            row["userID"]) if row else None for row in courses])

    def delete_course(self, course):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM courses WHERE courses.title = ?", (course.title,))
        self._connection.commit()

    def delete_all_courses(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM courses")
        self._connection.commit()
