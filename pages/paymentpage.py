from playwright.sync_api import expect
import allure


@allure.suite("Оплата")
@allure.feature("Оформление платежа")
@allure.epic("Магазин Automation Exercise")
@allure.tag("payment", "checkout", "credit_card", "ui")
class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.card_name = page.locator('[data-qa="name-on-card"]')
        self.card_number = page.locator('[data-qa="card-number"]')
        self.cvc = page.locator('[data-qa="cvc"]')
        self.exp_month = page.locator('[data-qa="expiry-month"]')
        self.exp_year = page.locator('[data-qa="expiry-year"]')
        self.pay_n_confirm = page.locator('[data-qa="pay-button"]')

    @allure.step("Заполнение данных карты")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Заполняет все поля данных кредитной карты:
    - Имя на карте
    - Номер карты
    - CVC код
    - Месяц expiration
    - Год expiration
    """)
    def fill_card(self, card_name, card_number, cvc, exp_month, exp_year):
        with allure.step(f"Ввод имени на карте: {card_name}"):
            self.card_name.fill(card_name)

        with allure.step("Ввод номера карты"):
            self.card_number.fill(card_number)

        with allure.step("Ввод CVC кода"):
            self.cvc.fill(cvc)

        with allure.step(f"Ввод месяца expiration: {exp_month}"):
            self.exp_month.fill(exp_month)

        with allure.step(f"Ввод года expiration: {exp_year}"):
            self.exp_year.fill(exp_year)

        with allure.step("Клик на кнопку 'Pay and Confirm Order'"):
            self.pay_n_confirm.click()

    @allure.step("Проверка успешного завершения оплаты")
    @allure.severity(allure.severity_level.CRITICAL)
    def payment_should_be_done(self):
        with allure.step("Поиск сообщения об успешном заказе"):
            congrats = self.page.get_by_text('Congratulations! Your order has been confirmed!')
            expect(congrats).to_be_visible()

        allure.attach(
            "Платеж успешно завершен, отображается сообщение 'Congratulations! Your order has been confirmed!'",
            name="payment_success",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Продолжение после оплаты")
    @allure.severity(allure.severity_level.NORMAL)
    def continue_pay(self):
        with allure.step("Клик на кнопку 'Continue'"):
            self.page.locator('[data-qa="continue-button"]').click()


