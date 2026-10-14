import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    required_fields = ()

    def __init__(self, token = None):
        self.response = None
        self.json = None
        self.headers = {'Content-Type': 'application/json'}
        if token:
            self.headers['Authorization'] = token

    @allure.step("Проверить статус-код {code}")
    def _check_status_code(self, code):
        assert self.response.status_code == code, (
            f"Ожидали {code}, получили {self.response.status_code}. "
            f"Ответ: {self.response.text}"
        )

    def check_status_code_200(self):
        self._check_status_code(200)

    def check_status_code_201(self):
        self._check_status_code(201)

    def check_status_code_400(self):
        self._check_status_code(400)

    def check_status_code_401(self):
        self._check_status_code(401)

    def check_status_code_404(self):
        self._check_status_code(404)

    @allure.step("Проверить, что обязательные поля присутствуют и не None")
    def check_required_fields(self, fields=None):
        fields = fields if fields else self.required_fields
        assert fields, "Список обязательных полей пуст"
        assert self.json is not None, "json пустой — выполните запрос"

        for field in fields:
            value = self.json.get(field)
            assert value is not None, (
                f"Поле '{field}' отсутствует или None. "
                f"Есть ключи: {list(self.json.keys())}. "
                f"Полный ответ: {self.json}"
            )

    @allure.step("Проверить, что поля равны ожидаемым значениям")
    def check_fields_values(self, expected):
        for field, value in expected.items():
            actual = self.json.get(field)
            assert actual == value, (
                f"Поле '{field}': ожидали {value}, получили {actual}. "
                f"Полный ответ: {self.json}"
            )

    @allure.step("Проверить, что поля — строки")
    def check_fields_are_str(self, fields):
        assert fields, "Список полей пуст"

        for field in fields:
            value = self.json.get(field)
            assert type(value) == str, (
                f"Поле '{field}' должно быть строкой, а не {type(value)}"
            )
