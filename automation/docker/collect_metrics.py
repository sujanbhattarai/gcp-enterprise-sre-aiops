import subprocess
import json
import sys


def collect_metrics(container):
    result = subprocess.run(
        [
            "docker", "stats", "--no-stream",
            "--format", "{{json .}}", container
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return json.loads(result.stdout)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: collect_metrics.py CONTAINER")

    metrics = collect_metrics(sys.argv[1])
    print(json.dumps(metrics, indent=4))
