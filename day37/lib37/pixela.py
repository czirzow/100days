# porting main.py to a class....
#

import requests
import os
from datetime import datetime as dt, timezone

PIXELA_URL="https://pixe.la"

class ApiPixela():
    # translate color names to japanse
    color_table = {
            'green': 'shibafu',
            'red': 'momiji',
            'blue': 'sora',
            'yellow': 'ichou',
            'purple': 'ajisai',
            'black': 'kuro',
            }

    valid_uris = ('users', 'graphs')

    def __init__(self, token:str, username:str) -> None:
        self.token = token
        self.username = username

    def url_for_users(self):
        return PIXELA_URL + '/v1/users'

    def url_for_graphs(self):
        return PIXELA_URL + f"/v1/users/{self.username}/graphs"

    def auth_headers(self) -> dict:
        return {'X-USER-TOKEN': self.token}

    def create_user(self):
        # Create a user
        url = self.url_for_users()
        params = {
                'token': self.token,
                'username': self.username,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes',
                }
        resp = requests.post(url=url, json=params)
        print(resp.text)

    def create_graph(self, id:str, name:str, unit:str, type:str, color:str = 'green') -> str:
        # Create a graph
        url = self.url_for_graphs()
        graph_config = {
                        'id': id,
                        'name': name,
                        'unit': unit,
                        'type': type,
                        'color': self.color_table[color],
                        }
        return requests.post(url=url, json=graph_config, 
                             headers=self.auth_headers()).text


# The test run:
username = str(os.environ.get('pixela_username'))
token = str(os.environ.get('pixela_token'))
if username == '' or token == '':
    raise Exception("Must set the pixela_ environment vars")
pixela = ApiPixela(token, username) 
if 0:
    print(pixela.url_for_users())
    print(pixela.url_for_graphs())
exit()



MY_GRAPH_ID = 'graph1'
if 0:


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



