from __future__ import annotations

from typing import Literal, TypedDict


PropertyType = Literal["apartment", "house", "workspace"]


class Listing(TypedDict):
    id: str
    property_type: PropertyType
    city: str
    neighborhood: str
    title: str
    price_per_month: int
    bedrooms: int


class RealEstateState(TypedDict, total=False):
    """The small, structured memory shared by every graph node."""

    phase: str
    user_message: str
    assistant_message: str
    property_type: PropertyType | None
    city: str | None
    neighborhood: str | None
    listings: list[Listing]
