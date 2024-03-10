from typing import Optional

from pydantic import BaseModel, Field

from src.models.mixins import TimeStampMixin


class PlaceModel(TimeStampMixin, BaseModel):
    """
    Модель для описания места.
    """

    id: Optional[int] = Field(title="Идентификатор")
    latitude: float = Field(title="Широта")
    longitude: float = Field(title="Долгота")
    description: str = Field(title="Описание")
    country: Optional[str] = Field(title="ISO Alpha2-код страны")
    city: Optional[str] = Field(title="Название города")
    locality: Optional[str] = Field(title="Местонахождение")


class UpdatePlaceModel(TimeStampMixin, BaseModel):
    """
    Модель для обновления места.
    """

    latitude: float | None = Field(title="Широта")
    longitude: float | None = Field(title="Долгота")
    description: str | None = Field(title="Описание")
