from ..pages.loginpage import LoginPage
import pytest

error_messages = {
    1: 'Please fill out this field.',  # email
    2: "Please include an '@' in the email address. '{}' is missing an '@'.",
    3: "Please enter a part following '@'. '{}' is incomplete.",
    4: "Please enter a part followed by '@'. '{}' is incomplete.",
    5: 'Please fill out this field.',  # password
}

@pytest.mark.parametrize(
    "email, password, error_code",
    [
        ('', '', 1), #email - Заполните это поле.
        ('qwe', '', 2), #включите символ "@" в электронный адрес.
        ('qwe@', '', 3), #введите часть адреса после символа "@"
        ('@qwe', '', 4),# введите часть адреса перед символом "@"
        ('qwe@123', '',5),# password - Заполните это поле.
        ('qwe@123', 'qwe', 6),#Your email or password is incorrect!
        ('', '123', 1),# email - Заполните это поле.
        ('timlill@mail.ru', 'qwerty', 7),# correct
    ])



def test_login(page, load, email, password, error_code):
    load.goto_signup()
    load.should_be_loaded()
    login_page = LoginPage(page)
    login_page.login(email, password)


    login_page.verify_login_result(error_code, error_messages)



