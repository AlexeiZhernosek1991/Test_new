import pytest
from playwright.sync_api import sync_playwright,Browser




# @pytest.fixture(autouse=True, scope='class')
# def browser_(request):
#     web_db = sync_playwright().start()
#     browser: Browser = web_db.chromium.launch(headless=False, slow_mo=1000)
#     request.cls.browser = browser

