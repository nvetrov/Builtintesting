# TASK_ID = 1
# TASK_TEXT = "text text"
# TASKS = {TASK_ID: TASK_TEXT}


def get_task(_id):
    if _id in TASKS:
        return TASKS[_id]
