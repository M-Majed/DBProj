# DBProj

A desktop music-platform database application built with **Python**, **PyQt5**, and **SQLite**. The project demonstrates a relational database-backed application with user accounts, music discovery, social interactions, artist tools, playlists, subscriptions, wallets, concerts, and ticket management.

> This is an educational project and is not intended for production use.

## Features

### User accounts

- Sign up and log in
- Maintain the current user session across application windows
- Switch between regular-user and artist modes
- Enable or disable a subscription
- Deposit funds into an in-app wallet

### Music discovery

- Browse tracks, albums, artists, concerts, public playlists, followed users, suggestions, and liked tracks
- View track information including title, artist, genre, age category, region, and lyrics
- Search tracks using fields such as title, artist, genre, age category, and region
- Receive genre-based track suggestions from previously liked music

### Likes, comments, and playlists

- Like and unlike tracks
- View and submit track comments
- Create playlists by adding tracks
- Set playlists as public or private
- Like albums and playlists

Some interactions, including liking and commenting, are restricted to subscribed users.

### Social features

- Follow and unfollow users
- View followers and followed users
- Send, accept, or reject friend requests
- Remove friends
- Exchange messages with friends

### Artist tools

Users marked as artists can:

- Add and remove music
- Organize tracks into albums
- Add and remove concerts
- Manage their music, album, and concert lists

### Concerts and tickets

- Browse available concerts
- Purchase tickets using the in-app wallet
- Prevent duplicate ticket purchases
- View active and expired tickets
- Cancel tickets and receive refunds
- Automatically mark tickets as expired according to concert dates

## Technology stack

| Component | Technology |
| --- | --- |
| Language | Python 3 |
| Desktop interface | PyQt5 |
| Database | SQLite |
| UI design files | Qt Designer `.ui` files |
| Data access | Python `sqlite3` through `DBManagement.py` |

## Database model

The application uses a relational SQLite database stored in `my.db`. Its main entities include:

- `user`
- `tracks`
- `albums`
- `concert`
- `ticket`
- `playlist`
- `playlist_music`
- `likes`
- `comment`
- `followorfollowing`
- `friend`
- `friend_request`
- `message`
- `suggestion`
- `like_album`
- `like_playlist`

Database connection handling is implemented in `DBManagement.py`, while schema operations and application queries are centralized in `dbfunctions.py`.

## Getting started

### Prerequisites

- Python 3.8 or newer
- `pip`

SQLite is included with standard Python installations.

### Installation

```bash
git clone https://github.com/M-Majed/DBProj.git
cd DBProj

python -m venv .venv
```

Activate the virtual environment:

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the GUI dependency:

```bash
python -m pip install PyQt5
```

### Run the application

Run the program from the repository root so it can locate `my.db` and the local resource modules:

```bash
python login_signup.py
```

The application opens on the login/sign-up screen.

## Project structure

```text
DBProj/
├── login_signup.py          # Main application entry point
├── login.py                 # Login interface and authentication flow
├── Signup.py                # User registration
├── MusicList.py             # Main browsing interface
├── Music.py                 # Track details, likes, comments, and playlists
├── Search.py                # Track search form
├── SearchResult.py          # Search and category results
├── Account.py               # Account, wallet, subscription, and artist controls
├── ArtistMusic_Concert.py   # Artist music and concert management
├── AddMusic.py              # Add-track interface
├── AddConcert.py            # Add-concert interface
├── albums.py                # Album management
├── playlist.py              # Playlist management
├── Friends.py               # Friendship and messaging features
├── Follow.py                # Follow/follower management
├── Ticket.py                # Active and expired tickets
├── Comments.py              # Track comments
├── DBManagement.py          # SQLite connection and query execution
├── dbfunctions.py           # Schema definitions and application queries
├── my.db                    # Bundled SQLite database
├── Resources/               # Icons, backgrounds, and Qt resources
├── pdf/DB_Project.pdf       # Original project specification
└── *.ui                     # Qt Designer interface files
```

## Project specification

The original assignment and project requirements are available in [`pdf/DB_Project.pdf`](pdf/DB_Project.pdf).

## Important notes

- The project currently stores passwords as plain text and constructs many SQL statements using string interpolation. It should only be used as a learning prototype.
- For a production implementation, use password hashing, parameterized SQL queries, input validation, database migrations, automated tests, and proper error handling.
- The repository includes both Qt Designer `.ui` files and Python versions of those interfaces.

## License

No license has been added to this repository. All rights are reserved by the repository owner unless a license is added later.
