from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, StringVar, messagebox
from tkinter.ttk import Label, Button, Notebook, Entry

class TimerFrame(Frame):
    def __init__(self, master, competition, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._competition = competition
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

    def _update_view(self):
        if self._competition.start_time is None:
            self._time_label.grid_forget()
            self._finisher_bib_label.grid_forget()
            self._finisher_bib_entry.grid_forget()
            self._finisher_button.grid_forget()

            self._not_started_label.grid(row=0, column=0)
            self._start_button.grid(row=1, column=0)

        else:
            self._not_started_label.grid_forget()
            self._start_button.grid_forget()

            self._time_label.grid(row=0, column=0, columnspan=2)
            self._finisher_bib_label.grid(row=1, column=0)
            self._finisher_bib_entry.grid(row=1, column=1)
            self._finisher_button.grid(row=2, column=0, columnspan=2)

    def _start_timer(self):
        if self._competition.start_time is None:
            self._competition.start_now()
            self._update_view()

    def _competitor_finish(self):
        try:
            bib = int(self._finisher_bib_var.get())
        except:
            bib = None

        matching_competitors = [c for c in self._competition.competitors if c.bib == bib]
        if len(matching_competitors) != 1:
            messagebox.showwarning("Invalid bib", "The bib does not exist")
            return

        competitor = matching_competitors[0]
        if competitor.finish_time is not None:
            messagebox.showwarning(
                "Competitor already finished",
                f"This competitor already finished at {competitor.finish_time}"
            )
            return

        competitor.finish_now()
        messagebox.showinfo("Finished competitor", f"{competitor.name}, {competitor.club}")
        self._finisher_bib_var.set("")
