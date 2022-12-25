# Requirement specification

## Purpose
The application allows organizers of a running competition to prepare and execute successful timekeeping.
It is supposed to cover all needed actions of hosting such an event, from competitor enrollment all the way to 
generating publish-ready result sheets.

## Users

There's only one user role in the app: the organizer. They is able to create competitions, manage competitors, add results and export data. Multiple competitions of a single user should be able to be carried out simultaneously. Only the user who created the competition can view and edit it.

## Functionality

### Accounts

Before signin in, user is able to create an account by giving some basic information (choose username, password, etc). **DONE**

If the user has already an account but they is not logged in (e.g. used application earlier and re-installed it), they is able to sign in using old credentials and has then access to all old competitions. **DONE**

### Selecting competition

As stated before, one user can be associated with multiple competitions. Therefore, after logging in to the account, user can open a competition by inserting its ID. **DONE**

User can also create new competitions. **DONE**

### Managing competition

After selecting a competition, user is able to perform the following actions with it:

* **Add a new competitor.** This is done by giving some information about the runner (e.g. bib number, name, club). **DONE**
* **Start the timer.** When the competition begins, user must start the clock. **DONE**
* **Add finish time.** For each competitor, the time of crossing the finish line must be determined. **DONE**
* **Special actions.** Instead of finish time, competitor can also be marked with *DNS* (did not start), *DNF* (did not finish) or *DQ* (disqualified). **DONE**
* **Exporting start lists.** Start list can be exported to an HTML file, that can then be published by the competition organizer (the publication process is out of this project's scope). **DONE**
* **Exporting results.** The same way as start list, competition results can also be exported. **DONE**

## Further ideas

* Setting competitor's *PB* (personal best) and *SB* (season best) before competition. Add a PB/SB mark to the exported result sheet if the result was better than that.
* Series based on competitor's age and gender.
* Possibility for the organizer to save split times.
* Multiple users could manage the same competition.
* Account settings, including changing username and password, as well as removing the entire account.
