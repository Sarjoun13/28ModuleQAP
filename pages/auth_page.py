from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    email = WebElement(id='username')
    password = WebElement(id='password')
    btn = WebElement(id='kc-login')
    registration_btn = WebElement(id='kc-register')
    forgot_password_btn = WebElement(id='forgot_password')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    captcha = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/img[1]')
    captcha_input = WebElement(id='captcha')
    btn_continue = WebElement(id='reset')
    reset_back = WebElement(id='reset-back')