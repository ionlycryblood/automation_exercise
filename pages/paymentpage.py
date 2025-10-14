from playwright.sync_api import expect

class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.card_name = page.locator('[data-qa="name-on-card"]')
        self.card_number = page.locator('[data-qa="card-number"]')
        self.cvc = page.locator('[data-qa="cvc"]')
        self.exp_month = page.locator('[data-qa="expiry-month"]')
        self.exp_year = page.locator('[data-qa="expiry-year"]')
        self.pay_n_confirm = page.locator('[data-qa="pay-button"]')

    def fill_card(self, card_name, card_number, cvc, exp_month, exp_year):
        self.card_name.fill(card_name)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.exp_month.fill(exp_month)
        self.exp_year.fill(exp_year)
        self.pay_n_confirm.click()

    def payment_should_be_done(self):
        congrats = self.page.get_by_text('Congratulations! Your order has been confirmed!')
        expect(congrats).to_be_visible()

    def continue_pay(self):
        self.page.locator('[data-qa="continue-button"]').click()


