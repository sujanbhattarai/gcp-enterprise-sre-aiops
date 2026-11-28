import json
import sys

from container_diagnostic import diagnose_container


def generate_recommendations(report):
    recommendations = []

    state = report["container_state"]

    if state["oom_killed"]:
        recommendations.append({
            "resource": "Memory",
            "severity": "CRITICAL",
            "finding": "Container OOMKilled",
            "action": "Investigate memory usage and review memory limits"
        })

    elif not state["running"] and state["exit_code"] != 0:
        recommendations.append({
            "resource": "Application",
            "severity": "CRITICAL",
            "finding": "Container execution failure",
            "action": "Investigate container logs and exit code"
        })

    throttling = report.get("cpu_throttling", {})
    cpu_status = throttling.get("status")

    if cpu_status == "CRITICAL":
        recommendations.append({
            "resource": "CPU",
            "severity": "CRITICAL",
            "finding": "Excessive CPU throttling",
            "action": "Review CPU quota, workload demand and scaling options"
        })

    elif cpu_status == "WARNING":
        recommendations.append({
            "resource": "CPU",
            "severity": "WARNING",
            "finding": "Elevated CPU throttling",
            "action": "Investigate CPU saturation and monitor trends"
        })

    elif cpu_status == "UNKNOWN":
        recommendations.append({
            "resource": "CPU",
            "severity": "UNKNOWN",
            "finding": "Insufficient CPU metric data",
            "action": "Repeat metric collection"
        })

    memory_status = report.get("memory_status")

    if memory_status == "CRITICAL":
        recommendations.append({
            "resource": "Memory",
            "severity": "CRITICAL",
            "finding": "High memory utilization",
            "action": "Investigate memory leaks and review capacity"
        })

    elif memory_status == "WARNING":
        recommendations.append({
            "resource": "Memory",
            "severity": "WARNING",
            "finding": "Elevated memory utilization",
            "action": "Monitor memory growth and available capacity"
        })

    if not recommendations:
        recommendations.append({
            "severity": report["overall_status"],
            "finding": "No configured resource problems detected",
            "action": "Continue monitoring or verify expected workload completion"
        })

    return recommendations


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: resource_recommendation.py CONTAINER")

    report = diagnose_container(sys.argv[1])
    report["recommendations"] = generate_recommendations(report)

    print(json.dumps(report, indent=4))
