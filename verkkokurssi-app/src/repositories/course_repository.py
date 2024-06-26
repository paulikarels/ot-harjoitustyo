from entities.course import Course

class CourseRepository:
    """
    Luokka, joka vastaa Kurssien liittyvistä tietokanta toiminnoista.
    """
    def __init__(self, connection):
        """
        Luokan konstruktori.

        Args:
            connection: Tietokantayhteysobjekti, joka vastaa tietokantayhteydestä.

        """
        self._connection = connection

    def create_course(self, course, user_id):
        """
        Tallentaa luodun kurssin tietokantaan.

        Args:
            course: Tallennettava kurssi-olio.
            user_id: Käyttäjä olion id yhdistettävään kurssiin.

        Returns:
            Palauttaa tallennetun luodun Kurssin.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO courses (id, title, credits, userID) VALUES (?, ?, ?, ?)",
                       (course.id, course.title, course.credits, user_id))

        course.id = cursor.lastrowid

        self._connection.commit()
        return course

    def get_course_with_userid(self, user_id):
        """
        Etsii ja palauttaa kurssin, annetulla/tietyllä käyttäjä id:llä tietokannasta.

        Args:
            user_id: Käyttäjä olion ID.

        Returns:
            Lista kursseista joilla on annetun käyttäjä olion ID liittyviä kursseja.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM courses WHERE userID = ?", (user_id,))
        courses = cursor.fetchall()

        courses_with_created_at = []
        for row in courses:
            course = Course(row["id"], row["title"], row["credits"], row["userID"])
            course.created_at = row["created_at"]
            courses_with_created_at.append(course)

        return courses_with_created_at

    def get_course_with_title(self, course_title):
        """
        Etsii ja palauttaa kurssin, annetulla kurssi olio tittelillä.

        Args:
            course_title: Kurssi olion titteli.

        Returns:
            Lista kursseista joilla on annetun kurssi olion titteli.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM courses WHERE title = ?", (course_title,))
        courses = cursor.fetchall()

        return [Course(row["id"], row["title"], row["credits"], row["userID"])
                if row else None for row in courses]

    def get_all_courses(self):
        """
        Löytää ja palauttaa kaikki kurssit tietokannasta.

        Returns:
            Palauttaa listan kurssi olioita.

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()

        return [Course(row["id"], row["title"], row["credits"], row["userID"])
                if row else None for row in courses]

    def delete_course_with_course_id(self, course_id):
        """
        Poistaa kurssin tietokannasta kurssi IDn perusteella.

        Args:
            course_id: Kurssi ID poistettavaksi.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        self._connection.commit()

    def delete_all_courses(self):
        """
        Poistaa kaikki kurssit.

        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM courses")
        self._connection.commit()
