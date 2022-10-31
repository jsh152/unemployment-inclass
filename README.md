# unemployment-inclass


## Setup

Create and activate a virtual environment:

'''sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
'''

Install package dependencies:
'''sh
pip install -r requirements.txt
'''

## Configuration


Obtain an API Key from Aplpha Vantage

Then create a local .env file and provide the key like this:
''sh
# this is the ".env" file...
API_KEY="abc123"
'''

## usage

Run a sample script:
'''sh
python app/my_script.py
'''

Run the unemployment report:
'''sh
python app/unemployment_report.py
'''

#or pass env var from command line:
API_KEY="____________" python app/unemployment_report.py
'''




