from entities.exercise import Exercise

class ExerciseRepository:
    """
    Luokka, joka vastaa Tehtävien liittyvistä tietokanta toiminnoista.
    """
    def __init__(self, connection=None):
        """
        Luokan konstruktori.

        Args:
            connection: Tietokantayhteysobjekti, joka vastaa tietokantayhteydestä.

        """
        self._connection = connection

    def create(self, exercise):
        """
        Tallentaa luodun tehtävän tietokantaan.

        Args:
            exercise: Tallennettava tehtävä-olio.

        Returns:
            Palauttaa tallennetun luodun käyttäjän.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO exercises (id, description, done, courseID) VALUES (?, ?, ?, ?)",
                       (exercise.id, exercise.description, exercise.done, exercise.course))

        self._connection.commit()

        return exercise

    def get_all_exercises(self):
        """
        Löytää ja palauttaa kaikki tehtävät tietokannasta.

        Returns:
            Palauttaa listan tehtävä olioita.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM exercises")
        exercises = cursor.fetchall()

        return [Exercise(row["id"], row["description"], row["done"], row["courseID"])
                if row else None for row in exercises]

    def delete_all_exercises(self):
        """
        Poistaa kaikki tehtävät.

        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM exercises")
        self._connection.commit()

    def get_exercises_for_course(self, course):
        """
        Etsii ja palauttaa tehtävän, annetulla/tietyllä kurssista ja sen id:stä tietokannasta

        Args:
            course: Kurssin id.

        Returns:
            Lista tehtävistä joilla on  määrittely kurssiin liittyviä harjoituksista

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM exercises WHERE courseID = ?", (course,))
        exercises = cursor.fetchall()

        return [Exercise(row["id"], row["description"], row["done"], row["courseID"])
                for row in exercises]

    def mark_exercise_as_done(self, exercise_description):
        """
        Merkkaa tehtävä olion tehdyksi annetulla tehtävä olio ID:llä

        Args:
            exercise_id: Tehtävän ID, joka tullaan merkkaamaan tehdyksi.
        """
        cursor = self._connection.cursor()
        cursor.execute("UPDATE exercises SET done = ? WHERE description = ?", (True, exercise_description))
        self._connection.commit()