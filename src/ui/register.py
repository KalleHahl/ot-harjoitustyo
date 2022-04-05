
from tkinter import ttk, constants
from app.app import App



class Register:
    def __init__(self, root, register, login=None):
        self._root = root
        self._register = register
        self._login = login
        self._frame = None
        self._username_txt = None
        self._password_txt = None

        self._initialize_moisture()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _register_user(self):
        username = self._username_txt.get()
        password = self._password_txt.get()

        App.register_user(username, password)
        print("kiitos")


        

    def _initialize_moisture(self):
        self._frame = ttk.Frame(master=self._root)


        username_label = ttk.Label(master=self._frame, text='Username')

        self._username_txt = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_txt.grid(padx=5, pady=5, sticky=constants.EW)

        password_label = ttk.Label(master=self._frame, text='Password')

        self._password_txt = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_txt.grid(padx=5, pady=5, sticky=constants.EW)

        register_user_button = ttk.Button(master=self._frame,text='Register',command=self._register_user())

        login_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._login
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        register_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)