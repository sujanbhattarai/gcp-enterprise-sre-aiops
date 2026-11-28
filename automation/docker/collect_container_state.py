import subprocess
import json
import sys

from bottleneck_detector import evaluate_oom


def collect_container_state(container):
    result = subprocess.run(
        ["docker", "inspect", container],
        capture_output=True,
        text=True,
        check=True
    )

    details = json.loads(result.stdout)[0]
    state = details["State"]

    oom_killed = state["OOMKilled"]
    exit_code = state["ExitCode"]

    if oom_killed:
        diagnosis = "Container terminated due to memory exhaustion"
        recommendation = "Review memory consumption and resource limits"
        severity = "CRITICAL"

    elif state["Running"]:
        diagnosis = "Container is running"
        recommendation = "Continue monitoring"
        severity = "HEALTHY"

    elif exit_code != 0:
        diagnosis = "Container exited with an error"
        recommendation = "Investigate container logs and exit code"
        severity = "CRITICAL"

    else:
        diagnosis = "Container stopped without a reported error"
        recommendation = "Verify expected workload behavior"
        severity = "INFO"

    return {
        "container": container,
        "status": state["Status"],
        "running": state["Running"],
        "oom_killed": oom_killed,
        "exit_code": exit_code,
        "oom_status": evaluate_oom(oom_killed),
        "severity": severity,
        "diagnosis": diagnosis,
        "recommendation": recommendation
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: collect_container_state.py CONTAINER")

    print(json.dumps(
        collect_container_state(sys.argv[1]),
        indent=4
    ))
