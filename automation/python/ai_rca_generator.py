import os
import json
from google import genai
from datetime import datetime, timezone

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

with open("simulated_incident.json") as file:
    incident = json.load(file)

with open("incident_analysis.txt") as file:
    analysis = file.read()

prompt = f"""
You are an enterprise SRE incident analyst.

Generate a professional draft RCA report.

Incident evidence:
{json.dumps(incident, indent=2)}

Previous AI investigation:
{analysis}

Include the following sections:

1. Executive Summary
2. Incident Severity
3. Affected Infrastructure
4. Observed Symptoms
5. Potential Root Cause
6. Business Impact
7. Recommended Troubleshooting
8. Corrective Actions
9. Preventive Actions
10. Recovery Validation Plan
11. Missing Evidence
12. Lessons Learned

Rules:
- Clearly label this as a simulated incident.
- Treat previous AI analysis as unverified.
- Do not invent timestamps or business impact.
- Distinguish facts from hypotheses.
- Do not claim recovery has occurred.
- Mark the root cause as unconfirmed.
- Require human review of the report.
"""

try:
    response = client.models.generate_content(
        model=os.getenv(
            "GEMINI_MODEL",
            "gemini-3.5-flash-lite"
        ),
        contents=prompt
    )

    if not response.text:
        raise ValueError("Empty Gemini response")

    timestamp = datetime.now(timezone.utc).isoformat()

    with open("incident_rca.md", "w") as file:
        file.write("# AI-Generated RCA Draft\n\n")
        file.write(f"Generated at: {timestamp}\n\n")
        file.write(response.text)

    print(response.text)
    print("\nRCA draft saved to incident_rca.md")

except Exception as error:
    print(f"RCA generation failed: {error}")
    raise SystemExit(1)
