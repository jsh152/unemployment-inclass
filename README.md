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

## Testing

Run tests:

```sh
pytest
```
### Email Sending

Run the email service to send an example email and see if everything is working:

```sh
python -m app.email_service
```

Send the unemployment report via email:

```sh
python -m app.unemployment_email
```

Send the stocks report via email:

```sh
python -m app.stocks_email

# or in production mode:
APP_ENV="production" DEFAULT_SYMBOL="GOOGL" python -m app.stocks_email
