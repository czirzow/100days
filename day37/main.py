# day37: using the post,put,delete methods
import os
from datetime import datetime as dt, timezone
from pprint import pprint


import lib37.pixela as pixela

# debug logic Oddly valued..
#    there is a reason.
UNTESTED = False
TESTED = False
TEST = True


username = str(os.environ.get('pixela_username'))
token = str(os.environ.get('pixela_token'))
if username == '' or token == '':
        raise Exception("Must set the pixela_username and pixela_token environment vars")

DATE = str(dt.now(timezone.utc).strftime('%Y%m%d'))


GRAPH_ID = 'work_on_import'
GRAPH_NAME = 'Times i work on import script'

pixela_api = pixela.ApiPixela(username=username, token=token, date=DATE)
# TODO:
#  there is an abilty to set the date with object. 
#     > pixela_api.set_date('20220131') 
#  setup up a test for that.



if UNTESTED:
    # create a user
    pprint(pixela_api.create_user())


if UNTESTED:
    # Create a graph
    pprint(pixela_api.create_graph(id=GRAPH_ID, name=GRAPH_NAME, 
                                   unit='num', type='int', color='red')
           )

if UNTESTED:
    # Add new pixel
    pprint( pixela_api.add_pixel(GRAPH_ID, "10"))


if UNTESTED:
    # Update a pixel
    pprint(pixela_api.update_pixel(GRAPH_ID, "30"))

if UNTESTED:
    # Delete a pixel
    pprint(pixela_api.delete_pixel(GRAPH_ID))



