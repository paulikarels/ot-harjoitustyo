from tkinter import Tk
from services.appservice import AppService
from databaselogic import database, initialize_database
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository
from repositories.exercise_repository import ExerciseRepository

def main():
    initialize_database.initialize_database()

    window = Tk()
    window.title("Online course application")

    user_repository = UserRepository(database.get_database_connection())
    course_repository = CourseRepository(database.get_database_connection())
    exercise_repository = ExerciseRepository(database.get_database_connection())

    app = AppService(window, user_repository, course_repository, exercise_repository)
    app.start()

    window.mainloop()

if __name__ == "__main__":
    main()
    