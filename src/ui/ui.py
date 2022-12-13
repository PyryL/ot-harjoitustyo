from tkinter import Tk, Listbox, Variable, Scrollbar, Frame
from tkinter.ttk import Label, Button
from entities.competition import Competition
from ui.login import LoginFrame
from ui.menu import MenuFrame
from ui.competition import CompetitionFrame

class UI(Tk):
    def __init__(self, competition_repository, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self._competition_repository = competition_repository
        self._competition_id = None

        self.geometry("400x200")
        self.resizable(width=False, height=False)

        self._container = Frame(self)
        self._container.grid(row=0, rowspan=10, column=0, columnspan=10)
        self._container.grid_rowconfigure(0, weight=1)
        self._container.grid_columnconfigure(0, weight=1)

        self._pages = {
            "login": LoginFrame(self._container, self._open_menu, width=400, height=200),
            "menu": MenuFrame(self._container, self._competition_repository, self._open_competition, width=400, height=200),
            "competition": CompetitionFrame(self._container, self._save_competition_changes, self._open_menu, width=400, height=200)
        }

        self._open_login()

    def _open_page(self, name):
        for page in self._pages.values():
            page.grid_forget()
        self._pages[name].grid(row=0, column=0, sticky="nsew")

    def _open_login(self):
        self.title("TimeKeeper - Login")
        self._open_page("login")
        self._pages["login"].check_if_already_logged_in()

    def _open_menu(self):
        self.title("TimeKeeper - Menu")
        self._competition_id = None
        self._open_page("menu")

    def _save_competition_changes(self, competition):
        if self._competition_id is not None:
            self._competition_repository.set_competition(self._competition_id, competition)

    def _open_competition(self, competition_id):
        competition = self._competition_repository.get_competition(competition_id)
        if competition is None:
            return
        self._competition_id = competition_id
        self.title(f"TimeKeeper - {competition.name}")
        self._pages["competition"].set_competition(competition_id, competition)
        self._open_page("competition")
