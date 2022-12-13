import re
from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, StringVar, messagebox
from tkinter.ttk import Label, Button, Entry
from tkinter.font import Font
from entities.competition import Competition
from services.login import Login

class MenuFrame(Frame):
    def __init__(self, master, competition_repository, open_competition, open_login, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._competition_repository = competition_repository
        self._open_competition = open_competition
        self._open_login = open_login
        self._login = Login()
        self.create_view()

    def create_view(self):
        bold_font = Font(weight='bold')

        logout_button = Button(self, text="Log out", command=self._log_out)

        open_existing_label = Label(self, text="Open existing competition", font=bold_font)
        competition_id_label = Label(self, text="Competition ID: ")
        self._competition_id_var = StringVar()
        self._competition_id_var.trace_add("write", self._make_competition_id_uppercase)
        competition_id_entry = Entry(self, textvariable=self._competition_id_var)
        open_button = Button(self, text="Open", command=self._open_competition_by_id)

        create_new_label = Label(self, text="Create new competition", font=bold_font)
        new_name_label = Label(self, text="Name: ")
        self._new_name_var = StringVar()
        new_name_entry = Entry(self, textvariable=self._new_name_var)
        create_new_button = Button(self, text="Create new", command=self._create_new_competition)

        logout_button.grid(row=0, column=2)
        open_existing_label.grid(row=1, column=0, columnspan=2)
        competition_id_label.grid(row=2, column=0)
        competition_id_entry.grid(row=2, column=1)
        open_button.grid(row=3, column=0, columnspan=2)
        create_new_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        new_name_label.grid(row=5, column=0)
        new_name_entry.grid(row=5, column=1)
        create_new_button.grid(row=6, column=0, columnspan=2)

    def _log_out(self, *args):
        self._login.log_out()
        self._open_login()

    def _make_competition_id_uppercase(self, *args):
        self._competition_id_var.set(self._competition_id_var.get().upper())

    def _create_new_competition(self):
        name = self._new_name_var.get()
        if not re.match("\\S+", name):
            messagebox.showerror("Invalid name", "Competition name must not be empty")
            return

        competition_id = self._competition_repository.generate_new_id()
        competition = Competition(name, [], None)
        self._competition_repository.set_competition(competition_id, competition)
        self._open_competition(competition_id)

    def _open_competition_by_id(self):
        competition_id = self._competition_id_var.get()
        competition = self._competition_repository.get_competition(competition_id)
        if competition is None:
            messagebox.showerror("Invalid ID", "Competition ID does not exist")
            return
        self._competition_id_var.set("")
        self._open_competition(competition_id)
