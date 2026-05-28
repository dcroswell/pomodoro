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
