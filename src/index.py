from entities.competition import Competition
from entities.competitor import Competitor

class CLI:
    def __init__(self):
        self._init_competition()
        self._print_commands()
        self._main_loop()

    def _init_competition(self):
        print("CREATING NEW COMPETITION")
        print(" Give a name for the competition:")
        name = input(" > ")
        print()
        self._competiton = Competition(name, [], None)

    def _main_loop(self):
        while True:
            print("MAIN MENU")
            command = input(" > ")
            print()
            if command == "c":
                self._add_competitor()
            elif command == "s":
                self._start_timing()
            elif command == "f":
                self._add_finish_time()
            elif command == "d":
                self._print_debug_info()
            elif command == "h":
                self._print_commands()
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

    def _start_timing(self):
        print("START TIMING")
        print(" When competition starts, press enter")
        input(" > ")
        self._competiton.start_now()
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

if __name__ == "__main__":
    CLI()
