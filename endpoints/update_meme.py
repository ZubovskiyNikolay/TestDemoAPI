import requests
import allure

from endpoints.endpoint import Endpoint
from endpoints.meme_checks import MemeStructureChecks


class UpdateMeme(Endpoint, MemeStructureChecks):
    required_fields = ('id', 'text', 'url', 'tags', 'info', 'updated_by')

    @allure.step("Обновить мем PUT /meme/{meme_id} с новыми данными")
    def update_meme(self, meme_id, payload):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=self.headers
        )
        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return
