from playwright.sync_api import expect


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

    def register(self, password, first_name, last_name, address, state, city, zipcode, mobile):
        self.mr.check()
        self.password.fill(password)
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.address.scroll_into_view_if_needed() #без этого тест падает тк локаторы тупа не видны
        self.address.fill(address)
        self.country.select_option('India')
        self.state.fill(state)
        self.city.scroll_into_view_if_needed() # тоже самое
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile.fill(mobile)
        self.create_acc_btn.click()

    def delete_acc(self):
        self.page.get_by_role('link', name='Delete Account').click()
        self.page.locator('[data-qa="continue-button"]').click()

    def text_should_be_visible(self):
        expect(self.title_text).to_be_visible()
        expect(self.name).to_have_text()
        expect(self.email).to_be_disabled()