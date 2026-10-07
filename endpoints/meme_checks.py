import allure


class MemeStructureChecks:

    @allure.step("Проверить структуру мема")
    def check_meme_structure(self):
        self.check_required_fields()
        self.check_fields_are_str(("text", "url"))
        self.check_field_is_list("tags")
        self.check_field_is_dict("info")