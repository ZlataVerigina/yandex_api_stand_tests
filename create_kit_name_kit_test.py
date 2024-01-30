import sender_stand_request
import data


# Получить тело запроса для создания нового набора
def get_kit_body(name):
    return {"name": name}


# Создать нового пользователя и получить его токен
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


# Проверка для валидных значений
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


# Проверка для невалидных значений
def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400


# Чек-лист:

def test_1_1symbol():
    positive_assert(get_kit_body("a"))


def test_2_511symbol():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))


def test_3_0symbol():
    negative_assert_code_400(get_kit_body(""))


def test_4_512symbol():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))


def test_5_eng():
    positive_assert(get_kit_body("QWErty"))


def test_6_rus():
    positive_assert(get_kit_body("Злата"))


def test_7_special():
    positive_assert(get_kit_body("\"№%@\","))


def test_8_space():
    positive_assert(get_kit_body(" Человек и КО "))


def test_9_number():
    positive_assert(get_kit_body("123"))


def test_10_empty():
    negative_assert_code_400({})


def test_11_wrong_type():
    negative_assert_code_400({"name": 123})