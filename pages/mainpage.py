from playwright.sync_api import expect


class MainPage:
    def __init__(self, page):
        self.page = page
        self.home = page.get_by_role('link', name='Home')
        self.products = page.get_by_text('Products')
        self.cart = page.get_by_role('link', name='Cart')
        self.signup_login = page.get_by_text('Signup / Login')

    def goto_home(self):
        self.home.click()

    def goto_products(self):
        self.products.click()

    def goto_cart(self):
        self.cart.click()

    def goto_signup(self):
        self.signup_login.click()

    def should_be_loaded(self):
        expect(self.home).to_be_visible()
        expect(self.cart).to_be_visible()


#gfdgfdfd@asfa
#qwerty
        