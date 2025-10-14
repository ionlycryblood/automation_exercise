from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.locator('a.btn.btn-default.check_out')
        self.product_name = page.locator('.cart_description h4 a')
        self.product_price = page.locator('.cart_price p')
        self.product_quantity = page.locator('.cart_quantity button')
        self.product_total = page.locator('.cart_total_price')
        self.delete_button = page.locator('.cart_quantity_delete')

    def get_product_name(self, index):
        return self.product_name.nth(index)

    def get_product_price(self, index):
        return self.product_price.nth(index)

    def get_product_quantity(self, index):
        return self.product_quantity.nth(index)

    def get_product_total(self, index):
        return self.product_total.nth(index)

    def delete_product(self, index):
        self.delete_button.nth(index).click()

    def goto_checkout(self):
        self.checkout_btn.click()

    def register_login(self):
        self.page.get_by_role('link', name='Register / Login').click()

    def should_display_product(self, product_name, price, quantity, total, index):
        expect(self.get_product_name(index)).to_have_text(product_name)
        expect(self.get_product_price(index)).to_have_text(price)
        expect(self.get_product_quantity(index)).to_have_text(quantity)
        expect(self.get_product_total(index)).to_have_text(total)

    def product_should_be_removed(self):
        expect(self.product_quantity).to_have_count(0)
