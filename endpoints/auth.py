import requests
import allure
from endpoints.endpoint import Endpoint


class Auth(Endpoint):
    required_fields = ('token', 'user')

    @allure.step("Авторизация по имени /authorize")
    def new_auth(self, payload):
        self.response = requests.post(f'{self.url}/authorize', json=payload, headers=self.headers)
        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return self.response
