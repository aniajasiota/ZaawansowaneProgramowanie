
import sqlite3
import time
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "queue.db"

INTERVAL = 5
TASK_TIME = 30


def get_task():
    with sqlite3.connect(DB_FILE, timeout=30) as connection:
        connection.execute("BEGIN IMMEDIATE")

        task = connection.execute("""
            SELECT id, name, status
            FROM tasks
            WHERE status = 'pending'
            ORDER BY rowid
            LIMIT 1
        """).fetchone()

        if task is None:
            return None

        connection.execute("""
            UPDATE tasks
            SET status = 'in_progress'
            WHERE id = ?
        """, (task[0],))

        return {
            "id": task[0],
            "name": task[1],
            "status": "in_progress"
        }


def finish_task(task_id):
    with sqlite3.connect(DB_FILE, timeout=30) as connection:
        connection.execute("""
            UPDATE tasks
            SET status = 'done'
            WHERE id = ?
        """, (task_id,))


def execute_task(task):
    print(f"[START] Task: {task['id']}")

    time.sleep(TASK_TIME)

    finish_task(task["id"])

    print(f"[DONE] Task: {task['id']}")


def consumer():
    print("Consumer started")

    while True:
        task = get_task()

        if task:
            execute_task(task)
        else:
            print("No more tasks in queue")
            time.sleep(INTERVAL)


if __name__ == "__main__":
    consumer()
