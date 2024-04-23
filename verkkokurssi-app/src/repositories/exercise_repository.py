from entities.exercise import Exercise

class ExerciseRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def create(self, exercise):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO exercises (description, done, courseID) VALUES (?, ?, ?)",
            (exercise.description, exercise.done, exercise.course))

        self._connection.commit()

        return exercise

    def get_all_exercises(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM exercises")
        exercises = cursor.fetchall()

        return ([Exercise(row["id"], row["description"], row["done"], row["courseID"])
            if row else None for row in exercises])

    def delete_all_exercises(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM exercises")
        self._connection.commit()

    def get_exercises_for_course(self, course):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM exercises WHERE courseID = ?", (course,))
        exercises = cursor.fetchall()

        return ([Exercise(row["id"], row["description"], row["done"], row["courseID"])
            for row in exercises])
