from src.routine_engine import list_routines


def test_list_routines_returns_available_routines():
    routines = list_routines()

    assert "wakeup" in routines
    assert routines["wakeup"]["name"] == "Wake-up Routine"
