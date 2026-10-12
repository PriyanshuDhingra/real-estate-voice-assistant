from pathlib import Path
import sys

# Support both `python tests/test_graph.py` (including IDE Run File) and pytest.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from graph import build_graph


def test_happy_path_searches_williamsburg_apartments():
    app = build_graph()
    state = app.invoke({"phase": "new"})

    state.update(app.invoke({**state, "user_message": "An apartment, please"}))
    state.update(app.invoke({**state, "user_message": "Brooklyn"}))
    state.update(app.invoke({**state, "user_message": "Williamsburg"}))

    assert state["phase"] == "listings_presented"
    assert len(state["listings"]) == 2
    assert "Sunny one-bedroom" in state["assistant_message"]


if __name__ == "__main__":
    test_happy_path_searches_williamsburg_apartments()
    print("Happy-path graph test passed.")
