from playwright.sync_api import expect
import allure


@allure.suite("Товары")
@allure.feature("Работа с каталогом товаров")
@allure.epic("Магазин Automation Exercise")
@allure.tag("products", "catalog", "search", "ui")
class AllProductsPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator('')
        self.search_product = page.get_by_placeholder('Search Product')
        self.search_btn = page.locator('#submit_search')
        self.woman_category = page.locator('a[data-toggle="collapse"][href="#Woman"]')
        self.men_category = page.locator('a[data-toggle="collapse"][href="#Men"]')
        self.kids_category = page.locator('a[data-toggle="collapse"][href="#Kids"]')
        self.view_product_btn = page.get_by_role('link', name='View Product')

    @allure.step("Поиск товара '{name_of_item}'")
    @allure.severity(allure.severity_level.NORMAL)
    def search(self, name_of_item):
        with allure.step(f"Ввод названия товара в поиск: {name_of_item}"):
            self.search_product.fill(f'{name_of_item}')

        with allure.step("Клик на кнопку поиска"):
            self.search_btn.click()

    @allure.step("Добавление товара '{name_of_item}' в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def add_product(self, name_of_item):
        with allure.step(f"Поиск карточки товара: {name_of_item}"):
            item = self.page.locator(f"div.productinfo.text-center:has-text('{name_of_item}')")

        with allure.step("Наведение курсора на товар"):
            item.hover()

        with allure.step("Клик на кнопку 'Add to cart'"):
            add_item_btn = item.get_by_text('Add to cart')
            add_item_btn.click()

        with allure.step("Клик на 'Continue Shopping'"):
            self.page.get_by_text('Continue Shopping').click()

    @allure.step("Переход в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    def goto_cart(self):
        with allure.step("Прокрутка к кнопке корзины"):
            cart = self.page.get_by_role('link', name='Cart')
            cart.scroll_into_view_if_needed()

        with allure.step("Клик на кнопку корзины"):
            cart.click()

    @allure.step("Просмотр товара с индексом {index}")
    @allure.severity(allure.severity_level.NORMAL)
    def view_product(self, index):
        with allure.step(f"Клик на кнопку 'View Product' для товара #{index}"):
            self.view_product_btn.nth(index).click()

    @allure.step("Фильтрация по категории 'Women' -> 'Dress'")
    @allure.severity(allure.severity_level.NORMAL)
    def for_women(self):
        with allure.step("Клик на категорию 'Women'"):
            self.woman_category.click()

        with allure.step("Выбор подкатегории 'Dress'"):
            self.page.locator('a:has-text("Dress")').click()

    @allure.step("Фильтрация по категории 'Men' -> 'Tshirts'")
    @allure.severity(allure.severity_level.NORMAL)
    def for_men(self):
        with allure.step("Клик на категорию 'Men'"):
            self.men_category.click()

        with allure.step("Выбор подкатегории 'Tshirts'"):
            self.page.locator('a:has-text("Tshirts")').click()

    @allure.step("Фильтрация по категории 'Kids' -> 'Dress'")
    @allure.severity(allure.severity_level.NORMAL)
    def for_kids(self):
        with allure.step("Клик на категорию 'Kids'"):
            self.kids_category.click()

        with allure.step("Выбор подкатегории 'Dress'"):
            self.page.locator('a:has-text("Dress")').click()

    @allure.step("Проверка что товар '{name_of_item}' найден в поиске")
    @allure.severity(allure.severity_level.NORMAL)
    def item_should_be_searched(self, name_of_item):
        with allure.step(f"Поиск карточки товара: {name_of_item}"):
            item = self.page.locator(f"div.productinfo.text-center:has-text('{name_of_item}')")

        with allure.step("Наведение курсора на товар"):
            item.hover()

        with allure.step("Проверка видимости товара"):
            expect(item).to_be_visible()

            allure.attach(
                f"Товар '{name_of_item}' успешно найден и отображается",
                name="search_verification",
                attachment_type=allure.attachment_type.TEXT
            )