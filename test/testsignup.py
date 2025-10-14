from ..pages.loginpage import LoginPage
from ..pages.signuppage import SignupPage
from ..pages.createdaccpage import CreatedAccPage
from ..utils.data_generator import random_user


def test_signup(page, load):
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
    login_page.login(user['email'],user['password'])

    signup_page.delete_acc()

