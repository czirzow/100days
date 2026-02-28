# day37: using the post,put,delete methods
import requests
import os
from datetime import datetime as dt, timezone

PIXELA_USERNAME=os.environ.get('pixela_username')
PIXELA_TOKEN=os.environ.get('pixela_token')
if PIXELA_USERNAME == '' or PIXELA_TOKEN == '':
        raise Exception("Must set the PIXELA_ environment vars")

# translate color names
PIXELA_COLORS = {
                'green': 'shibafu',
                'red': 'momiji',
                'blue': 'sora',
                'yellow': 'ichou',
                'purple': 'ajisai',
                'black': 'kuro',
                }

# note: each entry does not have a slash at the end.
PIXELA_URL="https://pixe.la"
PIXEL_URL_USERS = PIXELA_URL + '/v1/users'
PIXEL_URL_GRAPHS = PIXELA_URL + f"/v1/users/{PIXELA_USERNAME}/graphs"


if 0:
        # Create a user
        url = PIXEL_URL_USERS
        params = {
                        'token': PIXELA_TOKEN,
                        'username': PIXELA_USERNAME,
                        'agreeTermsOfService': 'yes',
                        'notMinor': 'yes',
                }
        resp = requests.post(url=url, json=params)
        print(resp.text)


MY_GRAPH_ID = 'graph1'
AUTH_HEADERS = {'X-USER-TOKEN': PIXELA_TOKEN}
if 0:
        # Create a graph
        url = PIXEL_URL_GRAPHS
        graph_config = {
                        'id': MY_GRAPH_ID,
                        'name': 'Programming Graph',
                        'unit': 'commit',
                        'type': 'int',
                        'color': PIXELA_COLORS['green'],
                        'description': 'keep track of when work on code.',
                        }
        resp = requests.post(url=url, json=graph_config, headers=AUTH_HEADERS)
        print(resp.text)


MY_DATE = str(dt.now(timezone.utc).strftime('%Y%m%d'))
if 0:
        # Add new pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}"
        report_data = {
                        'date': MY_DATE,
                        'quantity': "10",
                       }
        resp = requests.post(url=url, json=report_data, headers=AUTH_HEADERS)
        print(resp.text)

if 0:
        # Update a pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}/{MY_DATE}"
        report_data = {
                        'date': MY_DATE,
                        'quantity': "15",
                       }
        resp = requests.put(url=url, json=report_data, headers=AUTH_HEADERS)
        print(resp.text)

if 0:
        # Delete a pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}/{MY_DATE}"
        resp = requests.delete(url=url, headers=AUTH_HEADERS)
        print(resp.text)



