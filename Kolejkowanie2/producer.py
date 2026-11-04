
import sqlite3
import uuid
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "queue.db"
TASK_COUNT = 100


def create_tasks():
    with sqlite3.connect(DB_FILE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        tasks = [
            (str(uuid.uuid4()), "Phone call", "pending")
            for _ in range(TASK_COUNT)
        ]

        connection.executemany(
            "INSERT INTO tasks (id, name, status) VALUES (?, ?, ?)",
            tasks
        )

    print(f"Added {TASK_COUNT} tasks to the queue")


if __name__ == "__main__":
    create_tasks()
