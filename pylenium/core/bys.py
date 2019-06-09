from typing import Tuple
from selenium.webdriver.common.by import By


def x(expression: str) -> Tuple:
    return By.XPATH, expression


def xpath(expression: str) -> Tuple:
    return x(expression)


def css(expression: str) -> Tuple:
    return By.CSS_SELECTOR(expression)


def link_text(text: str) -> Tuple:
    return By.LINK_TEXT(text)


def partial_link_text(text: str) -> Tuple:
    return By.LINK_TEXT(text)


def clazz(class_name: str) -> Tuple:
    return By.CLASS_NAME(class_name)


def name(name: str) -> Tuple:
    return By.NAME(name)


def tag(tag_name: str) -> Tuple:
    return By.TAG_NAME(tag_name)


def identity(unique_id: str) -> Tuple:
    return By.ID(unique_id)
