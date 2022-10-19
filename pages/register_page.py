#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    registration_btn = WebElement(id='kc-register')

    first_name_input = WebElement(name='firstName')

    last_name_input = WebElement(name='lastName')

    email_input = WebElement(id='address')

    password_input = WebElement(id='password')

    password_confirm_input = WebElement(id='password-confirm')

    register_btn = WebElement(name='register')

