from tkinter import Tk, Listbox, Variable, Scrollbar, Frame
from tkinter.ttk import Label, Button, Notebook
from entities.competition import Competition
from ui.competitor_form import CompetitorFormFrame
from ui.timer import TimerFrame
from ui.exporting import ExportingFrame

class CompetitionFrame(Frame):
    def __init__(self, master, back_menu, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._back_menu = back_menu
        self._competition_id = None
        self._competition = None
        self.create_view()

    def set_competition(self, competition_id, competition):
        self._competition_id = competition_id
        self._competition = competition
        self.create_view()

    def create_view(self):
        if self._competition is None:
            return

        heading_label = Label(master=self, text=f"{self._competition.name} ({self._competition_id.upper()})")
        menu_button = Button(master=self, text="Menu", command=self._back_menu)

        tab_view = Notebook(master=self)
        competitor_form = CompetitorFormFrame(self, self._add_competitor)
        timer_frame = TimerFrame(self, self._competition)
        exporting_frame = ExportingFrame(self, self._competition)
        tab_view.add(competitor_form, text="Competitors")
        tab_view.add(timer_frame, text="Timer")
        tab_view.add(exporting_frame, text="Exporting")

        heading_label.grid(row=0, column=0)
        menu_button.grid(row=0, column=1)
        tab_view.grid(row=1, column=0, columnspan=2)

    def _add_competitor(self, competitor):
        if self._competition is not None:
            self._competition.add_competitor(competitor)
