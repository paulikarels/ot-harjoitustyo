from tkinter import Tk
from ui.ui import UI
from databaselogic import database, initialize_database
from repositories.user_repository import UserRepository
from repositories.course_repository import CourseRepository

def main():
    
    initialize_database.initialize_database()

    window = Tk()
    window.title("Online course application")

    user_repository = UserRepository(database.get_database_connection())
    course_repository = CourseRepository(database.get_database_connection())

    ui_view = UI(window, user_repository, course_repository)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()