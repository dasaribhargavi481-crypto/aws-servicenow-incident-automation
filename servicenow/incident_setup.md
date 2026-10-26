
# ServiceNow Incident Setup

## Project Overview
This module integrates AWS CloudWatch alerts with ServiceNow Incident Management.

## Objectives
- Automatically create incidents from AWS alerts.
- Reduce manual incident creation.
- Track cloud infrastructure issues.

## Technologies
- ServiceNow Incident Management
- ServiceNow REST API
- AWS Lambda
- Amazon CloudWatch
- Python

## Configuration
1. Log in to your ServiceNow developer instance.
2. Open the Incidents module.
3. Verify that you can create an incident manually.
4. Note your instance URL.
5. Configure an authorized integration user.
6. Use the Table API endpoint: /api/now/table/incident
7. Configure AWS Lambda to send alert details using HTTPS.
8. Verify that the incident appears in ServiceNow.

## Security
- Never upload passwords or API tokens to GitHub.
- Store credentials securely.
- Use minimum required permissions.
- Use HTTPS for API requests.

## Expected Result
When a valid AWS CloudWatch alarm event reaches AWS Lambda, a ServiceNow incident is created automatically.
