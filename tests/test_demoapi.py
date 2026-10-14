import pytest
from data import CREATE_PAYLOAD, INVALID_CREATE, UPDATE_PAYLOAD, INVALID_UPDATE


def test_post_auth(authorized):
    authorized.check_status_code_200()
    authorized.check_required_fields()
    authorized.check_fields_values({"user": "Nikolay"})
    authorized.check_fields_are_str(("token","user"))


def test_post_auth_no_name_field(auth_endpoint):
    auth_endpoint.new_auth(payload={})
    auth_endpoint.check_status_code_400()


def test_post_auth_number_name(auth_endpoint):
    auth_endpoint.new_auth(payload={"name": 123})
    auth_endpoint.check_status_code_400()


def test_get_auth(auth_alive_token_endpoint, token, username):
    auth_alive_token_endpoint.auth_token_alive(token)
    auth_alive_token_endpoint.check_status_code_200()
    auth_alive_token_endpoint.check_token_user(username)


def test_get_auth_invalid_token(auth_alive_token_endpoint):
    auth_alive_token_endpoint.auth_token_alive("invalid-token")
    auth_alive_token_endpoint.check_status_code_404()


def test_post_meme(create_meme_endpoint):
    create_meme_endpoint.create_new_meme(CREATE_PAYLOAD)
    create_meme_endpoint.check_status_code_200()
    create_meme_endpoint.check_meme_structure()
    create_meme_endpoint.check_fields_values({
        "text": CREATE_PAYLOAD["text"],
        "url": CREATE_PAYLOAD["url"],
    })


def test_create_meme_without_token(create_meme_endpoint_no_token):
    create_meme_endpoint_no_token.create_new_meme(CREATE_PAYLOAD)
    create_meme_endpoint_no_token.check_status_code_401()


@pytest.mark.parametrize("payload", INVALID_CREATE)
def test_create_meme_invalid_data(create_meme_endpoint, payload):
    create_meme_endpoint.create_new_meme(payload)
    create_meme_endpoint.check_status_code_400()


def test_get_all_meme(get_many_meme_endpoint, create_test_meme):
    meme_id = create_test_meme

    get_many_meme_endpoint.get_all_meme()
    get_many_meme_endpoint.check_status_code_200()
    get_many_meme_endpoint.check_meme_in_list(meme_id)


def test_get_all_meme_without_token(get_many_meme_endpoint_no_token):
    get_many_meme_endpoint_no_token.get_all_meme()
    get_many_meme_endpoint_no_token.check_status_code_401()


def test_get_one_meme(get_one_meme_endpoint, create_test_meme):
    meme_id = create_test_meme
    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_status_code_200()
    get_one_meme_endpoint.check_fields_values({"id": meme_id})


def test_get_one_meme_without_token(get_one_meme_endpoint_no_token, create_test_meme):
    meme_id = create_test_meme
    get_one_meme_endpoint_no_token.get_one_meme(meme_id)
    get_one_meme_endpoint_no_token.check_status_code_401()


def test_get_one_meme_not_found(get_one_meme_endpoint):
    get_one_meme_endpoint.get_one_meme(99999999)
    get_one_meme_endpoint.check_status_code_404()


def test_update_meme(update_meme_endpoint, create_test_meme):
    meme_id = create_test_meme
    payload = UPDATE_PAYLOAD.copy()
    payload["id"] = meme_id

    update_meme_endpoint.update_meme(meme_id, payload)
    update_meme_endpoint.check_status_code_200()
    update_meme_endpoint.check_meme_structure()
    update_meme_endpoint.check_fields_values({
        "id": meme_id,
        "text": UPDATE_PAYLOAD["text"],
        "url": UPDATE_PAYLOAD["url"],
        "tags": UPDATE_PAYLOAD["tags"],
        "info": UPDATE_PAYLOAD["info"],
        "updated_by": "Nikolay",
    })


def test_update_meme_without_token(update_meme_endpoint_no_token, create_test_meme):
    meme_id = create_test_meme
    payload = UPDATE_PAYLOAD.copy()
    payload["id"] = meme_id

    update_meme_endpoint_no_token.update_meme(meme_id, payload)
    update_meme_endpoint_no_token.check_status_code_401()


@pytest.mark.parametrize("payload", INVALID_UPDATE)
def test_update_meme_invalid_data(update_meme_endpoint, create_test_meme, payload):
    meme_id = create_test_meme
    payload = payload.copy()
    payload["id"] = meme_id

    update_meme_endpoint.update_meme(meme_id, payload)
    update_meme_endpoint.check_status_code_400()


def test_update_meme_not_found(update_meme_endpoint):
    payload = UPDATE_PAYLOAD.copy()
    payload["id"] = 99999999

    update_meme_endpoint.update_meme(99999999, payload)
    update_meme_endpoint.check_status_code_404()


def test_delete_meme(delete_meme_endpoint, get_one_meme_endpoint, create_test_meme):
    meme_id = create_test_meme
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_code_200()
    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_status_code_404()


def test_delete_meme_not_found(delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(99999999)
    delete_meme_endpoint.check_status_code_404()


def test_delete_meme_without_token(delete_meme_endpoint_no_token, create_test_meme):
    meme_id = create_test_meme
    delete_meme_endpoint_no_token.delete_meme(meme_id)
    delete_meme_endpoint_no_token.check_status_code_401()
