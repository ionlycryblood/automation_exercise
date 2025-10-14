from playwright.sync_api import expect

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

    def place_order(self):
        self.place_order_btn.click()

    def should_have_correct_delivery_address(self, user):
        expect(self.name).to_have_text(f"Mr. {user['first_name']} {user['last_name']}")
        expect(self.street).to_have_text(user['address'])
        expected_city_state_zip = f"{user['city']} {user['state']} {user['zipcode']}"
        expect(self.city_state_zip).to_have_text(expected_city_state_zip)
        expect(self.country).to_have_text('India')
        expect(self.phone).to_have_text(user['mobile'])