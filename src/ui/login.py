from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, StringVar, messagebox
from tkinter.ttk import Label, Button, Entry
from tkinter.font import Font
from services.login import Login

class LoginFrame(Frame):
    def __init__(self, master, open_menu, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._open_menu = open_menu
        self._login = Login()
        self.create_view()

    def create_view(self):
        title = Label(self, text="Create account or log in")

        username_label = Label(self, text="Username: ")
        self._username_var = StringVar()
        username_entry = Entry(self, textvariable=self._username_var)

        password_label = Label(self, text="Password: ")
        self._password_var = StringVar()
        password_entry = Entry(self, textvariable=self._password_var, show="*")

        submit_button = Button(self, text="Let's go", command=self._submit_form)

        title.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        submit_button.grid(row=3, column=0, columnspan=2)

    def check_if_already_logged_in(self):
        # if user is already logged in when opening app, go directly to menu
        if self._login.get_token() is not None:
            self._open_menu()

    def _submit_form(self, *args):
        username = self._username_var.get()
        password = self._password_var.get()
        if len(username) == 0:
            messagebox.showerror("Invalid credentials", "Username must not be empty")
            return
        if len(password) == 0:
            messagebox.showerror("Invalid credentials", "Password must not be empty")
            return
        if "#" in username:
            messagebox.showerror("Invalid credentials", "Username must not contain # character")
            return
        success = self._login.log_in(username, password)
        if not success:
            return
        self._open_menu()
