import time

from playwright.sync_api import expect, Page, sync_playwright, Dialog, Response, BrowserContext
from pages.login_page import LoginPage

url = "https://demoblaze.com/"
url2 = 'http://uitestingplayground.com/'


#
def test_start():
    with sync_playwright() as web_db:
        browser = web_db.chromium.launch(headless=False, slow_mo=1500)
        page = browser.new_page()
        page.goto(url)

        def accept_alert(alert: Dialog):
            print('<<<' + alert.message + '>>>')
            alert.accept()

        # page.on("response", accept_alert)
        page.get_by_role("link", name='Samsung galaxy s6').click()
        page.on('dialog', accept_alert)
        page.get_by_role("link", name="Add to cart").click()
        time.sleep(5)


#
def test_start2() -> None:
    def get_alert(resp: Dialog):
        time.sleep(3)
        resp.accept()

    with sync_playwright() as web_db:
        browser = web_db.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url2)
        href = page.get_by_role('link', name='Alerts').get_attribute('href')
        page2 = context.new_page()
        page2.on('dialog', get_alert)
        page2.goto(url2 + href)
        page2.get_by_role('button', name='Alert').click()

        # page.on('dialog', get_alert)
        # page.get_by_role('button', name='Prompt').click()
# user_name = 'standard_user'
# password = 'secret_sauce'
# url = ("https://www.saucedemo.com")


# class TestExample:
#     user_name = 'standard_user'
#     password = 'secret_sauce'
#
#
#     def setup_method(self):
#         self.login_page = LoginPage(self.browser)
#     def test_login_in(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.user_name)
#         self.login_page.enter_password(self.password)
#         self.login_page.enter_button_login()
#         expect(self.login_page.page.locator('//div[@class="app_logo"]')).to_contain_text('Swag Labs')
# time.sleep(5)

# expect(page.get_by_role('button', name='checkout'))

# with sync_playwright() as web_db:
#     browser = web_db.chromium.launch(headless=False, slow_mo=1500)
#     page = browser.new_page()
#     page.goto(url)


# with sync_playwright() as web_db:
#     browser = web_db.chromium.launch(headless=False)
#     page = browser.new_page()
#
# page.goto("https://www.saucedemo.com/inventory.html", )
# input_name = page.get_by_placeholder("Username")
# input_name.fill(user_name)
# input_password = page.get_by_placeholder("Password")
# input_password.fill(password)
# page.get_by_role("button").click()
# page.get_by_role('link').click()
# expect(page.locator('//a[@class="title"]'))
# expect(page.locator('//div[@class="footer_copy"]'))

# shopping_cart_container > a
# with sync_playwright() as web_db:
#     browser = web_db.chromium.launch(headless=False, slow_mo=1000)
#     page = browser.new_page()
#     page.goto('https://www.saucedemo.com/')
#     page.get_by_placeholder("Username").fill('standard_user')
#     page.get_by_placeholder('Password').fill('secret_sauce')
#     page.get_by_role("button").click()
# from ssss import Log_in_test
# #
# def test_login():
#    Log_in_test(sync_playwright).make_login()

# web_db = sync_playwright().start()
# browser = web_db.firefox.launch(headless=False, slow_mo=1000)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
# page.get_by_placeholder("Username").fill('standard_user')
# page.get_by_placeholder('Password').fill('secret_sauce')
# page.get_by_role("button").click()
