from src.routine_engine import list_routines, start_routine


def test_list_routines_returns_supplied_routines():
    routine_store = {
        "example-routine": {
            "name": "Example Routine",
        }
    }

    routines = list_routines(routine_store)

    assert routines == routine_store


def test_start_routine_creates_active_routine_state():
    routine_store = {
        "example-routine": {
            "name": "Example Routine",
        }
    }

    active_routine = start_routine(routine_store, "example-routine")

    assert active_routine["routine_id"] == "example-routine"
    assert active_routine["routine_name"] == "Example Routine"
    assert active_routine["status"] == "active"
