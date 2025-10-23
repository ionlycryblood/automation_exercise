from playwright.sync_api import expect
import allure
import re


@allure.suite("Корзина")
@allure.feature("Управление товарами в корзине")
@allure.epic("Магазин Automation Exercise")
@allure.tag("cart", "regression", "ui")
class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = page.locator('a.btn.btn-default.check_out')
        self.product_name = page.locator('.cart_description h4 a')
        self.product_price = page.locator('.cart_price p')
        self.product_quantity = page.locator('.cart_quantity button')
        self.product_total = page.locator('.cart_total_price')
        self.delete_button = page.locator('.cart_quantity_delete')

    @allure.step("Получение названия товара с индексом {index}")
    def get_product_name(self, index):
        return self.product_name.nth(index)

    @allure.step("Получение цены товара с индексом {index}")
    def get_product_price(self, index):
        return self.product_price.nth(index)

    @allure.step("Получение количества товара с индексом {index}")
    def get_product_quantity(self, index):
        return self.product_quantity.nth(index)

    @allure.step("Получение общей суммы товара с индексом {index}")
    def get_product_total(self, index):
        return self.product_total.nth(index)

    @allure.step("Удаление товара с индексом {index} из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def delete_product(self, index):
        with allure.step(f"Клик на кнопку удаления для товара #{index}"):
            self.delete_button.nth(index).click()

        # ЗАКОММЕНТИРОВАЛ СКРИНШОТ - ПАДАЕТ
        # with allure.step("Проверка что товар удален"):
        #     allure.attach(
        #         self.page.screenshot(),
        #         name=f"after_delete_{index}",
        #         attachment_type=allure.attachment_type.PNG
        #     )

    @allure.step("Переход к оформлению заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def goto_checkout(self):
        with allure.step("Клик на кнопку 'Proceed To Checkout'"):
            self.checkout_btn.click()

            # ЗАКОММЕНТИРОВАЛ СКРИНШОТ - ПАДАЕТ
            # allure.attach(
            #     self.page.screenshot(),
            #     name="checkout_page",
            #     attachment_type=allure.attachment_type.PNG
            # )

    @allure.step("Переход к регистрации/логину из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def register_login(self):
        self.page.get_by_role('link', name='Register / Login').click()

    @allure.step("Проверка отображения товара '{product_name}' в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверяет что товар корректно отображается в корзине:
    - Название товара
    - Цена за единицу  
    - Количество
    - Общая стоимость
    """)
    def should_display_product(self, product_name, price, quantity, total, index):
        with allure.step(f"Проверка названия товара: ожидается '{product_name}'"):
            actual_name = self.get_product_name(index).text_content()
            expect(self.get_product_name(index)).to_have_text(product_name)
            allure.attach(
                f"Ожидалось: {product_name}\nФактически: {actual_name}",
                name="product_name_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка цены: ожидается '{price}'"):
            actual_price = self.get_product_price(index).text_content()
            expect(self.get_product_price(index)).to_have_text(price)
            allure.attach(
                f"Ожидалось: {price}\nФактически: {actual_price}",
                name="product_price_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка количества: ожидается '{quantity}'"):
            actual_quantity = self.get_product_quantity(index).text_content()
            expect(self.get_product_quantity(index)).to_have_text(quantity)
            allure.attach(
                f"Ожидалось: {quantity}\nФактически: {actual_quantity}",
                name="product_quantity_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step(f"Проверка общей суммы: ожидается '{total}'"):
            actual_total = self.get_product_total(index).text_content()
            expect(self.get_product_total(index)).to_have_text(total)
            allure.attach(
                f"Ожидалось: {total}\nФактически: {actual_total}",
                name="product_total_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        # ЗАКОММЕНТИРОВАЛ СКРИНШОТ - ПАДАЕТ
        # with allure.step("Скриншот корзины с товарами"):
        #     allure.attach(
        #         self.page.screenshot(full_page=True),
        #         name="cart_with_products",
        #         attachment_type=allure.attachment_type.PNG
        #     )

    @allure.step("Проверка что товар удален из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def product_should_be_removed(self):
        with allure.step("Проверка что в корзине 0 товаров"):
            actual_count = self.product_quantity.count()
            expect(self.product_quantity).to_have_count(0)
            allure.attach(
                f"Количество товаров в корзине: {actual_count}",
                name="cart_empty_verification",
                attachment_type=allure.attachment_type.TEXT
            )

        # ЗАКОММЕНТИРОВАЛ СКРИНШОТ - ПАДАЕТ
        # with allure.step("Скриншот пустой корзины"):
        #     allure.attach(
        #         self.page.screenshot(full_page=True),
        #         name="empty_cart",
        #         attachment_type=allure.attachment_type.PNG
        #     )

    @allure.step("Полная очистка корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def clear_cart(self):
        delete_count = self.delete_button.count()
        with allure.step(f"Удаление {delete_count} товаров из корзины"):
            for i in range(delete_count):
                self.delete_product(0)  # всегда удаляем первый элемент

        with allure.step("Финальная проверка пустой корзины"):
            self.product_should_be_removed()