import requests

from api.base_url import BaseUrl


class PostRegister(BaseUrl):
    def register(self, email, password):
        input_register = {
            "email": email,
            "password": password
        }
        res = requests.post(self.base_url + '/register', data=input_register)
        status = res.status_code
        result = res.json()
        return status, result

