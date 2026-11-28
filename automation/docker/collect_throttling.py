import subprocess
import json
import sys
import time

from bottleneck_detector import evaluate_throttling


def read_cpu_stats(container):
    result = subprocess.run(
        [
            "docker", "exec", container,
            "cat", "/sys/fs/cgroup/cpu.stat"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    metrics = {}

    for line in result.stdout.splitlines():
        key, value = line.split()
        metrics[key] = int(value)

    return metrics


def collect_throttling(container):
    before = read_cpu_stats(container)

    time.sleep(5)

    after = read_cpu_stats(container)

    periods = after["nr_periods"] - before["nr_periods"]
    throttled = after["nr_throttled"] - before["nr_throttled"]

    rate, status = evaluate_throttling(periods, throttled)

    return {
        "container": container,
        "sample_duration_seconds": 5,
        "cpu_periods": periods,
        "throttled_periods": throttled,
        "cpu_throttling_percent": rate,
        "status": status
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: collect_throttling.py CONTAINER")

    print(json.dumps(
        collect_throttling(sys.argv[1]),
        indent=4
    ))
