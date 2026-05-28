def list_routines(routine_store):
    return routine_store


def start_routine(routine_store, routine_id):
    if routine_id not in routine_store:
        raise ValueError(f"Routine not found: {routine_id}")

    routine = routine_store[routine_id]

    return {
        "routine_id": routine_id,
        "routine_name": routine["name"],
        "status": "active",
        "items": [
            {"text": item_text, "status": "pending"}
            for item_text in routine.get("items", [])
        ],
    }


def get_current_routine(active_routine):
    return active_routine


def mark_item_done(active_routine, item_text):
    for item in active_routine["items"]:
        if item["text"] == item_text:
            item["status"] = "done"
            return active_routine

    raise ValueError(f"Checklist item not found: {item_text}")


def skip_item(active_routine, item_text):
    for item in active_routine["items"]:
        if item["text"] == item_text:
            item["status"] = "skipped"
            return active_routine

    raise ValueError(f"Checklist item not found: {item_text}")


def finish_routine(active_routine):
    summary = {
        "done": 0,
        "skipped": 0,
        "pending": 0,
    }

    for item in active_routine["items"]:
        summary[item["status"]] += 1

    active_routine["status"] = "finished"
    active_routine["summary"] = summary

    return active_routine


def log_finished_routine(routine_log, finished_routine):
    routine_log.append(finished_routine)
    return routine_log
