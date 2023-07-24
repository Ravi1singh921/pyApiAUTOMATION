'''

Author:Ravi
objective: create & verify by post request
Tc1#- verify the status code
Tc2#- Verify the body --> booking id
Tc3#- verify the json schema is valid
'''


import pytest
import requests

from SRC.constants.apiconstants import  base_url, url_create_booking
from SRC.helpers.api_wrapper import post_request
from SRC.helpers.payload_manager import payload_create_booking

# base url
# verify


class TestIntigration (object):
    header = {
        "Content-Type: application/json"
    }
    def test_create_booking_tc1(self):
        # url
        response=post_request(url_create_booking(), headers=header,  auth=None, payload=payload_create_booking(), in_json=False)
        print(response.status_code)


'''
    def test_create_booking_tc2(self):
        assert True == False

    def test_create_booking_tc3(self):
        assert True == True

'''