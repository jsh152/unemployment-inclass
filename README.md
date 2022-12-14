# unemployment-inclass


## Setup

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:
```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local .env file and provide the key like this:
```sh
# this is the ".env" file...
API_KEY="{Insert API Key here}"
```

## usage

Run a sample script:
```sh
python app/my_script.py
```

Run the unemployment report:
```sh
python -m app.unemployment_report
```

## or pass env var from command line:
```sh
API_KEY="____________" python app/unemployment_report.py
```

## run stocks report:
```sh
#python app/stocks.py
```

python -m app.stocks

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Testing

Run tests:

```sh
pytest
```

