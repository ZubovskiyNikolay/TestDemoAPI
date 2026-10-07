import requests
import allure

from endpoints.endpoint import Endpoint
from endpoints.meme_checks import MemeStructureChecks


class CreateMeme(Endpoint, MemeStructureChecks):
    required_fields = ('id', 'text', 'url', 'tags', 'info', 'updated_by')

    @allure.step("Создать мем на /meme")
    def create_new_meme(self, payload):
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=self.headers)
        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return self.response
