from ..pages.cartpage import CartPage
from ..pages.loginpage import LoginPage
from ..pages.allproductspage import AllProductsPage

def test_searching(page, load, email='timlill@mail.ru', password='qwerty'):
    load.goto_signup()
    login_page = LoginPage(page)
    login_page.login(email, password)

    load.goto_products()

    products_page = AllProductsPage(page)
    name_of_item = [
        'Blue Top',
        'GRAPHIC DESIGN MEN T SHIRT - BLUE'
    ]
    products_page.add_product(name_of_item[0])
    products_page.add_product(name_of_item[1])

    products_page.goto_cart()

    cart_page = CartPage(page)
    cart_page.should_display_product('Blue Top', 'Rs. 500', '1', 'Rs. 500', index=0)
    cart_page.should_display_product('GRAPHIC DESIGN MEN T SHIRT - BLUE', 'Rs. 1389', '1', 'Rs. 1389', index=1)

    cart_page.delete_product(index=1)
    cart_page.delete_product(index=0)

    cart_page.product_should_be_removed()


