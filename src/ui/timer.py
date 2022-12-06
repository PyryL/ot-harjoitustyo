from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, StringVar, messagebox
from tkinter.ttk import Label, Button, Notebook, Entry
from entities.competitor import SpecialResult

class TimerFrame(Frame):
    def __init__(self, master, competition, save_changes, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._competition = competition
        self._save_changes = save_changes
        self.create_view()
        self._update_view()

    def create_view(self):
        self._not_started_label = Label(self, text="Timer not started")
        self._start_button = Button(self, text="Start", command=self._start_timer)
        self._time_label = Label(self, text="Timer is running")
        self._finisher_bib_label = Label(self, text="Finisher's bib: ")
        self._finisher_bib_var = StringVar()
        self._finisher_bib_entry = Entry(self, textvariable=self._finisher_bib_var, width=10)
        self._finisher_button = Button(self, text="Finish", command=self._competitor_finish)
        self._dnf_button = Button(self, text="DNF", command=self._competitor_dnf)
        self._dns_button = Button(self, text="DNS", command=self._competitor_dns)
        self._dq_button = Button(self, text="DQ", command=self._competitor_dq)

    def _update_view(self):
        if self._competition.start_time is None:
            self._time_label.grid_forget()
            self._finisher_bib_label.grid_forget()
            self._finisher_bib_entry.grid_forget()
            self._finisher_button.grid_forget()
            self._dnf_button.grid_forget()
            self._dns_button.grid_forget()
            self._dq_button.grid_forget()

            self._not_started_label.grid(row=0, column=0)
            self._start_button.grid(row=1, column=0)

        else:
            self._not_started_label.grid_forget()
            self._start_button.grid_forget()

            self._time_label.grid(row=0, column=0, columnspan=3)
            self._finisher_bib_label.grid(row=1, column=0)
            self._finisher_bib_entry.grid(row=1, column=1, columnspan=2)
            self._finisher_button.grid(row=2, column=0, columnspan=3)
            self._dnf_button.grid(row=3, column=0)
            self._dns_button.grid(row=3, column=1)
            self._dq_button.grid(row=3, column=2)

    def _start_timer(self):
        if self._competition.start_time is None:
            self._competition.start_now()
            self._save_changes()
            self._update_view()

    def _get_competitor_from_bib(self):
        try:
            bib = int(self._finisher_bib_var.get())
        except:
            bib = None

        matching_competitors = [c for c in self._competition.competitors if c.bib == bib]
        if len(matching_competitors) != 1:
            messagebox.showwarning("Invalid bib", "The bib does not exist")
            return None

        competitor = matching_competitors[0]
        if competitor.has_finished:
            messagebox.showwarning(
                "Competitor already finished",
                f"This competitor already finished {competitor.finish}"
            )
            return None
        
        self._finisher_bib_var.set("")
        return competitor

    def _competitor_finish(self):
        competitor = self._get_competitor_from_bib()
        if competitor is None:
            return
        competitor.finish_now()
        self._save_changes()
        messagebox.showinfo("Finished competitor", f"{competitor.name}, {competitor.club}")

    def _competitor_dnf(self):
        competitor = self._get_competitor_from_bib()
        if competitor is None:
            return
        competitor.special_result(SpecialResult.did_not_finish)
        self._save_changes()
        messagebox.showinfo("Did not finish", f"{competitor.name}, {competitor.club}")

    def _competitor_dns(self):
        competitor = self._get_competitor_from_bib()
        if competitor is None:
            return
        competitor.special_result(SpecialResult.did_not_start)
        self._save_changes()
        messagebox.showinfo("Did not start", f"{competitor.name}, {competitor.club}")

    def _competitor_dq(self):
        competitor = self._get_competitor_from_bib()
        if competitor is None:
            return
        competitor.special_result(SpecialResult.disqualified)
        self._save_changes()
        messagebox.showinfo("Disqualified", f"{competitor.name}, {competitor.club}")
