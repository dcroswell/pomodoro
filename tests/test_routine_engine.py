import pytest

from src.routine_engine import get_current_routine, list_routines, start_routine


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
            "items": ["First item", "Second item"],
        }
    }

    active_routine = start_routine(routine_store, "example-routine")

    assert active_routine["routine_id"] == "example-routine"
    assert active_routine["routine_name"] == "Example Routine"
    assert active_routine["status"] == "active"
    assert active_routine["items"] == [
        {"text": "First item", "status": "pending"},
        {"text": "Second item", "status": "pending"},
    ]


def test_start_routine_raises_clear_error_for_unknown_routine():
    routine_store = {
        "example-routine": {
            "name": "Example Routine",
        }
    }

    with pytest.raises(ValueError, match="Routine not found: missing-routine"):
        start_routine(routine_store, "missing-routine")


def test_get_current_routine_returns_active_routine():
    active_routine = {
        "routine_id": "example-routine",
        "routine_name": "Example Routine",
        "status": "active",
        "items": [
            {"text": "First item", "status": "pending"},
        ],
    }

    current_routine = get_current_routine(active_routine)

    assert current_routine == active_routine
