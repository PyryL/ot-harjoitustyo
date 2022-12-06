from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, constants
from tkinter.ttk import Label, Button
from entities.competition import Competition

class MenuFrame(Frame):
    def __init__(self, master, open_competition, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._open_competition = open_competition
        self._competitions = [
            Competition("Yksi kisa", [], None),
            Competition("Kaksi kisa", [1,2,3], None),
            Competition("Kolme kisa", [5,2], None)
        ]
        self.create_view()

    def create_view(self):
        account_id_label = Label(master=self, text=f"Account ID: {'ABC123'}")

        competitions_var = Variable(value=[c.name for c in self._competitions])
        self.competition_list = Listbox(master=self, listvariable=competitions_var)

        account_id_label.grid(row=0, column=0, columnspan=10)
        self.competition_list.grid(row=1, rowspan=9, column=0, columnspan=10)

        self.competition_list.bind('<Double-1>', self._competition_clicked)

    def _competition_clicked(self, event):
        competition_name = self.competition_list.selection_get()
        competition = [c for c in self._competitions if c.name == competition_name][0]
        self._open_competition(competition)
