from playwright.sync_api import expect
import allure


@allure.suite("Авторизация")
@allure.feature("Логин и регистрация пользователя")
@allure.epic("Магазин Automation Exercise")
@allure.tag("login", "signup", "auth", "ui")
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.new_user_text = page.get_by_text('New User Signup!')
        self.login_text = page.get_by_text('Login to your account')

        self.login_email = page.locator('[data-qa="login-email"]')
        self.login_password = page.locator('[data-qa="login-password"]')
        self.login_btn = page.get_by_role('button', name='Login')

        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"]')
        self.signup_btn = page.get_by_role('button', name='Signup')

    @allure.step("Логин с email: {email}")
    @allure.severity(allure.severity_level.CRITICAL)
    def login(self, email, password):
        with allure.step(f"Ввод email: {email}"):
            self.login_email.fill(email)

        with allure.step("Ввод пароля"):
            self.login_password.fill(password)

        with allure.step("Клик на кнопку 'Login'"):
            self.login_btn.click()

    @allure.step("Регистрация нового пользователя: {name}")
    @allure.severity(allure.severity_level.CRITICAL)
    def signup(self, name, email):
        with allure.step(f"Ввод имени: {name}"):
            self.signup_name.fill(name)

        with allure.step(f"Ввод email: {email}"):
            self.signup_email.fill(email)

        with allure.step("Клик на кнопку 'Signup'"):
            self.signup_btn.click()

    @allure.step("Проверка элементов страницы логина")
    @allure.severity(allure.severity_level.NORMAL)
    def text_should_be_visible(self):
        with allure.step("Проверка текста 'New User Signup!'"):
            expect(self.new_user_text).to_be_visible()

        with allure.step("Проверка текста 'Login to your account'"):
            expect(self.login_text).to_be_visible()

    @allure.step("Проверка валидации email")
    @allure.severity(allure.severity_level.NORMAL)
    def should_show_email_validation_error(self, expected_message):
        actual_message = self.login_email.evaluate('el => el.validationMessage')
        assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        allure.attach(
            f"Ожидалось: {expected_message}\nФактически: {actual_message}",
            name="email_validation",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Проверка валидации пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def should_show_password_validation_error(self, expected_message):
        actual_message = self.login_password.evaluate('el => el.validationMessage')
        assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

        allure.attach(
            f"Ожидалось: {expected_message}\nФактически: {actual_message}",
            name="password_validation",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Проверка ошибки неверных учетных данных")
    @allure.severity(allure.severity_level.NORMAL)
    def should_show_invalid_credentials_error(self):
        with allure.step("Поиск сообщения об ошибке"):
            expect(self.page.get_by_text('Your email or password is incorrect!')).to_be_visible()

        allure.attach(
            "Отображается ошибка 'Your email or password is incorrect!'",
            name="invalid_credentials_error",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Проверка успешного логина")
    @allure.severity(allure.severity_level.CRITICAL)
    def should_be_logged_in_successfully(self):
        with allure.step("Проверка отображения кнопки 'Logout'"):
            expect(self.page.get_by_text('Logout')).to_be_visible()

        allure.attach(
            "Пользователь успешно залогинен, кнопка 'Logout' отображается",
            name="login_success",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Верификация результата логина для кода ошибки {error_code}")
    @allure.severity(allure.severity_level.NORMAL)
    def verify_login_result(self, error_code, expected_messages):
        with allure.step(f"Обработка результата для кода ошибки: {error_code}"):
            if error_code in [1, 2, 3, 4]:
                expected_message = expected_messages[error_code]
                self.should_show_email_validation_error(expected_message)
            elif error_code == 5:
                expected_message = expected_messages[error_code]
                self.should_show_password_validation_error(expected_message)
            elif error_code == 6:
                self.should_show_invalid_credentials_error()
            else:  # error_code == 7
                self.should_be_logged_in_successfully()