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
        self.date = str(dt.now(timezone.utc).strftime('%Y%m%d'))

    def url_for_users(self):
        return PIXELA_URL + '/v1/users'

    def url_for_graphs(self):
        return PIXELA_URL + f"/v1/users/{self.username}/graphs"

    def auth_headers(self) -> dict:
        return {'X-USER-TOKEN': self.token}


    def get_date(self) -> str:
        return self.date

    def set_date(self, date:str) -> None:
        """ format: YYYYMMDD """
        self.date = date

    def create_user(self) -> str:
        # Create a user
        url = self.url_for_users()
        params = {
                'token': self.token,
                'username': self.username,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes',
                }
        return requests.post(url=url, json=params).text

    def create_graph(self, id:str, name:str, unit:str, type:str, color:str = 'green') -> str:
        # Create a graph
        url = self.url_for_graphs()

        # TODO: make just a graph_config:dict that is passed instead of all the params
        # move this to caller.
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
if 1:
    print(pixela.url_for_users())
    print(pixela.url_for_graphs())

# test these:
#
#print(pixela.create_user())
# 
#print(pixela.create_graph())
exit()


"""
if 0:
    def add_pixel(report_data):
        # Add new pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}"
        report_data = {
                        'date': MY_DATE,
                        'quantity': "10",
                       }
        resp = requests.post(url=url, json=report_data, headers=AUTH_HEADERS)
        print(resp.text)

if 0:
    def update_pixel(report_data: dict)
        # Update a pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}/{MY_DATE}"
        report_data = {
                        'date': MY_DATE,
                        'quantity': "15",
                       }
        resp = requests.put(url=url, json=report_data, headers=AUTH_HEADERS)
        print(resp.text)

if 0:
    def delete_pixel():
        # Delete a pixel
        url = PIXEL_URL_GRAPHS + f"/{MY_GRAPH_ID}/{MY_DATE}"
        resp = requests.delete(url=url, headers=AUTH_HEADERS)
        print(resp.text)


"""
