import os
from tkinter import Tk, Listbox, Variable, Scrollbar, Frame, messagebox
from tkinter.ttk import Label, Button, Notebook
from tkinter.filedialog import asksaveasfilename
from services.exporting import Exporting

class ExportingFrame(Frame):
    def __init__(self, master, competition, cnf={}, **kw):
        super().__init__(master=master, cnf={}, **kw)
        self._competition = competition
        self.create_view()

    def create_view(self):
        start_list_button = Button(self, text="Export start list", command=self._export_start_list)
        results_button = Button(self, text="Export results", command=self._export_results)

        start_list_button.grid(row=0, column=0)
        results_button.grid(row=1, column=0)

    def _export_string(self, string):
        file_types = (("HTML files", "*.html"), ("All files", "*.*"))
        path = asksaveasfilename(defaultextension=".html", filetypes=file_types)
        try:
            with open(path, "w") as file:
                file.write(string)
        except:
            messagebox.showerror("File saving failed", "Could not save the file")
            return
        open_file_now = messagebox.askyesno(
            "File saved",
            f"File is successfully saved to {path}. Would you like to open it now?"
        )
        if open_file_now:
            os.system(f"open \"{path}\"")

    def _export_start_list(self):
        html_string = Exporting(self._competition).start_list_html()
        self._export_string(html_string)

    def _export_results(self):
        html_string = Exporting(self._competition).results_list_html()
        self._export_string(html_string)
