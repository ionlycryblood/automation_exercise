from playwright.sync_api import expect
import allure


@allure.suite("Главная страница")
@allure.feature("Навигация по сайту")
@allure.epic("Магазин Automation Exercise")
@allure.tag("navigation", "main", "ui")
class MainPage:
    def __init__(self, page):
        self.page = page
        self.home = page.get_by_role('link', name='Home')
        self.products = page.get_by_text('Products')
        self.cart = page.get_by_role('link', name='Cart')
        self.signup_login = page.get_by_text('Signup / Login')

    @allure.step("Переход на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_home(self):
        with allure.step("Клик на ссылку 'Home'"):
            self.home.click()

    @allure.step("Переход в каталог товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_products(self):
        with allure.step("Клик на ссылку 'Products'"):
            self.products.click()

    @allure.step("Переход в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_cart(self):
        with allure.step("Клик на ссылку 'Cart'"):
            self.cart.click()

    @allure.step("Переход на страницу регистрации/логина")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_signup(self):
        with allure.step("Клик на ссылку 'Signup / Login'"):
            self.signup_login.click()

    @allure.step("Проверка загрузки главной страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверяет что главная страница загружена корректно:
    - Ссылка 'Home' видна
    - Ссылка 'Cart' видна
    """)
    def should_be_loaded(self):
        with allure.step("Проверка видимости ссылки 'Home'"):
            expect(self.home).to_be_visible()

        with allure.step("Проверка видимости ссылки 'Cart'"):
            expect(self.cart).to_be_visible()

        allure.attach(
            "Главная страница успешно загружена, основные элементы отображаются",
            name="main_page_loaded",
            attachment_type=allure.attachment_type.TEXT
        )