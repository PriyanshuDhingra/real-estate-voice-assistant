# Real Estate Voice Agent (text-first prototype)

This project begins as a terminal chat application. It proves the core real-estate workflow before adding a phone provider, speech-to-text, calendars, or a production database.

## What works

1. The assistant welcomes the customer.
2. It collects a property type.
3. It collects city and neighbourhood, one at a time when necessary.
4. It searches a small mock property catalogue and presents matching listings.
5. The user can start a new search with `restart`.

## Setup

From PowerShell:

```powershell
cd C:\Projects\real-estate-voice-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Explore the workflow

Open [notebooks/graph.ipynb](notebooks/graph.ipynb) in VS Code or Jupyter to
run the graph step by step and visualize its structure while you learn.

Try this conversation:

```text
I want an apartment
Brooklyn
Williamsburg
restart
```

## Why text first?

The graph and data tools are the business core. A voice provider will later turn call audio into text before invoking this same graph, and turn its replies back into speech.

## Next milestones

1. Add selection of one or more shown listings.
2. Add a mock realtor calendar and available viewing slots.
3. Add an appointment confirmation and conflict-safe booking service.
4. Persist threads with a SQLite checkpointer, then PostgreSQL.
5. Add FastAPI and an inbound-call/STT/TTS adapter.
