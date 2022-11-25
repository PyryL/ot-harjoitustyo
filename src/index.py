import sys
from entities.competition import Competition
from entities.competitor import Competitor
from repositories.competition_repository import CompetitionRepository
from services.exporting import Exporting

class CLI:
    def __init__(self):
        self._competition_repository = CompetitionRepository()
        self._competition_id = None
        self._competiton = None
        self._init_competition()
        self._print_commands()
        self._main_loop()

    def _init_competition(self):
        print("CREATING NEW COMPETITION")
        print(" Give the ID of the competition or empty to create new:")
        self._competition_id = input(" > ")
        if self._competition_id == "":
            self._create_new_competition()
        else:
            self._competiton = self._competition_repository.get_competition(self._competition_id)
            if self._competiton is None:
                print(" Competition not found")
                sys.exit(1)
        print()

    def _create_new_competition(self):
        print(" Give a name for the new competiton:")
        competition_name = input(" > ")
        self._competition_id = self._competition_repository.generate_new_id()
        self._competiton = Competition(competition_name, [], None)
        self._save_changes()
        print(f" The ID of the new competition is {self._competition_id}")

    def _save_changes(self):
        self._competition_repository.set_competition(self._competition_id, self._competiton)

    def _main_loop(self):
        commands = {
            "c": self._add_competitor,
            "s": self._start_timing,
            "f": self._add_finish_time,
            "e": self._export_to_html,
            "d": self._print_debug_info,
            "h": self._print_commands
        }
        while True:
            print("MAIN MENU")
            command = input(" > ")
            print()
            if command in commands:
                commands[command]()
            elif command == "x":
                break
            else:
                print(" Unknown command, try again.")
                print()

    def _print_commands(self):
        print("COMMAND LIST")
        print(" c Add new competitor")
        print(" s Start timing")
        print(" f Add finish times")
        print(" e Export to HTML")
        print(" d Debug")
        print(" h Print help")
        print(" x Exit application")
        print()

    def _add_competitor(self):
        print("ADDING COMPETITOR")
        print(" Name:")
        name = input(" > ")
        print(" Bib number:")
        bib = int(input(" > "))
        print(" Club:")
        club = input(" > ")
        print()
        competitor = Competitor(name, bib, club, None)
        self._competiton.add_competitor(competitor)
        self._save_changes()

    def _start_timing(self):
        print("START TIMING")
        print(" When competition starts, press enter")
        input(" > ")
        self._competiton.start_now()
        self._save_changes()
        print(" Time is now running")
        print()

    def _add_finish_time(self):
        print("FINISH TIME")
        print(" Write the competitor's bib number below.")
        print(" When they cross the finish line, press enter.")
        bib = int(input(" > "))
        for competitor in self._competiton.competitors:
            if competitor.bib == bib:
                competitor.finish_now()
                self._save_changes()
                print(f" Finished competitor: {competitor.name}, {competitor.club}")
                print()
                return
        print(" Invalid bib number, please try again")
        print()

    def _print_debug_info(self):
        print("DEBUG INFORMATION")
        print(" Competition:")
        print(f"  {self._competiton}")
        print(" Competitors:")
        for competitor in self._competiton.competitors:
            print(f"  {competitor}")
        print()

    def _export_to_html(self):
        print(" Select [s]tartlist or [r]esults")
        export_type = input(" > ")
        if export_type not in ["s", "r"]:
            print(" Invalid selection")
            print()
            return

        if export_type == "s":
            html_string = Exporting(self._competiton).start_list_html()
            filename = f"competitions/{self._competition_id}_startlist.html"
        elif export_type == "r":
            html_string = Exporting(self._competiton).results_list_html()
            filename = f"competitions/{self._competition_id}_results.html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_string)
        print(f" File {filename} saved")
        print()

if __name__ == "__main__":
    CLI()
