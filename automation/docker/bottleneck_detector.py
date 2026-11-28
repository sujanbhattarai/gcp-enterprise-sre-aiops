import json


def evaluate_usage(value):
    if value >= 90:
        return "CRITICAL"
    elif value >= 75:
        return "WARNING"
    return "HEALTHY"


def evaluate_throttling(periods, throttled):
    if periods <= 0:
        return 0, "UNKNOWN"

    percentage = (throttled / periods) * 100

    if percentage >= 25:
        status = "CRITICAL"
    elif percentage >= 10:
        status = "WARNING"
    else:
        status = "HEALTHY"

    return round(percentage, 2), status


def evaluate_oom(oom_killed):
    return "CRITICAL" if oom_killed else "HEALTHY"


if __name__ == "__main__":
    rate, status = evaluate_throttling(117, 116)

    report = {
        "cpu_throttling_percent": rate,
        "cpu_throttling_status": status,
        "memory_usage_percent": 79.67,
        "memory_status": evaluate_usage(79.67),
        "oom_killed": False,
        "oom_status": evaluate_oom(False)
    }

    print(json.dumps(report, indent=4))
