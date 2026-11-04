import csv
import time
from filelock import FileLock

QUEUE_FILE = "queue.csv"
LOCK_FILE = "queue.csv.lock"

INTERVAL = 5
TASK_TIME = 30


def get_task():
    lock = FileLock(LOCK_FILE)

    with (lock):
        with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as file:
            tasks = list(csv.DictReader(file))

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "in_progress"

                with open(QUEUE_FILE, "w", newline="", encoding="utf-8"
                          ) as file:
                    writer = csv.DictWriter(
                        file,
                        fieldnames=["id", "name", "status"]
                    )
                    writer.writeheader()
                    writer.writerows(tasks)

                return task

    return None


def finish_task(task_id):
    lock = FileLock(LOCK_FILE)

    with lock:
        with open(QUEUE_FILE, "r", newline="", encoding="utf-8") as file:
            tasks = list(csv.DictReader(file))

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                break

        with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "name", "status"]
            )
            writer.writeheader()
            writer.writerows(tasks)


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