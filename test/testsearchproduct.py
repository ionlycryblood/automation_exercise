from ..pages.loginpage import LoginPage
from ..pages.allproductspage import AllProductsPage

def test_searching(page, load, email='timlill@mail.ru', password='qwerty', name_of_item='Blue top'):
    load.goto_signup()
    login_page = LoginPage(page)
    login_page.login(email, password)

    load.goto_products()

    products_page = AllProductsPage(page)
    products_page.search(name_of_item)

    products_page.item_should_be_searched(name_of_item)
    gfdgfd
    gfdgfdfd@asfa
