from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.sign_up_view import SignupView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_handle_sign_up_view
        )

        self._current_view.pack()

    def _show_handle_sign_up_view(self):
        self._hide_current_view()

        self._current_view = SignupView(
            self._root,
            self._handle_signup,
            self._show_login_view
        )

        self._current_view.pack()

        pass

    def _handle_login(self, username, password):
        pass

    def _handle_signup(self, username, password):
        pass