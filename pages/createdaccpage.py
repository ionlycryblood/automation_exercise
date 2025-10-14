from playwright.sync_api import expect


class CreatedAccPage:
    def __init__(self, page):
        self.page = page
        self.acc_created = page.get_by_text('Account Created!')
        self.continue_btn = page.locator('[data-qa="continue-button"]')

    def continue_click(self):
        self.continue_btn.click()

    def account_should_be_created(self):
        expect(self.acc_created).to_be_visible()
        expect(self.continue_btn).to_be_enabled()