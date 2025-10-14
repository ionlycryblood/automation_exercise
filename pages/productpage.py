class ProductPage:
    def __init__(self, page):
        self.page = page
        self.quantity = page.locator('#quantity')
        self.add_to_cart_btn = page.get_by_role('button', name='Add to cart')
        self.cartpage = page.get_by_role('link', name='Cart')


    def set_quantity(self, value):
        self.quantity.fill(str(value))

    def add_to_cart(self):
        self.add_to_cart_btn.click()
        self.page.get_by_role('button', name='Continue Shopping').click()

    def goto_cart(self):
        self.cartpage.click()
