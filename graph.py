from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from mock_data import find_listings
from state import RealEstateState


PROPERTY_TYPES = ("apartment", "house", "workspace")


def _normalized_match(message: str, choices: tuple[str, ...]) -> str | None:
    message = message.casefold()
    return next((choice for choice in choices if choice in message), None)


def welcome(_: RealEstateState) -> dict:
    return {
        "phase": "awaiting_property_type",
        "assistant_message": (
            "Welcome to HomeFinder. What type of property would you like to see: "
            "an apartment, house, or workspace?"
        ),
    }


def listings_presented(_: RealEstateState) -> dict:
    return {
        "assistant_message": (
            "I have already shown the matching listings. Type 'restart' to begin "
            "a new search; appointment selection will be added in the next milestone."
        )
    }


def collect_property_type(state: RealEstateState) -> dict:
    property_type = _normalized_match(state["user_message"], PROPERTY_TYPES)
    if property_type is None:
        return {
            "assistant_message": "Please choose one: apartment, house, or workspace."
        }
    return {
        "property_type": property_type,
        "phase": "awaiting_city",
        "assistant_message": "Great. Which city would you like to search in?",
    }


def collect_city(state: RealEstateState) -> dict:
    city = state["user_message"].strip()
    if not city:
        return {"assistant_message": "Please tell me the city you have in mind."}
    return {
        "city": city.title(),
        "phase": "awaiting_neighborhood",
        "assistant_message": "Which neighbourhood in that city interests you?",
    }


def collect_neighborhood_and_search(state: RealEstateState) -> dict:
    neighborhood = state["user_message"].strip()
    if not neighborhood:
        return {"assistant_message": "Please tell me the neighbourhood you prefer."}

    normalized_neighborhood = neighborhood.title()
    listings = find_listings(
        state["property_type"], state["city"], normalized_neighborhood
    )
    if not listings:
        return {
            "neighborhood": normalized_neighborhood,
            "listings": [],
            "phase": "awaiting_neighborhood",
            "assistant_message": (
                f"I could not find {state['property_type']} listings in "
                f"{normalized_neighborhood}, {state['city']}. "
                "Please try another neighbourhood."
            ),
        }

    formatted_listings = "\n".join(
        f"{index}. {listing['title']} — ${listing['price_per_month']:,}/month "
        f"({listing['bedrooms']} bedrooms, ID {listing['id']})"
        for index, listing in enumerate(listings, start=1)
    )
    return {
        "neighborhood": normalized_neighborhood,
        "listings": listings,
        "phase": "listings_presented",
        "assistant_message": (
            f"I found {len(listings)} option(s) in {normalized_neighborhood}:\n"
            f"{formatted_listings}\n\n"
            "Appointment selection is the next milestone. Type 'restart' to search again."
        ),
    }


def route_turn(state: RealEstateState) -> str:
    return state.get("phase", "awaiting_property_type")


def build_graph():
    """Compile a graph that processes exactly one customer turn at a time."""

    graph = StateGraph(RealEstateState)
    graph.add_node("welcome", welcome)
    graph.add_node("collect_property_type", collect_property_type)
    graph.add_node("collect_city", collect_city)
    graph.add_node("collect_neighborhood_and_search", collect_neighborhood_and_search)
    graph.add_node("listings_presented", listings_presented)

    graph.add_conditional_edges(
        START,
        route_turn,
        {
            "new": "welcome",
            "awaiting_property_type": "collect_property_type",
            "awaiting_city": "collect_city",
            "awaiting_neighborhood": "collect_neighborhood_and_search",
            "listings_presented": "listings_presented",
        },
    )
    graph.add_edge("welcome", END)
    graph.add_edge("collect_property_type", END)
    graph.add_edge("collect_city", END)
    graph.add_edge("collect_neighborhood_and_search", END)
    graph.add_edge("listings_presented", END)

    return graph.compile()
