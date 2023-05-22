import pytest
from selenium import webdriver

from api.api_users import GetUsers, PostUsers, UpdateUsers, DeleteUsers
from api.api_resource import GetResource
from api.api_register import PostRegister
from api.api_login import PostLogin

from web.web_elements import ButtonExample, ResExample


"""Fixture for API"""
@pytest.fixture(scope="session")
def get_users():
    get_users = GetUsers()
    return get_users


@pytest.fixture(scope="session")
def get_resource():
    get_resource = GetResource()
    return get_resource


@pytest.fixture(scope="session")
def post_user():
    post_user = PostUsers()
    return post_user


@pytest.fixture(scope="session")
def post_register():
    post_register = PostRegister()
    return post_register


@pytest.fixture(scope="session")
def post_login():
    post_login = PostLogin()
    return post_login


@pytest.fixture(scope="session")
def update_user():
    update_user = UpdateUsers()
    return update_user


@pytest.fixture(scope="session")
def delete_users():
    delete_users = DeleteUsers()
    return delete_users


"""Fixture for WEB"""
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def button_example(browser):
    button_example = ButtonExample(browser)
    return button_example


@pytest.fixture(scope="session")
def res_example(browser):
    res_example = ResExample(browser)
    return res_example

