import pytest
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestLanguage:
    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(30)

        button = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button, 'Кнопка "Добавить в корзину" отсутствует'

