import requests

from api.base_url import BaseUrl


class GetUsers(BaseUrl):

    def list_users(self, page, per_page):
        params = {'page': page, 'per_page': per_page}
        res = requests.get(self.base_url + '/users', params=params)
        status = res.status_code
        result = res.json()
        return status, result

    def single_users(self, user_id):
        res = requests.get(self.base_url + f'/users/{user_id}')
        status = res.status_code
        result = res.json()
        return status, result

    def delayed_response(self, delay):
        params = {'delay': delay}
        res = requests.get(self.base_url + '/users', params=params)
        status = res.status_code
        result = res.json()
        return status, result


class PostUsers(BaseUrl):
    def create_new_user(self, name, job):
        input_user = {
            "name": name,
            "job": job
        }
        res = requests.post(self.base_url + '/users', data=input_user)
        status = res.status_code
        result = res.json()
        return status, result


class UpdateUsers(BaseUrl):
    def update_user_put(self, user_id, name, job):
        input_user = {
            "name": name,
            "job": job
        }
        res = requests.put(self.base_url + f'/users/{user_id}', data=input_user)
        status = res.status_code
        result = res.json()
        return status, result

    def update_user_patch(self, user_id, name, job):
        input_user = {
            "name": name,
            "job": job
        }
        res = requests.patch(self.base_url + f'/users/{user_id}', data=input_user)
        status = res.status_code
        result = res.json()
        return status, result


class DeleteUsers(BaseUrl):
    def delete(self, user_id):
        res = requests.delete(self.base_url + f'/users/{user_id}')
        status = res.status_code
        return status
