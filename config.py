import os

from dotenv import load_dotenv

load_dotenv()

URL = 'https://proxy6.net/'
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

XPATH_LOGIN = "//*[@data-role='login']"
XPATH_USER = "//div[@class='block']//input[@name='email']"
XPATH_PASSWORD = "//div[@class='block']//input[@name='password']"
XPATH_CAPTCHA = "//iframe[@title='reCAPTCHA']"
CSS_CAPTCHA = "div.recaptcha-checkbox-border"

XPATH_USER_PROFILE = "//div[@class='wrap clearfix']"\
        "//a[@href='https://proxy6.net/user/proxy']"

IP_PORT = "//div[@class='right clickselect ']"
DATE = "//div[@class='right color-warning']"
URL_USER = 'https://proxy6.net/user/proxy'

ELEM_BALANCE = "//*[@id='notepad-toggle']"
