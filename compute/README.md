# Enterprise Compute Engine Architecture

## Project Configuration
- Project: gcp-enterprise-sre-aiops
- Region: us-east4
- Zone: us-east4-a
- Network: enterprise-sre-vpc
- Subnet: application-subnet

## Planned Infrastructure
- Linux virtual machines
- E2 general-purpose machine family
- Persistent disks
- Instance templates
- Managed Instance Groups
- Autoscaling and autohealing
- Application health checks

## Observability
- Google Cloud Ops Agent
- Cloud Monitoring
- Cloud Logging
- CPU, memory, disk and network monitoring

## AIOps Integration
- Python automation
- Gemini and Vertex AI
- AI-powered incident investigation
- Root cause analysis recommendations
- Human-approved remediation

## Implementation Status
- Architecture designed
- VM deployment pending

## Machine Type Selection
- Machine family: E2
- Initial machine type: e2-small
- Virtual CPUs: 2 shared-core
- Memory: 2 GiB
- Operating system: Ubuntu 24.04 LTS
- Boot disk: 10 GB standard persistent disk
- Provisioning model: Standard

## Cost Optimization
- On-demand pricing
- Stop VMs when not performing labs
- Delete unused disks and external IPs
- Avoid oversized machine types
- Monthly project budget target: $50

## Scaling Strategy
- Vertical scaling for resource constraints
- Horizontal scaling using Managed Instance Groups
- Autoscaling based on workload demand
- Monitoring-driven capacity planning
