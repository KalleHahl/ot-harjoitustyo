from tkinter import Tk
from ui.register import Register
from ui.login import Login

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_todos_view(self):
        pass

    def _login_view(self):
        self._hide_current_view()

        self._current_view = Login(self._root, self._show_todos_view, self._register_view)

        self._current_view.pack()



    def _register_view(self):
        self._hide_current_view()

        self._current_view = Register(self._root,self._show_todos_view,self._login_view)
        self._current_view.pack()



