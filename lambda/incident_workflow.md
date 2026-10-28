
# AWS to ServiceNow Incident Workflow

## Project Goal
Simulate AWS CloudWatch alerts and document how they can be converted into ServiceNow incidents.

## Workflow
1. CloudWatch detects high CPU usage.
2. An alarm changes its state to ALARM.
3. Amazon EventBridge detects the alarm state change.
4. AWS Lambda processes the alert event.
5. Lambda sends an API request to ServiceNow.
6. ServiceNow creates an incident for the support team.

## Sample Alert
- Alarm Name: High-CPU-Usage
- Alert State: ALARM
- Reason: CPU utilization exceeded 80 percent
- Incident Priority: To be assigned according to ServiceNow rules.

## Expected Result
A ServiceNow incident should contain the alarm name, alert state, and reason.

## Testing Limitation
This GitHub-only version documents and simulates the workflow. It does not create a real AWS alarm or a real ServiceNow incident.

## Security
Never commit ServiceNow passwords, API tokens, or other credentials to GitHub.
