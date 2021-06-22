# RoboCollab
**Note:** Most of this projects core features have not yet been implemented. It is unfinished.

## New Features
**Current Version:** `Rewrite 1.1`

**Bot Version:** `V7 1.0.0`

**Python Version:** `3.8.9`

- Added some things
## Credits

### Developers

This project was developed by [ZeroIntensity](https://zintensity.net) and [Brittank88](https://twitter.com/_brittank88).

Special thanks to [nekitdev](https://github.com/nekitdev) for helping me with [gd.py](https://pypi.org/project/gd.py/).


### Dependencies
- [discord.py](https://pypi.org/project/discord.py/)
- [gd.py](https://pypi.org/project/gd.py/)
- [requests](https://pypi.org/project/requests/)
- [bs4](https://pypi.org/project/bs4/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [flask-discord](https://pypi.org/project/flask-discord/)
- [gevent](https://pypi.org/project/gevent/)

## Installation

**Note:** `Python 3.8.9` is recommended for using RoboCollab. Python must also be installed to `PATH` for dependencies to be installed via the `install.py`. **Python 3.9 will not work**.

**Note: #2** Installation is currently only supported for the `bot` folder, as the web server is not ready.

**Note #3:** The `install.py` is also only supported for Windows. **It does not work with macOS or Linux**.


The `bot` folder has a hidden folder called `private`. This folder is where the RoboCollab `database`, `users.json`, `prefixes.json`, `env.py`, and a `.env`. In the `bot` folder, there is a file called "`install.py`". Run this file in your `bot` directory after downloading via command prompt with `python <path to install.py>`. This will create all the needed files and install all the needed dependencies. The only thing you will need to edit after running this is your `.env`. This will contain your bot's token, secret (which is unneeded without the web server), and GD password. The `.env` should look like this after installation:

```
token=bot token here
password=gd password here
secret=bot secret here
```

## Notes
### Planned features
- Start development of a lot of commands.
- Fix `help` command.
- Finish `partlist` command.
- Fix error "`Invalid OAuth2 redirect_uri`" when logging in on the web server. 

### Known Bugs
- Account linking can cause GD IP ban (Not sure if fixed, nothing I can do about this atm.).
- Web server will start, but all the features pretty much wont work.
- `addpart` command will allow part overwriting.
- JsonDB is buggy.
### Other
- `partlist` command is not an actual command on the bot yet as it is unfinished.
- `help` command is outdated and a lot of it does not work.
- Batch files that run the bot and server have not yet been implemented in the `install.py`
