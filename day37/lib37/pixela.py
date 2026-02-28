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

    def __init__(self, token:str, username:str, date:str = '') -> None:
        self.token = token
        self.username = username

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

    def create_user(self) -> dict:
        # Create a user
        url = self.url_for_users()
        params = {
                'token': self.token,
                'username': self.username,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes',
                }
        return requests.post(url=url, json=params).json()

    def create_graph(self, id:str, name:str, unit:str, type:str, color:str = 'green') -> dict:
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
                             headers=self.auth_headers()).json()

    def add_pixel(self, graphid:str, quantity:str) -> dict:
        # Add new pixel
        url = self.url_for_graphs() + f"/{graphid}"
        report_data = {
                        'date': self.date,
                        'quantity': f"{quantity}",
                       }
        return requests.post(url=url, json=report_data, 
                             headers=self.auth_headers()).json()

    def update_pixel(self, graphid:str, amount:str) -> dict:
        # Update a pixel
        url = self.url_for_graphs() + f"/{graphid}/{self.date}"
        report_data = {
                        'date': self.date,
                        'quantity': f"{amount}",
                       }
        return requests.put(url=url, json=report_data, 
                            headers=self.auth_headers()).json()

    def delete_pixel(self, graphid:str, date:str) -> dict:
        # Delete a pixel
        url = self.url_for_graphs() + f"/{graphid}/{self.date}"
        return requests.delete(url=url, headers=self.auth_headers()).json()

# The test run:
username = str(os.environ.get('pixela_username'))
token = str(os.environ.get('pixela_token'))
if username == '' or token == '':
    raise Exception("Must set the pixela_ environment vars")
pixela = ApiPixela(token, username) 
if 0:
    print(pixela.url_for_users())
    print(pixela.url_for_graphs())

# test these:
#
#print(pixela.create_user())
# 
#print(pixela.create_graph())
exit()


