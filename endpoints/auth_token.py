import requests
import allure
from endpoints.endpoint import Endpoint


class AuthAlive(Endpoint):

    @allure.step("Проверить, что токен авторизации жив /authorize")
    def auth_token_alive(self, token):
        self.response = requests.get(f'{self.url}/authorize/{token}', headers=self.headers)
        return self.response

    @allure.step("Проверить, что токен принадлежит '{username}'")
    def check_token_user(self, username):
        assert username in self.response.text, (
            f"В ответе нет '{username}'. Ответ: {self.response.text}"
        )
