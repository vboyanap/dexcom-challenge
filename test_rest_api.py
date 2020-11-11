import requests
import json
import pytest
from config import configuration as cfg


class Restapi():
    @pytest.fixture(scope="class", autouse=True)
    def __init__(self, resp_dict, auth_token, canonical_id, user_canonical_id):
        self.resp_dict = resp_dict
        self.auth_token = auth_token
        
    def login(self):
        headers = {
            'Content-Type': 'application/json',
                    }
        data = {"username":cfg.USER,"password":cfg.PASSWORD}
        response = requests.get("https://clarity.dexcom.com/", headers=headers, data=data, verify=False)
        self.resp_dict = json.loads(response)
        self.auth_token = self.resp_dict['payload']['token']
        assert self.auth_token

        response = response.post("/api/subject/1681277794575765504/analysis_session", headers = self.auth_token, data=data, verify = False)


rest = Restapi()
rest.login()