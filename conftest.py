import pytest
from endpoints.auth import Auth
from endpoints.auth_token import AuthAlive
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.get_many import GetManyMeme
from endpoints.get_one import GetOneMeme
from endpoints.delete_meme import DeleteMeme
from data import CREATE_PAYLOAD


@pytest.fixture()
def auth_endpoint():
    return Auth()


@pytest.fixture(scope="session")
def authorized():
    auth = Auth()
    auth.new_auth(payload={"name": "Nikolay"})
    return auth


@pytest.fixture(scope="session")
def token(authorized):
    return authorized.json['token']


@pytest.fixture(scope="session")
def username(authorized):
    return authorized.json["user"]


@pytest.fixture()
def auth_alive_token_endpoint():
    return AuthAlive()


@pytest.fixture()
def create_meme_endpoint(token):
    return CreateMeme(token=token)


@pytest.fixture()
def create_meme_endpoint_no_token():
    return CreateMeme()


@pytest.fixture()
def update_meme_endpoint(token):
    return UpdateMeme(token=token)


@pytest.fixture()
def update_meme_endpoint_no_token():
    return UpdateMeme()


@pytest.fixture()
def get_many_meme_endpoint(token):
    return GetManyMeme(token=token)


@pytest.fixture()
def get_many_meme_endpoint_no_token():
    return GetManyMeme()


@pytest.fixture()
def get_one_meme_endpoint(token):
    return GetOneMeme(token=token)


@pytest.fixture()
def get_one_meme_endpoint_no_token():
    return GetOneMeme()


@pytest.fixture()
def delete_meme_endpoint(token):
    return DeleteMeme(token=token)


@pytest.fixture()
def delete_meme_endpoint_no_token():
    return DeleteMeme()


@pytest.fixture()
def create_test_meme(create_meme_endpoint, token):
    create_meme_endpoint.create_new_meme(payload=CREATE_PAYLOAD)
    meme_id = create_meme_endpoint.json["id"]

    yield meme_id

    delete_endpoint = DeleteMeme(token=token)
    delete_endpoint.delete_meme(meme_id)
