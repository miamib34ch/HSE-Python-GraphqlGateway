import pytest
from graphene.test import Client

from schema import schema


class TestQuery:
    """
    Тесты для схемы Query
    """

    place_id = None

    @pytest.fixture
    def client(self):
        """
        Фикстура для получения клиента
        """
        return Client(schema)

    @pytest.fixture(scope="class")
    def places_id(self):
        """
        Фикстура для получения идентификатора объекта любимого места
        """
        places_ids = []
        yield places_ids

    def test_query_create_place(self, client, places_id):
        """
        Тестирование метода create_place
        """
        result = client.execute(
            """
            mutation {
                createPlace(
                    latitude: 1,
                    longitude: 1,
                    description: "Описание"
                ) {
                    result
                    place {
                        id
                        latitude
                        longitude
                        description
                    }
                }
            }
            """
        )
        assert result["data"]["createPlace"]["result"] is True
        assert result["data"]["createPlace"]["place"]["id"] is not None
        assert result["data"]["createPlace"]["place"]["latitude"] == 1
        assert result["data"]["createPlace"]["place"]["longitude"] == 1
        assert result["data"]["createPlace"]["place"]["description"] == "Описание"

    def test_query_resolve_places(self, client):
        """
        Тестирование метода resolve_places
        """
        result = client.execute(
            """
            query {
                places {
                    id
                    latitude
                    longitude
                    description
                }
            }
            """
        )

        assert result["data"]["places"][-1]["id"] is not None
        assert result["data"]["places"][-1]["latitude"] == 1
        assert result["data"]["places"][-1]["longitude"] == 1
        assert result["data"]["places"][-1]["description"] == "Описание"
