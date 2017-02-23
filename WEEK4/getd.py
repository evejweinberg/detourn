import requests
url = 'thing goes here'
response = requests.get(url).json()
#this just turned it into a python dictionary

responses = response['response']

for r in responses:
    print r['raw_message']

    # try converting code from curl to python
