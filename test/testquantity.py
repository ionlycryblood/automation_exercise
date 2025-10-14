from pages.cartpage import CartPage
from ..pages.loginpage import LoginPage
from ..pages.allproductspage import AllProductsPage
from ..pages.productpage import ProductPage

def test_searching(page, load, email='timlill@mail.ru', password='qwerty'):
    load.goto_signup()
    login_page = LoginPage(page)
    login_page.login(email, password)

    load.goto_products()

    products_page = AllProductsPage(page)
    products_page.view_product(0)

    product_page = ProductPage(page)
    product_page.set_quantity(4)
    product_page.add_to_cart()
    product_page.goto_cart()

    cart_page = CartPage(page)
    cart_page.should_display_product('Blue Top', 'Rs. 500', '4', 'Rs. 2000', index=0)
    cart_page.delete_product(index=0)