from playwright.sync_api import expect
import allure


@allure.suite("Регистрация")
@allure.feature("Создание аккаунта")
@allure.epic("Магазин Automation Exercise")
@allure.tag("registration", "account", "ui")
class CreatedAccPage:
    def __init__(self, page):
        self.page = page
        self.acc_created = page.get_by_text('Account Created!')
        self.continue_btn = page.locator('[data-qa="continue-button"]')

    @allure.step("Продолжение после успешной регистрации")
    @allure.severity(allure.severity_level.NORMAL)
    def continue_click(self):
        with allure.step("Клик на кнопку 'Continue'"):
            self.continue_btn.click()

    @allure.step("Проверка успешного создания аккаунта")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверяет что аккаунт успешно создан:
    - Отображается сообщение 'Account Created!'
    - Кнопка 'Continue' активна и доступна для клика
    """)
    def account_should_be_created(self):
        with allure.step("Проверка сообщения 'Account Created!'"):
            expect(self.acc_created).to_be_visible()
            allure.attach(
                "Сообщение 'Account Created!' успешно отображается",
                name="account_created_message",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка активности кнопки 'Continue'"):
            expect(self.continue_btn).to_be_enabled()
            allure.attach(
                "Кнопка 'Continue' активна и доступна для клика",
                name="continue_button_status",
                attachment_type=allure.attachment_type.TEXT
            )