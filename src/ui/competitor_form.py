import re
from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, StringVar, messagebox
from tkinter.ttk import Label, Button, Notebook, Entry
from entities.competitor import Competitor

class CompetitorFormFrame(Frame):
    def __init__(self, master, add_competitor, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._add_competitor = add_competitor
        self.create_view()

    def create_view(self):
        name_label = Label(self, text="Name: ")
        self._name_var = StringVar()
        name_input = Entry(self, textvariable=self._name_var)

        bib_label = Label(self, text="Bib: ")
        self._bib_var = StringVar()
        bib_input = Entry(self, textvariable=self._bib_var)

        club_label = Label(self, text="Club: ")
        self._club_var = StringVar()
        club_input = Entry(self, textvariable=self._club_var)

        add_button = Button(self, text="Add", command=self._submit_form)

        name_label.grid(row=0, column=0)
        name_input.grid(row=0, column=1)
        bib_label.grid(row=1, column=0)
        bib_input.grid(row=1, column=1)
        club_label.grid(row=2, column=0)
        club_input.grid(row=2, column=1)
        add_button.grid(row=3, column=0, columnspan=2)

    def _submit_form(self):
        name = self._name_var.get()
        bib = self._bib_var.get()
        club = self._club_var.get()

        invalid_inputs = []
        if not re.match("\\S+", name):
            invalid_inputs.append("name")
        if not re.match("^\\d+$", bib):
            invalid_inputs.append("bib")
        if len(invalid_inputs) > 0:
            messagebox.showerror("Invalid entry", "Please check " + " and ".join(invalid_inputs))
            return

        competitor = Competitor(name, int(bib), club, None)
        self._add_competitor(competitor)

        self._name_var.set("")
        self._bib_var.set("")
        self._club_var.set("")
