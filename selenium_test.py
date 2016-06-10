#Selenium Test
from selenium import webdriver
import pytest
import os
import time

class TestWebpages(object):

    @pytest.fixture(scope='function')
    def browser(self, request):
        browser = webdriver.Firefox()

        def fin():
            browser.quit()

        request.addfinalizer(fin)
        return browser

    def test_amazon(self, browser):
        browser.get("http://www.amazon.com")
        assert 'Amazon' in browser.title

    def test_google(self, browser):
        browser.get("http://www.google.com")
        assert "Google" in browser.title