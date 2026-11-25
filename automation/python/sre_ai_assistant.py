import os
import json
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

with open("diagnostic_report.json", "r") as file:
    report = json.load(file)

report["hostname"] = "lab-vm"

prompt = f"""
You are a Site Reliability Engineering assistant.

Analyze the following infrastructure diagnostic report:

{json.dumps(report, indent=2)}

Provide:

1. Overall infrastructure health assessment
2. CPU, memory and disk analysis
3. Potential operational risks
4. Recommended troubleshooting actions
5. Preventive recommendations
6. Short incident summary, if an incident exists

Use only the supplied evidence.
Do not invent incidents or root causes.
Identify any missing information.
Do not recommend unnecessary restarts.
"""

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("===== AI-Powered SRE Analysis =====")
    print(response.text)

    with open("ai_analysis.txt", "w") as file:
        file.write(response.text or "")

    print("\nAI analysis saved successfully.")

except Exception as error:
    print(f"Gemini analysis failed: {error}")
    raise SystemExit(1)
