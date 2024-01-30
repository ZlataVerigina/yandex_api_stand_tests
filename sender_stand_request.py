import configuration
import requests
import data


# Создать нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Создать новый набор для пользователя
def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT,
                         json=kit_body,
                         # Заголовок для авторизации пользователя по токену
                         headers=data.headers | {"Authorization": f"Bearer {auth_token}"})
