import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step("Удалить mem с ID /meme/{meme_id}")
    def delete_meme(self, meme_id):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers=self.headers
        )
        return meme_id
