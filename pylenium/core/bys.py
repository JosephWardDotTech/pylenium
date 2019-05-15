from typing import Tuple
from selenium.webdriver.common.by import By


def X(expression: str) -> Tuple:
    return By.XPATH, expression


def XPATH(expression: str) -> Tuple:
    return X(expression)


def CSS(expression: str) -> Tuple:
    return By.CSS_SELECTOR(expression)


def LT(text: str) -> Tuple:
    return By.LINK_TEXT(text)


def LINK_TEXT(text: str) -> Tuple:
    return LT(text)


def PTL(text: str) -> Tuple:
    return By.LINK_TEXT(text)


def PARTIAL_LINK_TEXT(text: str) -> Tuple:
    return LT(text)


def CLASS(class_name: str) -> Tuple:
    return By.CLASS_NAME(class_name)


def NAME(name: str) -> Tuple:
    return By.NAME(name)


def TAG(tag_name: str) -> Tuple:
    return By.TAG_NAME(tag_name)


def ID(unique_id: str) -> Tuple:
    return By.ID(unique_id)
