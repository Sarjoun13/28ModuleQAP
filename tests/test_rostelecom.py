#py -m pytest -v --driver Chrome --driver-path driver.exe

import time
import pytest
from pages.auth_page import AuthPage
from pages.register_page import MainPage
from pages.auth_page_with_code import AuthPageWithCode
from config import TestData

def test_main_page_all_items(web_browser):
    page = AuthPage(web_browser)

    assert page.email.is_visible()
    assert page.password.is_visible()
    assert page.btn.is_visible()
    assert page.registration_btn.is_visible()
    assert page.forgot_password_btn.is_visible()
    assert page.tab_email.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_phone.is_visible()
    assert page.tab_ls.is_visible()


def test_positive_registration1(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password001)
    page.password_confirm_input.send_keys(TestData.password001)

    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_positive_registration2(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive2)
    page.last_name_input.send_keys(TestData.last_name_positive2)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password001)
    page.password_confirm_input.send_keys(TestData.password001)

    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_password_recovery(web_browser):
    page = AuthPage(web_browser)

    page.forgot_password_btn.click()

    assert page.email.is_presented()
    assert page.captcha.is_presented()
    assert page.captcha_input.is_presented()
    assert page.btn_continue.is_presented()


def test_positive_authorisation_email(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys(TestData.valid_email)
    page.password.send_keys(TestData.password002)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_positive_authorisation_phone(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys(TestData.valid_phone)
    page.password.send_keys(TestData.password002)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_positive_authorisation_with_code(web_browser):
    page = AuthPageWithCode(web_browser)

    page.email.send_keys(TestData.valid_email)
    page.btn_code.click()
    time.sleep(2)
    assert page.code0.is_presented()
    assert page.code1.is_presented()
    assert page.code2.is_presented()
    assert page.code3.is_presented()
    assert page.code4.is_presented()
    assert page.code5.is_presented()


def test_repeat_code_for_authorisation(web_browser):
    page = AuthPageWithCode(web_browser)

    page.email.send_keys(TestData.valid_email)
    page.btn_code.click()
    time.sleep(125)
    page.repeat_code.click()
    time.sleep(5)

    assert page.timeout_input_code.is_visible()


def test_reset_button(web_browser):
    page = AuthPage(web_browser)

    page.forgot_password_btn.click()

    assert page.reset_back.is_clickable()

    page.reset_back.click()

    assert 'https://b2c.passport.rt.ru' in page.get_current_url()


def test_negative_authorisation_email(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys(TestData.invalid_email)
    page.password.send_keys(TestData.password002)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()



def test_negative_authorisation_phone(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys(TestData.valid_phone)
    page.password.send_keys(TestData.empty_password)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()


def test_negative_authorisation_short_password(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.short_password)
    page.password_confirm_input.send_keys(TestData.short_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()


def test_negative_authorisation_lowercase_password(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.lowercase_password)
    page.password_confirm_input.send_keys(TestData.lowercase_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароль должен содержать хотя бы одну заглавную букву' in page.get_page_source()


def test_negative_authorisation_cyrillic_password(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.cyrillic_password)
    page.password_confirm_input.send_keys(TestData.cyrillic_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароль должен содержать только латинские буквы' in page.get_page_source()


def test_negative_authorisation_different_passwords(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password001)
    page.password_confirm_input.send_keys(TestData.password002)
    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароли не совпадают' in page.get_page_source()


def test_negative_authorisation_non_unique_email(web_browser):
    page = MainPage(web_browser)

    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name_positive1)
    page.last_name_input.send_keys(TestData.last_name_positive1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password003)
    page.password_confirm_input.send_keys(TestData.password003)
    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Учётная запись уже существует' in page.get_page_source()