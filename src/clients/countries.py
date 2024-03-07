from typing import Optional
from urllib.parse import urljoin

from src.clients.base.base import BaseClient
from src.models.countries import CountryModel
from src.settings import settings


class CountriesClient(BaseClient):
    """
    Реализация функций для получения информации о странах.
    """

    @property
    def base_url(self) -> str:
        return settings.service.countries_informer.base_url

    def get_list_by_codes(self, alpha2codes: set[str]) -> Optional[list[CountryModel]]:
        """
        Получение списка стран с фильтрацией по ISO Alpha2-кодам.
        TODO: добавить пагинацию.

        :param alpha2codes: Множество ISO Alpha2-кодов стран
        :return:
        """

        endpoint = "/api/v1/country"

        query_params = ""
        for code in alpha2codes:
            query_params += f"codes={code.lower()}&"

        query_params = query_params.rstrip("&")
        url = urljoin(
            self.base_url,
            f"{endpoint}?{query_params}",
        )
        if response := self._request(self.GET, url):
            return [
                CountryModel(
                    name=country.get("name"),
                    alpha2code=country.get("alpha2code"),
                    alpha3code=country.get("alpha3code"),
                    capital=country.get("capital"),
                    region=country.get("region"),
                    subregion=country.get("subregion"),
                    population=country.get("population"),
                    latitude=country.get("latitude"),
                    longitude=country.get("longitude"),
                    demonym=country.get("demonym"),
                    area=country.get("area"),
                    numeric_code=country.get("numeric_code"),
                    flag=country.get("flag"),
                    currencies=country.get("currencies"),
                    languages=country.get("languages"),
                )
                for country in response.get("results", [])
            ]

        return None
