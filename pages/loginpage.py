from playwright.sync_api import expect


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

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_btn.click()

    def signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_btn.click()

    def text_should_be_visible(self):
        expect(self.new_user_text).to_be_visible()
        expect(self.login_text).to_be_visible()

    def should_show_email_validation_error(self, expected_message):
        actual_message = self.login_email.evaluate('el => el.validationMessage')
        assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

    def should_show_password_validation_error(self, expected_message):
        actual_message = self.login_password.evaluate('el => el.validationMessage')
        assert actual_message == expected_message, f"Expected: {expected_message}, Got: {actual_message}"

    def should_show_invalid_credentials_error(self):
        expect(self.page.get_by_text('Your email or password is incorrect!')).to_be_visible()

    def should_be_logged_in_successfully(self):
        expect(self.page.get_by_text('Logout')).to_be_visible()

    def verify_login_result(self, error_code, expected_messages):
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