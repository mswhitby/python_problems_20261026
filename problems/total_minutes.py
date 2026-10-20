def total_minutes(tasks, include_paused=True):
    total = 0
    for task in tasks:
        total += task["minutes"]
    return total