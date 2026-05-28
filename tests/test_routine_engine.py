from src.routine_engine import list_routines


def test_list_routines_returns_supplied_routines():
    routine_store = {
        "example-routine": {
            "name": "Example Routine",
        }
    }

    routines = list_routines(routine_store)

    assert routines == routine_store
