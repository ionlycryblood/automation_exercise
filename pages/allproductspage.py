from playwright.sync_api import expect

class AllProductsPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator('')
        self.search_product = page.get_by_placeholder('Search Product')
        self.search_btn = page.locator('#submit_search')
        self.woman_category = page.locator('a[data-toggle="collapse"][href="#Woman"]')
        self.men_category = page.locator('a[data-toggle="collapse"][href="#Men"]')
        self.kids_category = page.locator('a[data-toggle="collapse"][href="#Kids"]')
        self.view_product_btn = page.get_by_role('link', name='View Product')



    def search(self, name_of_item):
        self.search_product.fill(f'{name_of_item}')
        self.search_btn.click()

    def add_product(self, name_of_item):
        item = self.page.locator(f"div.productinfo.text-center:has-text('{name_of_item}')")
        item.hover()
        add_item_btn = item.get_by_text('Add to cart')
        add_item_btn.click()
        self.page.get_by_text('Continue Shopping').click()

    def goto_cart(self):
        cart = self.page.get_by_role('link', name='Cart')
        cart.scroll_into_view_if_needed()
        cart.click()

    def view_product(self, index):
        self.view_product_btn.nth(index).click()

    def for_women(self):
        self.woman_category.click()
        self.page.locator('a:has-text("Dress")').click()

    def for_men(self):
        self.men_category.click()
        self.page.locator('a:has-text("Tshirts")').click()


    def for_kids(self):
        self.kids_category.click()
        self.page.locator('a:has-text("Dress")').click()

    def item_should_be_searched(self, name_of_item):
        item = self.page.locator(f"div.productinfo.text-center:has-text('{name_of_item}')")
        item.hover()

        expect(item).to_be_visible()