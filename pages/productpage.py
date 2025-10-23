import allure


@allure.suite("Страница товара")
@allure.feature("Детали товара и добавление в корзину")
@allure.epic("Магазин Automation Exercise")
@allure.tag("product", "details", "quantity", "ui")
class ProductPage:
    def __init__(self, page):
        self.page = page
        self.quantity = page.locator('#quantity')
        self.add_to_cart_btn = page.get_by_role('button', name='Add to cart')
        self.cartpage = page.get_by_role('link', name='Cart')

    @allure.step("Установка количества товара: {value}")
    @allure.severity(allure.severity_level.NORMAL)
    def set_quantity(self, value):
        with allure.step(f"Заполнение поля количества значением: {value}"):
            self.quantity.fill(str(value))

        allure.attach(
            f"Количество товара установлено: {value}",
            name="quantity_set",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def add_to_cart(self):
        with allure.step("Клик на кнопку 'Add to cart'"):
            self.add_to_cart_btn.click()

        with allure.step("Клик на кнопку 'Continue Shopping'"):
            self.page.get_by_role('button', name='Continue Shopping').click()

        allure.attach(
            "Товар успешно добавлен в корзину",
            name="product_added_to_cart",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.step("Переход в корзину со страницы товара")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_cart(self):
        with allure.step("Клик на ссылку 'Cart'"):
            self.cartpage.click()