import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    @allure.step("Получение одного мема по ID /meme{meme_id}")
    def get_one_meme(self, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)

        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return self.response
