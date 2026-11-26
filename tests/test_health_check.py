import pytest
from health_utils import check_health


@pytest.mark.parametrize(
    "value, warning, critical, expected",
    [
        (25, 70, 90, "HEALTHY"),
        (69, 70, 90, "HEALTHY"),
        (70, 70, 90, "WARNING"),
        (89, 70, 90, "WARNING"),
        (90, 70, 90, "CRITICAL"),
        (95, 70, 90, "CRITICAL"),
        (75, 75, 90, "WARNING"),
        (80, 80, 95, "WARNING"),
        (95, 80, 95, "CRITICAL"),
    ]
)
def test_check_health(value, warning, critical, expected):
    assert check_health(value, warning, critical) == expected


@pytest.mark.parametrize(
    "value, warning, critical, expected",
    [
        (0, 70, 90, "HEALTHY"),
        (100, 70, 90, "CRITICAL"),
        (69.9, 70, 90, "HEALTHY"),
        (70.1, 70, 90, "WARNING"),
        (89.9, 70, 90, "WARNING"),
        (90.1, 70, 90, "CRITICAL"),
    ]
)
def test_boundary_conditions(value, warning, critical, expected):
    assert check_health(value, warning, critical) == expected
