from __future__ import annotations

from graph import build_graph
from state import RealEstateState


def initial_state() -> RealEstateState:
    return {
        "phase": "new",
        "property_type": None,
        "city": None,
        "neighborhood": None,
        "listings": [],
    }


def run() -> None:
    app = build_graph()
    state = initial_state()

    greeting = app.invoke(state)
    state.update(greeting)
    print(f"\nAgent: {greeting['assistant_message']}")

    while True:
        user_message = input("\nYou: ").strip()
        if user_message.casefold() in {"quit", "exit"}:
            print("Agent: Goodbye!")
            return
        if user_message.casefold() == "restart":
            state = initial_state()
            greeting = app.invoke(state)
            state.update(greeting)
            print(f"Agent: {greeting['assistant_message']}")
            continue

        state["user_message"] = user_message
        update = app.invoke(state)
        state.update(update)
        print(f"Agent: {state['assistant_message']}")


if __name__ == "__main__":
    run()
