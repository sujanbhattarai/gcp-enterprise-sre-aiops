import json
import sys
from datetime import datetime, timezone

from collect_metrics import collect_metrics
from collect_throttling import collect_throttling
from collect_container_state import collect_container_state
from bottleneck_detector import evaluate_usage


def diagnose_container(container):
    state = collect_container_state(container)

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "container": container,
        "container_state": state
    }

    if not state["running"]:
        report["overall_status"] = state["severity"]
        return report

    metrics = collect_metrics(container)
    throttling = collect_throttling(container)

    cpu = float(metrics["CPUPerc"].rstrip("%"))
    memory = float(metrics["MemPerc"].rstrip("%"))

    memory_status = evaluate_usage(memory)

    statuses = [
        memory_status,
        throttling["status"],
        state["severity"]
    ]

    if "CRITICAL" in statuses:
        overall = "CRITICAL"
    elif "UNKNOWN" in statuses:
        overall = "UNKNOWN"
    elif "WARNING" in statuses:
        overall = "WARNING"
    else:
        overall = "HEALTHY"

    report.update({
        "cpu_usage_percent": cpu,
        "memory_usage_percent": memory,
        "memory_status": memory_status,
        "cpu_throttling": throttling,
        "overall_status": overall
    })

    return report


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: container_diagnostic.py CONTAINER")

    report = diagnose_container(sys.argv[1])
    print(json.dumps(report, indent=4))
