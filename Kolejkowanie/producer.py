import csv
import os
import uuid
from filelock import FileLock

QUEUE_FILE = "queue.csv"
LOCK_FILE = "queue.csv.lock"


def create_task():
    task = {"id": str(uuid.uuid4()), "name": "Phone call", "status": "pending"}

    lock = FileLock(LOCK_FILE)

    with lock:
        file_exists = os.path.exists(QUEUE_FILE)

        with open(QUEUE_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "name", "status"]
            )

            if not file_exists or os.path.getsize(QUEUE_FILE) == 0:
                writer.writeheader()

            writer.writerow(task)

    print(f"Task added: {task['id']}")


if __name__ == "__main__":
    create_task()