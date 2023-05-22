import json
import time


def test_button_list_users(button_example, get_users, res_example):
    """Кнопка 'List Users', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_users.list_users(page=2, per_page="")
    button_example.go_to_site()
    button_example.window() # делаем окно во весь экран
    button_example.scroll(x=0, y=1200) # скролим экран
    button_example.click_button_to_users()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_single_users(button_example, get_users, res_example):
    """Кнопка 'Single Users', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_users.single_users(user_id=2)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_single_users()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_single_users_not_found(button_example, get_users, res_example):
    """Кнопка 'Single Users Not Found', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_users.single_users(user_id=23)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_single_users_nf()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_list_resource(button_example, get_resource, res_example):
    """Кнопка 'List resource', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_resource.list_resource(resource="unknown")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_list_resource()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_single_resource(button_example, get_resource, res_example):
    """Кнопка 'Single resource', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_resource.single_resource(resource="unknown", r_id=2)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_single_resource()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_single_resource_not_found(button_example, get_resource, res_example):
    """Кнопка 'Single resource not found', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_resource.single_resource(resource="unknown", r_id=23)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_single_resource_nf()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_create(button_example, post_user, res_example):
    """Кнопка 'Create', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = post_user.create_new_user(name="morpheus", job="leader")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_create()
    time.sleep(1)
    print(status)
    print(result)
    print(json.loads(res_example.check_response_body()))
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result
    """Новый пользователь создаётся с другим ID. Не думаю, что это баг"""


def test_button_update_put(button_example, update_user, res_example):
    """Кнопка 'Update put', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = update_user.update_user_put(user_id=2, name="morpheus", job="zion resident")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_update_put()
    time.sleep(1)
    print(status)
    print(result)
    print(json.loads(res_example.check_response_body()))
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result
    """В 'updatedAt' записывается разные значения, так как один запрос
    делается на несколько секунд раньше другого. Это не баг"""


def test_button_update_patch(button_example, update_user, res_example):
    """Кнопка 'Update patch', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = update_user.update_user_patch(user_id=2, name="morpheus", job="zion resident")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_update_patch()
    time.sleep(1)
    print(status)
    print(result)
    print(json.loads(res_example.check_response_body()))
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result
    """В 'updatedAt' записывается разные значения, так как один запрос
    делается на несколько секунд раньше другого. Это не баг"""


def test_button_delete(button_example, delete_users, res_example):
    """Кнопка 'Delete', сравнение статус-кода и тела ответа образца с API запроса"""
    status = delete_users.delete(user_id=2)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_delete()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    """Тело запроса отсутствует, поэтому нет проверки"""


def test_button_register_successful(button_example, post_register, res_example):
    """Кнопка 'Register successful', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = post_register.register(email="eve.holt@reqres.in", password="pistol")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_register_succes()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_register_unsuccessful(button_example, post_register, res_example):
    """Кнопка 'Register unsuccessful', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = post_register.register(email="sydney@fife", password="")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1200)
    button_example.click_button_to_register_unsucces()
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_login_successful(button_example, post_login, res_example):
    """Кнопка 'login successful', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = post_login.login(email="eve.holt@reqres.in", password="cityslicka")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1400)
    button_example.click_button_to_login_succes()
    time.sleep(1)
    button_example.scroll(x=0, y=-200)
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_login_unsuccessful(button_example, post_login, res_example):
    """Кнопка 'login unsuccessful', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = post_login.login(email="peter@klaven", password="")
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1400)
    button_example.click_button_to_login_unsucces()
    time.sleep(1)
    button_example.scroll(x=0, y=-200)
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result


def test_button_delayed_response(button_example, get_users, res_example):
    """Кнопка 'Delayed response', сравнение статус-кода и тела ответа образца с API запроса"""
    status, result = get_users.delayed_response(delay=3)
    button_example.go_to_site()
    button_example.window()
    button_example.scroll(x=0, y=1500)
    button_example.click_button_to_delay_res()
    time.sleep(4)
    button_example.scroll(x=0, y=-300)
    time.sleep(1)
    assert res_example.check_response_code() == str(status)
    assert json.loads(res_example.check_response_body()) == result

