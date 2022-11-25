# Requirement specification

## Purpose
The application allows organisers of a running competition to prepare and execute successful timekeeping.
It is supposed to cover all needed actions of hosting such an event, from competitor enrollment all the way to 
generating publish-ready result sheets.

## Users
Two user rolas are needed: administrator and basic.
Basic should have permission to add competitors, manage results and export data.
Additionally, admin should be able to create and delete competitions, and manage basic users' accounts.

Multiple users, at least one of which is admin, should be able to edit the same competition at the same time.
On the other hand multiple competitions should be able to be carried out simultaneously.

## Functionality
### Accounts
Before signin in, user is able to create an account by giving some basic information (choose username, password, etc).

If user wants to become admin, one must also give in a six-digit code from the server organizator.
This way the server host can, for example, sell the right of use for the server.

### Selecting competition
As stated before, one user can be associated with multiple competitions. Therefore, after logging in to the account, user can select the competition from a list.

User can also see their account ID, which can then be used by an admin user to grant a permission to manage a competition.

Admin users can also create new competitions.

### Managing competition
After selecting a competition, user is able to perform the following actions with it:

* **Manage staff.** Admin users can add and remove users to the competition.
* **Add a new competitor.** This is done by giving some information about the runner (e.g. bib number, name, club). **DONE**
* **Start the timer.** When the competition begins, someone must start the clock. **DONE**
* **Add finish time.** For each competitor, the time of crossing the finish line must be determined. **DONE**
* **Special actions.** Instead of finish time, competitor can also be marked with *DNS* (did not start), *DNF* (did not finish) or *DQ* (disqualified).
* **Exporting results.** Results can be exported to an HTML file, that can then be published by the competition organizer. The publication process is out of this project's scope. **DONE**

## Further ideas

* Exporting starting lists. **DONE**
* Setting competitor's *PB* (personal best) and *SB* (season best) before competition. Add a PB/SB mark to the exported result sheet if the result was better than that.
* Series based on competitor's age and gender.
* Possibility for the organizer to save split times.
* Account settings, including changing username and password, as well as removing the entire account.