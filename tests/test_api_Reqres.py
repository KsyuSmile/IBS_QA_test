import pytest


def test_get_list_users(get_users, page=2, per_page=""):
    """Получение списка всех пользователей"""
    status, result = get_users.list_users(page, per_page)
    print(result)
    assert status == 200


def test_get_id_users_from_list(get_users, page=2, per_page=""):
    """Поиск пользователя по ID из списка. Для этого запрашиваем общий список
    пользователей. Если количество пользователей больше нуля, то запрашиваем первого из списка.
    Если пользователей нет, тогда тест завершается со статусом Failed"""
    _, all_users = get_users.list_users(page, per_page)
    user_id = all_users['data'][0]['id']
    status, result = get_users.single_users(user_id)

    print(status)
    print(result)
    assert status == 200


@pytest.mark.parametrize("user_id", [2, 1, 3])
def test_get_single_user(get_users, user_id):
    """Поиск пользователя по существующему ID"""
    status, result = get_users.single_users(user_id)
    print(status)
    print(result)
    assert status == 200


@pytest.mark.parametrize("user_id", [23, 88, 368])
def test_get_single_user_not_found(get_users, user_id):
    """Поиск пользователя по несуществующему ID,
    в ответе ждём код 404 и пустое тело ответа"""
    status, result = get_users.single_users(user_id)
    print(status)
    print(result)
    assert status == 404
    assert result == {}


def test_get_list_resource(get_resource, resource="unknown"):
    """Получаем список ресурсов"""
    status, result = get_resource.list_resource(resource)
    print(status)
    print(result)
    assert status == 200


def test_get_single_resource(get_resource, resource="unknown", r_id=2):
    """Поиск ресурса по существующему ID"""
    status, result = get_resource.single_resource(resource, r_id)
    print(status)
    print(result)
    assert status == 200


def test_get_single_resource_not_found(get_resource, resource="unknown", r_id=45):
    """Поиск ресурса по несуществующему ID,
    в ответе ждём код 404 и пустое тело ответа"""
    status, result = get_resource.single_resource(resource, r_id)
    print(status)
    print(result)
    assert status == 404
    assert result == {}


def test_post_new_users(post_user, name="morpheus", job="leader"):
    """Создаём нового пользователя, проверяем, что в теле ответа
    содержится ID, а имя равно введённому имени"""
    status, result = post_user.create_new_user(name, job)
    print(status)
    print(result)
    assert status == 201
    assert "id" in result
    assert result["name"] == name


def test_put_update_users(update_user, user_id=2, name="morpheus", job="zion resident"):
    """Изменяем данные пользователя методом PUT.
     Проверяем, что в теле ответа занесена дата изменения данных"""
    status, result = update_user.update_user_put(user_id, name, job)
    print(status)
    print(result)
    assert status == 200
    assert "updatedAt" in result


def test_patch_update_users(update_user, user_id=2, name="morpheus", job="zion resident"):
    """Изменяем данные пользователя методом PATCH.
     Проверяем, что в теле ответа занесена дата изменения данных"""
    status, result = update_user.update_user_patch(user_id, name, job)
    print(status)
    print(result)
    assert status == 200
    assert "updatedAt" in result


def test_delete_user(delete_users, user_id=2):
    """Удаление пользователя, проверяем, что возвращается статус-код 204"""
    status = delete_users.delete(user_id)
    print(status)
    assert status == 204


def test_post_register_successful(post_register, email="eve.holt@reqres.in", password="pistol"):
    """Регистрация с корректными данными,
    проверяем, что в теле ответа присутствует ID"""
    status, result = post_register.register(email, password)
    print(status)
    print(result)
    assert status == 200
    assert "id" in result


def test_post_register_unsuccessful(post_register, email="sydney@fife", password=""):
    """Регистрация без пароля, проверяем, что возвращается статус-код 400,
    а в теле ответа присутствует сообщение об ошибке"""
    status, result = post_register.register(email, password)
    print(status)
    print(result)
    assert status == 400
    assert "error" in result


def test_post_login_successful(post_login, email="eve.holt@reqres.in", password="cityslicka"):
    """Авторизация с корректными данными,
    проверяем, что в теле ответа присутствует token"""
    status, result = post_login.login(email, password)
    print(status)
    print(result)
    assert status == 200
    assert "token" in result


def test_post_login_unsuccessful(post_register, email="peter@klaven", password=""):
    """Авторизация без пароля, проверяем, что возвращается статус-код 400,
    а в теле ответа присутствует сообщение об ошибке"""
    status, result = post_register.register(email, password)
    print(status)
    print(result)
    assert status == 400
    assert "error" in result


@pytest.mark.parametrize("delay", [3, 5, 10])
def test_get_delayed_response(get_users, delay):
    """Получаем список пользователей с ожиданием в секундах"""
    status, result = get_users.delayed_response(delay)
    print(status)
    print(result)
    assert status == 200