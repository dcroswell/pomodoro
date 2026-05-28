def list_routines(routine_store):
    return routine_store


def start_routine(routine_store, routine_id):
    routine = routine_store[routine_id]

    return {
        "routine_id": routine_id,
        "routine_name": routine["name"],
        "status": "active",
    }
