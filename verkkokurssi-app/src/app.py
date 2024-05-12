from tkinter import Tk
from services.appservice import AppService

def main():
    window = Tk()
    window.title("Online course application")

    app = AppService(window)
    app.start()

    window.mainloop()

if __name__ == "__main__":
    main()
