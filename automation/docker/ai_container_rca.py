import os
import sys
import json
from google import genai

from container_diagnostic import diagnose_container
from resource_recommendation import generate_recommendations


def generate_ai_rca(report):
    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    prompt = """
    Analyze the following synthetic Docker laboratory
    incident as a Site Reliability Engineer.

    Generate:
    1. Executive incident summary
    2. Observed symptoms
    3. Potential root cause
    4. Supporting metric evidence
    5. Recommended remediation
    6. Recovery validation steps
    7. Preventive actions
    8. Capacity planning recommendations

    Use only the supplied evidence.
    Distinguish confirmed facts from hypotheses.
    Do not invent metrics or claim actions were executed.

    Diagnostic report:
    """ + json.dumps(report, indent=4)

    response = client.models.generate_content(
        model=os.environ["GEMINI_MODEL"],
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ai_container_rca.py CONTAINER")

    report = diagnose_container(sys.argv[1])

    report["recommendations"] = generate_recommendations(
        report
    )

    print("# Container Incident RCA\n")

    print("## Collected Evidence\n")
    print("```json")
    print(json.dumps(report, indent=4))
    print("```")

    try:
        print("\n## AI-Assisted Analysis\n")
        print(generate_ai_rca(report))
    except Exception as error:
        print(
            f"AI analysis failed: {type(error).__name__}",
            file=sys.stderr
        )
        sys.exit(1)
