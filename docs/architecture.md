# Architecture

## Structure

The project consists of three architecture layers: UI, logics and repositories.
Logics is divided into two smaller parts, services and entities, which are responsible for handling and storing data, respectively.
Repositories layer, on the other hand, stores the data permanently to the remote database via API.

The package diagram of the project is as follows:

![package diagram](./assets/package-diagram.svg)

## Logics

Services package contains modules that are all responsible for a single logical operation:

* [`exporting`](/src/services/exporting.py) takes in a competition and produces start and result lists as export-ready HTML strings.
* [`login`](/src/services/login.py) handles the login token: generates it from given credentials, saves it to a file and reads it from there later
* [`request`](/src/services/request.py) module contains a simple class making HTTP requests to the server
* [`timedelta-format`](/src/services/timedelta-format.py) consists of a single function that converts a timedelta instance into a readable string

Entities package consists of two classes that store data in a short term:

* [`competition`](/src/entities/competition.py) holds data about a single competition.
* [`competitor`](/src/entities/competitor.py) holds data about a single participant of a competition. One Competition class holds a list of Competitor instances.

### Login token

There is no real user accounts in the application.
Instead, it asks for a username and password, and then converts these into a unique _login token_ using SHA-256 hashing algorithm.
Each competition created is then associated with a token like this, after which everyone with the correct token (i.e. correct username-password pair) can edit the competition.

The string that is being hashed to generate the token consists of the username and password separated by a single `#` character.
Therefore the username must not contain this character,
or else there could be collisions with different username-password pairs:
for example pairs `user#name`-`password` and `user`-`name#password` would both lead to hash string of `user#name#password`.

## Storing competition data

All data is stored at the database, which is accessed via an API. [`CompetitionRepository`](../src/repositories/competition_repository.py) class is responsible for creating these requests and [`Request`](../src/services/request.py) class actually sends them.

A new competition is first created by sending POST request with JSON body to the API endpoint. Request body should contain one key: `token` holding the user's login token. When process is successful, 201 status is responded with JSON body. The object has exactly one key, `id`, which holds the new competition ID.

Updating competition data is done by sending PUT request with JSON body. The object should contain three keys: `id` holding the competition ID, `token` holding the user's login token, and `content` holding the dictionary representation of the competition. Expect status code 200 as a response.

Competition data can be read by sending GET request with JSON body containing two keys: `id` holding the competition ID and `token` holding the user's login token. Expect receiving response status 200 with JSON body holding the dictionary respresentation of the competition.

## Sequence diagrams

The following sequence diagram depicts the flow of managing a competition.

```mermaid
sequenceDiagram
  UI->>Competition: create competition
  Competition-->>UI: new competition instance
  UI->>Competitor: create competitor
  Competitor-->>UI: new competitor instance
  UI->>Competition: add competitor
  UI->>Competition: start timer
  note over Competition: datetime of start is being saved
  UI->>Competitor: finish now
  note over Competitor: datetime of finish is being saved
  UI->>Exporting: export results
  Exporting-->>UI: HTML string
  note over UI: user saves the HTML document
```

Competition data management is as follows.

```mermaid
sequenceDiagram
Note over App,API: Create a new competition
App->>API: POST {"token":"myusertoken"}
API->>App: Status 201 {"id":"competitionid"}
Note over App,API: Add/update competition data
loop After every change
  App->>API: PUT {"token":"myusertoken","id":"competitionid","content":{"name":"My competition", ... }}
  API->>App: Status 200
end
Note over App: Closes app and opens later
App->>API: GET {"id":"competitionid","token":"myusertoken"}
API->>App: 200 {"name":"My competition", ... }
```
