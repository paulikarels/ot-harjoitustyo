from tkinter import ttk, StringVar, constants
from services.app_service import app_service

class LoginView:
    def __init__(self, root, handle_login, handle_show_sign_up_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_sign_up_view = handle_show_sign_up_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Log in")
        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Log in",
            command=self._handle_login
        )

        signup_button = ttk.Button(
            master=self._frame,
            text="Create User",
            command=self._handle_show_sign_up_view
        )

        x=2
        y=2

        heading_label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=8, pady=8)
        username_label.grid(padx=x, pady=y)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        password_label.grid(padx=x, pady=y)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=x, pady=y)
        login_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=x, pady=y)
        signup_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=x, pady=y)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _handle_create_user_button_click(self):
        username = self._username_var.get()
        password = self._password_var.get()

        self._handle_show_sign_up_view(username, password)

    def _handle_login_button_click(self):
        username = self._username_var.get()
        password = self._password_var.get()

        self._handle_login(username, password)