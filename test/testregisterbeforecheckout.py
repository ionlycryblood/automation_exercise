from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from pages.createdaccpage import CreatedAccPage
from pages.paymentpage import PaymentPage
from pages.signuppage import SignupPage
from pages.loginpage import LoginPage
from pages.allproductspage import AllProductsPage
from utils.data_generator import random_user

def test_searching(page, load):
    user = random_user()

    load.goto_signup()
    login_page = LoginPage(page)

    login_page.signup(user['name'],
                      user['email'])

    signup_page = SignupPage(page)
    signup_page.register(user['password'],
                         user['first_name'],
                         user['last_name'],
                         user['address'],
                         user['state'],
                         user['city'],
                         user['zipcode'],
                         user['mobile'])

    created_acc_page = CreatedAccPage(page)
    created_acc_page.continue_click()

    page.get_by_text('Logout').click()
    login_page.login(user['email'], user['password'])

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
    cart_page.goto_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.should_have_correct_delivery_address(user)
    checkout_page.place_order()

    payment_page = PaymentPage(page)
    payment_page.fill_card(user['first_name'],
                           user['number'],
                           user['security_code'],
                           user['month'],
                           user['year'])
    payment_page.payment_should_be_done()
    payment_page.continue_pay()
    signup_page.delete_acc()
