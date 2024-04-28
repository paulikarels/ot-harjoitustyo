from tkinter import Tk
from services.appservice import AppService
from databaselogic import database, initialize_database

def main():
    initialize_database.initialize_database()

    window = Tk()
    window.title("Online course application")

    app = AppService(window)
    app.start()

    window.mainloop()

if __name__ == "__main__":
    main()
    