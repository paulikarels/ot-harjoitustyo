from entities.exercise import Exercise
from repositories.course_repository import course_repository
from database import get_database_connection

class ExerciseRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, exercise):
        cursor = self._connection.cursor()
        cursor.execute("insert into exercises (description, done, course) values (?, ?)", (exercise.description, exercise.done, exercise.course))

        self._connection.commit()

        return exercise

    def get_all_exercises(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from exercises")
        exercises = cursor.fetchall()

        return [Exercise(row["description"], row["done"], row["course"]) if row else None for row in exercise]

    def delete_all_exercises(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from exercises")
        self._connection.commit()


exercise_repository = ExerciseRepository(get_database_connection())
