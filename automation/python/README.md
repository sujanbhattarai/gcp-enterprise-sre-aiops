# Python Automation & AI-Powered SRE Incident Assistant

## Overview

This module implements infrastructure monitoring,
automated health checks, structured diagnostic reporting,
and AI-assisted incident investigation using Python
and Google Gemini.

## Architecture

Compute Engine VM
    -> Python Infrastructure Monitoring
    -> Automated Threshold Detection
    -> JSON Diagnostic Reporting
    -> Gemini AI Analysis
    -> Incident Investigation
    -> RCA Draft Generation

## Implemented Capabilities

- Linux infrastructure monitoring
- CPU, memory and disk utilization monitoring
- Automated health classification
- Structured JSON diagnostic reporting
- Operational logging and exception handling
- Gemini API integration
- AI-powered infrastructure analysis
- Simulated incident investigation
- AI-generated root cause analysis drafts

## Technology Stack

- Google Compute Engine
- Ubuntu Linux
- Python 3.12
- psutil
- Google GenAI SDK
- Gemini 3.5 Flash-Lite
- JSON
- Git and GitHub

## Python Modules

| Script | Purpose |
|---|---|
| system_info.py | Collect system information |
| infrastructure_health.py | Monitor resource utilization |
| health_check.py | Classify infrastructure health |
| diagnostic_report.py | Generate JSON diagnostics |
| sre_monitor.py | Operational logging and orchestration |
| gemini_test.py | Validate Gemini API connectivity |
| sre_ai_assistant.py | AI infrastructure analysis |
| sre_incident_assistant.py | AI incident investigation |
| ai_rca_generator.py | Generate RCA drafts |

## Security

- API keys are supplied through environment variables.
- Credentials are excluded from version control.
- Live diagnostic reports and logs are excluded.
- AI recommendations require human validation.
- Automated remediation is not yet enabled.

## Validation

- Live VM resource monitoring successfully tested.
- JSON reporting and operational logging verified.
- Gemini API connectivity successfully validated.
- Healthy infrastructure analysis tested.
- Synthetic critical incident investigation tested.
- AI-generated RCA draft successfully produced.

## Upcoming Enhancements

- Pytest automated testing
- GitHub Actions CI pipeline
- Google Cloud Build
- Docker containerization
- Artifact Registry
- Cloud Run deployment
- Cloud Deploy
- Intelligent alert correlation
- RAG-based runbook assistant
- Agentic AI
- Controlled self-healing
