from tkinter import ttk,  constants



class Login:
    def __init__(self, root, login, register):
        self._root = root
        self._login = login
        self._register = register
        self._frame = None


        self._initialize_moisture()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

        


    def _initialize_moisture(self):
        self._frame = ttk.Frame(master=self._root)

        
        username_label = ttk.Label(master=self._frame, text='Username')

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)
        
        password = ttk.Label(master=self._frame, text='Password')

        self._password_type = ttk.Entry(master=self._frame)

        password.grid(padx=5, pady=5, sticky=constants.W)
        self._password_type.grid(padx=5, pady=5, sticky=constants.EW)

        login_button = ttk.Button(master=self._frame, text='Login',command=self._login)

        register_button = ttk.Button(master=self._frame,text="Register",command=self._register)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)

        
