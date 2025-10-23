from playwright.sync_api import expect
import allure


@allure.suite("Регистрация")
@allure.feature("Заполнение информации об аккаунте")
@allure.epic("Магазин Automation Exercise")
@allure.tag("signup", "registration", "account", "ui")
class SignupPage:
    def __init__(self, page):
        self.page = page
        self.title_text = page.get_by_text('Enter Account Information')

        self.mr = page.locator('#id_gender1').first
        self.name = page.locator('[data-qa="name"]')
        self.email = page.locator('[data-qa="email"]')
        self.first_name = page.locator('[data-qa="first_name"]')
        self.password = page.locator('[data-qa="password"]')
        self.birth_day = page.locator('[data-qa="days"]')
        self.birth_month = page.locator('[data-qa="months"]')
        self.birth_year = page.locator('[data-qa="years"]')
        self.last_name = page.locator('[data-qa="last_name"]')
        self.address = page.locator('#address1')
        self.country = page.locator('[data-qa="country"]')
        self.state = page.locator('[data-qa="state"]')
        self.city = page.locator('[data-qa="city"]')
        self.zipcode = page.locator('[data-qa="zipcode"]')
        self.mobile = page.locator('[data-qa="mobile_number"]')
        self.create_acc_btn = page.locator('[data-qa="create-account"]')

    @allure.step("Регистрация нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Полное заполнение формы регистрации пользователя:
    - Выбор пола (Mr)
    - Личная информация (имя, фамилия, пароль)
    - Адресные данные
    - Контактная информация
    """)
    def register(self, password, first_name, last_name, address, state, city, zipcode, mobile):
        with allure.step("Выбор пола 'Mr'"):
            self.mr.check()

        with allure.step("Ввод пароля"):
            self.password.fill(password)

        with allure.step(f"Ввод имени: {first_name}"):
            self.first_name.fill(first_name)

        with allure.step(f"Ввод фамилии: {last_name}"):
            self.last_name.fill(last_name)

        with allure.step("Прокрутка к полю адреса"):
            self.address.scroll_into_view_if_needed()

        with allure.step(f"Ввод адреса: {address}"):
            self.address.fill(address)

        with allure.step("Выбор страны: India"):
            self.country.select_option('India')

        with allure.step(f"Ввод штата: {state}"):
            self.state.fill(state)

        with allure.step("Прокрутка к полю города"):
            self.city.scroll_into_view_if_needed()

        with allure.step(f"Ввод города: {city}"):
            self.city.fill(city)

        with allure.step(f"Ввод почтового индекса: {zipcode}"):
            self.zipcode.fill(zipcode)

        with allure.step(f"Ввод номера телефона: {mobile}"):
            self.mobile.fill(mobile)

        with allure.step("Клик на кнопку 'Create Account'"):
            self.create_acc_btn.click()

    @allure.step("Удаление аккаунта")
    @allure.severity(allure.severity_level.NORMAL)
    def delete_acc(self):
        with allure.step("Клик на ссылку 'Delete Account'"):
            self.page.get_by_role('link', name='Delete Account').click()

        with allure.step("Клик на кнопку 'Continue'"):
            self.page.locator('[data-qa="continue-button"]').click()

    @allure.step("Проверка элементов страницы регистрации")
    @allure.severity(allure.severity_level.NORMAL)
    def text_should_be_visible(self):
        with allure.step("Проверка заголовка 'Enter Account Information'"):
            expect(self.title_text).to_be_visible()

        with allure.step("Проверка поля имени"):
            expect(self.name).to_have_text()

        with allure.step("Проверка что поле email заблокировано"):
            expect(self.email).to_be_disabled()

        allure.attach(
            "Страница регистрации загружена корректно, все необходимые элементы отображаются",
            name="signup_page_loaded",
            attachment_type=allure.attachment_type.TEXT
        )