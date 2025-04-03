import requests

users_link = "https://reqres.in/api/users"
user2 = "https://reqres.in/api/users/2"
register_link = "https://reqres.in/api/register"
login_link = "https://reqres.in/api/login"

page2 = {'page': 2}
delayed = {'delay': 3}
valid_login = {"email": "george.bluth@reqres.in", "password": "test"}
valid_reg = {"name": "paul rudd", **valid_login}
update_user = {"name": "test test"}


def test_get_users_list():
    resp = requests.get(users_link, params=page2)
    assert resp.status_code == 200, f"Error: {resp.status_code}, data={resp.json()}"


def test_get_single_user():
    resp = requests.get(user2)
    assert resp.status_code == 200, f"Error: {resp.status_code}, data={resp.json()}"


def test_register():
    resp = requests.post(register_link, data=valid_reg)
    assert resp.status_code == 200, f"Error: {resp.status_code}, data={resp.json()}"


def test_login():
    resp = requests.post(login_link, data=valid_login)
    assert resp.status_code == 200, f"Error: {resp.status_code}, data={resp.json()}"


def test_update_user():
    resp = requests.patch(user2, data=update_user)
    assert resp.status_code == 200, f"Error: {resp.status_code}, data={resp.json()}"


def test_delete_user():
    resp = requests.delete(user2)
    assert resp.status_code == 204, f"Error: got status code {resp.status_code} instead of 204"
