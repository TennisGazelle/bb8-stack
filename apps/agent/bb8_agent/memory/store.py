from __future__ import annotations

import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class EventStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS summaries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created_at TEXT NOT NULL,
                    summary TEXT NOT NULL
                )
                """
            )

    def append_event(self, event_type: str, payload: dict[str, Any]) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO events(created_at, event_type, payload_json) VALUES (?, ?, ?)",
                (datetime.now(UTC).isoformat(), event_type, json.dumps(payload, sort_keys=True)),
            )

    def append_summary(self, summary: str) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO summaries(created_at, summary) VALUES (?, ?)",
                (datetime.now(UTC).isoformat(), summary),
            )
