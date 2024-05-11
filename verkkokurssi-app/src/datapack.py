
from datetime import datetime, timedelta
import random
from databaselogic.database import get_database_connection

if __name__ == "__main__":
    cursor = get_database_connection().cursor()

    cursor.execute('''INSERT INTO users (id, admin, username, password)
                    values (1, true, 't', 't')''')

    # Tästä alaspäin oleva koodi on Generoitu CHATGPT HYÖDYNTÄEN
    # Tässä luodaan useampi kurssi ja tehtävä tietokantaan,
    # luodakseen jokin malli plotly.graph_objs Taulua varten
    for i in range(1, 11):
        course_title = f"Course_{i}"
        credits_amount = i
        created_at = datetime(2024, 11, 2, 10+i, 30, 15)
        cursor.execute('''INSERT INTO courses
                      (id, userID, title, credits, created_at)
                      VALUES (?, ?, ?, ?, ?)''',
                      (i, 1, course_title, credits_amount, created_at))

    for i in range(1, 11):
        cursor.execute("SELECT created_at FROM courses WHERE id = ?", (i,))
        course_created_at_str = cursor.fetchone()["created_at"]
        course_created_at = datetime.strptime(course_created_at_str, "%Y-%m-%d %H:%M:%S")

        for j in range(1, 11):
            exercise_description = f"Course_{i}_Exercise_{j}"
            done = j % 2 == 0

            marked_done_at = course_created_at + timedelta(hours=random.randint(0, 23))

            for _ in range(j):
                marked_done_at += timedelta(hours=1)
                marked_done_at += timedelta(minutes=random.randint(0, 59))

                if marked_done_at < course_created_at:
                    marked_done_at = course_created_at + timedelta(minutes=random.randint(1, 59))

            cursor.execute('''INSERT INTO exercises
                           (courseID, description, done, marked_done_at)
                           VALUES (?, ?, ?, ?)''',
                            (i, exercise_description, done, marked_done_at))

    get_database_connection().commit()
