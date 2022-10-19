from pages.base import WebPage
from pages.elements import WebElement


class AuthPageWithCode(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://my.rt.ru/'
        super().__init__(web_driver, url)

    email = WebElement(id='address')

    code0 = WebElement(id='rt-code-0')
    code1 = WebElement(id='rt-code-1')
    code2 = WebElement(id='rt-code-2')
    code3 = WebElement(id='rt-code-3')
    code4 = WebElement(id='rt-code-4')
    code5 = WebElement(id='rt-code-5')

    btn_code = WebElement(id='otp_get_code')

    standard_auth_btn = WebElement(id='standard_auth_btn')

    repeat_code = WebElement(css_selector='button.code-input-container__resend')

    timeout_input_code = WebElement(css_selector='span.code-input-container__timeout')

    reset_back = WebElement(id='reset-back')