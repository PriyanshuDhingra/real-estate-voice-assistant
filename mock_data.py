from state import Listing


LISTINGS: list[Listing] = [
    {
        "id": "APT-101",
        "property_type": "apartment",
        "city": "Brooklyn",
        "neighborhood": "Williamsburg",
        "title": "Sunny one-bedroom near Domino Park",
        "price_per_month": 3200,
        "bedrooms": 1,
    },
    {
        "id": "APT-102",
        "property_type": "apartment",
        "city": "Brooklyn",
        "neighborhood": "Williamsburg",
        "title": "Two-bedroom loft with roof access",
        "price_per_month": 4650,
        "bedrooms": 2,
    },
    {
        "id": "APT-103",
        "property_type": "apartment",
        "city": "Brooklyn",
        "neighborhood": "Park Slope",
        "title": "Quiet garden-level two-bedroom",
        "price_per_month": 3900,
        "bedrooms": 2,
    },
    {
        "id": "HOME-201",
        "property_type": "house",
        "city": "Austin",
        "neighborhood": "Zilker",
        "title": "Three-bedroom home close to Barton Springs",
        "price_per_month": 4800,
        "bedrooms": 3,
    },
    {
        "id": "WORK-301",
        "property_type": "workspace",
        "city": "New York",
        "neighborhood": "SoHo",
        "title": "Private six-desk studio workspace",
        "price_per_month": 2900,
        "bedrooms": 0,
    },
]


def find_listings(
    property_type: str, city: str, neighborhood: str
) -> list[Listing]:
    """A deterministic stand-in for a future property-search API."""

    return [
        listing
        for listing in LISTINGS
        if listing["property_type"] == property_type
        and listing["city"].casefold() == city.casefold()
        and listing["neighborhood"].casefold() == neighborhood.casefold()
    ]
