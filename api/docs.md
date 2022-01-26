# Development Documentation

**Note:** This is not a documentation on how to use the api (as of now), only development references.

## Getting it running

**This has been tested and developed on Python 3.8, it is recommended that you use that.** First off, you need to install the dependencies, you can do this by running the command below (based on your OS).

### Linux/macOS

```
python3 -m pip install -r requirements.txt
```

### Windows

```
py -3 -m pip install -r requirements.txt
```

Now, inside the `config.json` file, make sure `production` is `false`. I would rather you not run this on production servers.

Now, you need to make sure you have a MongoDB server running. If you changed the URL of it, then make sure to change the key of `mongo_url` in the `config.json` to the correct URL.

Assuming everything is correctly installed, to run the server, open `main.py`. You should see a message like this:

```
INFO:     Started server process [28748]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:5000 (Press CTRL+C to quit)
```
