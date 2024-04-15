from tkinter import ttk, StringVar, constants
from services.app_service import app_service

class SignupView:
    def __init__(self, root, handle_signup, handle_show_login_view):
        self._root = root
        self._handle_signup = handle_signup
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_var = StringVar()
        self._password_var = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Sign Up")
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame, textvariable=self._username_var)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame, textvariable=self._password_var)

        signup_button = ttk.Button(
            master=self._frame,
            text="Sign Up",
            command=self._handle_signup
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Back to Login",
            command=self._handle_show_login_view
        )

        x=2
        y=2

        heading_label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=8, pady=8)
        username_label.grid(padx=x, pady=y)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        password_label.grid(padx=x, pady=y)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        signup_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=x, pady=y)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=x, pady=y)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _handle_signup(self):
        username = self._username_var.get()
        password = self._password_var.get()

        self._handle_signup(username, password)