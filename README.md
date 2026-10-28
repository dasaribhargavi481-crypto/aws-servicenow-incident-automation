
# AWS CloudWatch to ServiceNow Incident Automation

## Project Overview
This beginner-friendly project demonstrates how cloud monitoring alerts can be connected to IT incident management.

## Objectives
- Understand AWS CloudWatch alarm events.
- Learn the role of Amazon EventBridge.
- Understand AWS Lambda event processing.
- Learn how ServiceNow REST API can create incidents.
- Document an incident automation workflow.

## Technologies
- AWS CloudWatch
- Amazon EventBridge
- AWS Lambda
- ServiceNow Incident Management
- ServiceNow REST API
- GitHub

## Architecture
CloudWatch Alarm → EventBridge → AWS Lambda → ServiceNow REST API → Incident

See [Architecture](architecture.md) for details.

## Project Files

- `lambda/sample_alert.json` — sample CloudWatch alert.
- `lambda/incident_handler.py` — AWS Lambda handler example.
- `lambda/incident_workflow.md` — incident automation workflow.
- `lambda/cloudwatch/alarm_setup.md` — CloudWatch setup notes.
- `servicenow/incident_setup.md` — ServiceNow setup notes.
- `architecture.md` — project architecture.
- `test_cases.md` — test scenarios and expected results.
- `incident_examples.md` — sample incident scenarios.


## Demo Status
This repository contains sample alert data, code, and documentation. Real AWS-to-ServiceNow integration has not yet been tested and requires configured AWS and ServiceNow environments.

## Security
Never upload passwords, API tokens, or other credentials to GitHub.

## Author
Dasari Bhargavi
  
