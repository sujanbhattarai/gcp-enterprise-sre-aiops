import pytest

from bottleneck_detector import (
    evaluate_usage,
    evaluate_throttling,
    evaluate_oom
)


@pytest.mark.parametrize("usage,expected", [
    (0, "HEALTHY"),
    (50, "HEALTHY"),
    (74.99, "HEALTHY"),
    (75, "WARNING"),
    (89.99, "WARNING"),
    (90, "CRITICAL"),
    (100, "CRITICAL")
])
def test_resource_usage(usage, expected):
    assert evaluate_usage(usage) == expected


@pytest.mark.parametrize("periods,throttled,rate,status", [
    (100, 0, 0, "HEALTHY"),
    (100, 9, 9, "HEALTHY"),
    (100, 10, 10, "WARNING"),
    (100, 24, 24, "WARNING"),
    (100, 25, 25, "CRITICAL"),
    (117, 116, 99.15, "CRITICAL"),
    (101, 1, 0.99, "HEALTHY"),
    (0, 0, 0, "UNKNOWN")
])
def test_cpu_throttling(periods, throttled, rate, status):
    assert evaluate_throttling(periods, throttled) == (rate, status)


def test_oom_killed():
    assert evaluate_oom(True) == "CRITICAL"


def test_no_oom():
    assert evaluate_oom(False) == "HEALTHY"
