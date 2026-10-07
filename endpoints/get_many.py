import requests
import allure
from endpoints.endpoint import Endpoint


class GetManyMeme(Endpoint):
    @allure.step("Получение списка мемов /meme")
    def get_all_meme(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        try:
            self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = None
        return self.response

    @allure.step("Проверить, что мем {meme_id} есть в списке")
    def check_meme_in_list(self, meme_id):
        ids = [meme.get("id") for meme in self.json["data"]]
        assert meme_id in ids, (
            f"Мем {meme_id} не найден в списке. "
            f"Есть id: {ids}"
        )
