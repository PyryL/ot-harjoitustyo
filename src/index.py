from repositories.competition_repository import CompetitionRepository
from ui.ui import UI

if __name__ == "__main__":
    repository = CompetitionRepository()
    app = UI(repository)
    app.mainloop()
