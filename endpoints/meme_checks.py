import allure


class MemeStructureChecks:

    @allure.step("Проверить структуру мема")
    def check_meme_structure(self):
        self.check_required_fields()
        self.check_fields_are_str(("text", "url"))
        self.check_field_is_list("tags")
        self.check_field_is_dict("info")

    @allure.step("Проверить, что поля — строки")
    def check_fields_are_str(self, fields):
        assert fields, "Список полей пуст"

        for field in fields:
            value = self.json.get(field)
            assert type(value) == str, (
                f"Поле '{field}' должно быть строкой, а не {type(value)}"
            )

    @allure.step("Проверить, что поле — список")
    def check_field_is_list(self, field):
        value = self.json.get(field)
        assert type(value) == list, (
            f"Поле '{field}' должно быть списком, "
            f"а не {type(value)}. "
            f"Полный ответ: {self.json}"
        )

    @allure.step("Проверить, что поле — словарь")
    def check_field_is_dict(self, field):
            value = self.json.get(field)
            assert type(value) == dict, (
                f"Поле '{field}' должно быть словарём, "
                f"а не {type(value)}. "
                f"Полный ответ: {self.json}"
            )
