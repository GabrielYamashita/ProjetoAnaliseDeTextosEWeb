

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '€'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.de/"

CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\gabri\\AppData\\Local\\Google\\Chrome\\User Data\\WebScrapping\\Yama"



def get_chrome_web_driver(options):
    # return webdriver.Chrome("./chromedriver", chrome_options=options)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')

def set_chrome_profile(options, profile):
    options.add_argument(profile)

def set_logging_off(options):
    options.add_experimental_option('excludeSwitches', ['enable-logging'])