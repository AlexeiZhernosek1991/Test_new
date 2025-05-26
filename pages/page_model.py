from playwright.sync_api import sync_playwright, Page, Browser


class BasePage:

    def __init__(self, browser: Browser):
        self.page :Page = browser.new_page()

    def open(self):
        self.page.goto(self.PAGE_URL)



# class Page_login():
#     page = Page.goto("https://www.saucedemo.com")
#
#     def input_login(self):
#         input_name = self.page.get_by_placeholder("Username")
#         input_name.fill(self.user_name)
#
#     def input_password(self):
#         input_password = self.page.get_by_placeholder("Password")
#         input_password.fill(self.password_)
#
#     def enter_(self):
#         self.page.get_by_role("button").click()
#
# # class Log_in_test:
#     user_name = 'standard_user'
#     password_ = 'secret_sauce'
#     url = 'https://www.saucedemo.com/'
#
#     def __init__(self, sync):
#         self.sync: sync_playwright = sync
#         # self.user_name = None
#         # self.password_ = None
#
#     def create_browser(self):
#         web_dr = self.sync().start()
#         browser = web_dr.chromium.launch(headless=False, slow_mo=1000)
#         return browser
#
#     def make_login(self):
#         browser = self.create_browser()
#         page = browser.new_page()
#         page.goto(self.url)
#         page.get_by_placeholder("Username").fill(self.user_name)
#         page.get_by_placeholder('Password').fill(self.password_)
#         page.get_by_role("button").click()
#         browser.close()
