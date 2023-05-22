import requests

from api.base_url import BaseUrl


class PostLogin(BaseUrl):
    def login(self, email, password):
        input_login = {
            "email": email,
            "password": password
        }
        res = requests.post(self.base_url + '/login', data=input_login)
        status = res.status_code
        result = res.json()
        return status, result