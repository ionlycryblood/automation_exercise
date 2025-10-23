from playwright.sync_api import expect
import allure


@allure.suite("Оформление заказа")
@allure.feature("Работа с checkout процессом")
@allure.epic("Магазин Automation Exercise")
@allure.tag("checkout", "order", "address", "ui")
class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.place_order_btn = page.get_by_role('link', name='Place Order')
        self.delivery_address = page.locator('#address_delivery')
        self.name = self.delivery_address.locator('.address_firstname.address_lastname')
        self.street = self.delivery_address.locator('.address_address1.address_address2').nth(1)
        self.city_state_zip = self.delivery_address.locator('.address_city.address_state_name.address_postcode')
        self.country = self.delivery_address.locator('.address_country_name')
        self.phone = self.delivery_address.locator('.address_phone')

    @allure.step("Начало оформления заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def place_order(self):
        with allure.step("Клик на кнопку 'Place Order'"):
            self.place_order_btn.click()

    @allure.step("Проверка корректности адреса доставки")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверяет что адрес доставки соответствует данным пользователя:
    - Имя и фамилия
    - Улица и адрес
    - Город, штат и почтовый индекс
    - Страна
    - Телефон
    """)
    def should_have_correct_delivery_address(self, user):
        with allure.step(f"Проверка имени: Mr. {user['first_name']} {user['last_name']}"):
            expected_name = f"Mr. {user['first_name']} {user['last_name']}"
            actual_name = self.name.text_content()
            expect(self.name).to_have_text(expected_name)
            allure.attach(
                f"Ожидалось: {expected_name}\nФактически: {actual_name}",
                name="name_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка адреса: {user['address']}"):
            actual_street = self.street.text_content()
            expect(self.street).to_have_text(user['address'])
            allure.attach(
                f"Ожидалось: {user['address']}\nФактически: {actual_street}",
                name="address_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка города/штата/индекса: {user['city']} {user['state']} {user['zipcode']}"):
            expected_city_state_zip = f"{user['city']} {user['state']} {user['zipcode']}"
            actual_city_state_zip = self.city_state_zip.text_content()
            expect(self.city_state_zip).to_have_text(expected_city_state_zip)
            allure.attach(
                f"Ожидалось: {expected_city_state_zip}\nФактически: {actual_city_state_zip}",
                name="city_state_zip_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка страны: India"):
            actual_country = self.country.text_content()
            expect(self.country).to_have_text('India')
            allure.attach(
                f"Ожидалось: India\nФактически: {actual_country}",
                name="country_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка телефона: {user['mobile']}"):
            actual_phone = self.phone.text_content()
            expect(self.phone).to_have_text(user['mobile'])
            allure.attach(
                f"Ожидалось: {user['mobile']}\nФактически: {actual_phone}",
                name="phone_verification",
                attachment_type=allure.attachment_type.TEXT
            )