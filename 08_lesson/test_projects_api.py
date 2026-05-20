import pytest
from api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()


@pytest.fixture
def new_project(api):
    data = {
        "title": "Тестовый проект"
    }
    response = api.post("/api-v2/projects", data)

    if response.status_code != 201:
        pytest.skip(f"Не удалось создать проект: {response.status_code} - {response.text}")

    project_id = response.json().get("id")
    yield project_id


#  POST /api-v2/projects

"""Позитивный тест: создаем проект с корректными данными"""
def test_create_project_positive(api):
    data = {
        "title": "Мой проект"
    }
    response = api.post("/api-v2/projects", data)

    assert response.status_code == 201
    assert "id" in response.json()

"""Негативный тест: создаем проект без названия"""
def test_create_project_negative_no_title(api):
    data = {}
    response = api.post("/api-v2/projects", data)

    assert response.status_code == 400
    assert "title should not be empty" in response.text


def test_create_project_negative_empty_title(api):
    """Негативный тест: создаем проект с пустым названием"""
    data = {
        "title": ""
    }
    response = api.post("/api-v2/projects", data)

    assert response.status_code == 400


#  PUT /api-v2/projects/{id}

"""Позитивный тест: обновляем название проекта"""
def test_update_project_positive(api, new_project):
    data = {
        "title": "Проект, проект"
    }
    response = api.put(f"/api-v2/projects/{new_project}", data)

    assert response.status_code == 200

"""Позитивный тест: обновляем название проекта"""
def test_update_project_negative_wrong_id(api):
    data = {
        "title": "Проет Х"
    }
    response = api.put("/api-v2/projects/00000000-0000-0000-0000-000000000000", data)

    assert response.status_code == 404

"""Негативный тест: обновляем без данных"""
def test_update_project_negative_no_data(api, new_project):
    response = api.put(f"/api-v2/projects/{new_project}", {})

    assert response.status_code == 200


#  GET /api-v2/projects/{id}

"""Позитивный тест: получаем созданный проект"""
def test_get_project_positive(api, new_project):
    response = api.get(f"/api-v2/projects/{new_project}")

    assert response.status_code == 200
    assert response.json()["id"] == new_project

"""Негативный тест: получаем несуществующий проект"""
def test_get_project_negative_wrong_id(api):
    response = api.get("/api-v2/projects/11111111-1111-1111-1111-111111111111")

    assert response.status_code == 404

"""Негативный тест: передаем кривой id"""
def test_get_project_negative_invalid_id(api):
    response = api.get("/api-v2/projects/123")

    assert response.status_code == 404