from ..pages.loginpage import LoginPage
import pytest

error_messages = {
    1: 'Заполните это поле.',  # email
    2: 'Адрес электронной почты должен содержать символ "@". В адресе "qwe" отсутствует символ "@".',
    3: 'Введите часть адреса после символа "@". Адрес "qwe@" неполный.',
    4: 'Введите часть адреса до символа "@". Адрес "@qwe" неполный.',
    5: 'Заполните это поле.', #password
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



