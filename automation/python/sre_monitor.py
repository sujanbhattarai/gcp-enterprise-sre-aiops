import logging
import json
import subprocess
import sys

logging.basicConfig(
    filename="sre_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Infrastructure health check started")

    subprocess.run(
        [sys.executable, "diagnostic_report.py"],
        check=True
    )

    with open("diagnostic_report.json", "r") as file:
        report = json.load(file)

    status = report["overall_status"]

    if status == "CRITICAL":
        logging.critical("Critical infrastructure condition detected")
    elif status == "WARNING":
        logging.warning("Infrastructure warning detected")
    elif status == "HEALTHY":
        logging.info("Infrastructure is healthy")
    else:
        raise ValueError("Unknown health status")

    logging.info("Health check completed successfully")

    print(f"Overall Status: {status}")
    print("Logs saved to sre_monitor.log")

except Exception as error:
    logging.exception("Monitoring automation failed")
    print(f"Error: {error}")
    sys.exit(1)
