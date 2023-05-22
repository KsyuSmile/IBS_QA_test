import requests

from api.base_url import BaseUrl


class GetResource(BaseUrl):
    def list_resource(self, resource):
        res = requests.get(self.base_url + f'/{resource}')
        status = res.status_code
        result = res.json()
        return status, result

    def single_resource(self, resource, r_id):
        res = requests.get(self.base_url + f'/{resource}/{r_id}')
        status = res.status_code
        result = res.json()
        return status, result

