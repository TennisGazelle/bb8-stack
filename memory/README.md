# Memory

Milestone 0 uses SQLite as the authoritative event log.

The database is created at runtime from the Python `EventStore`. `schema.sql` records the intended shape for humans and migrations.
