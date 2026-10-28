
# AWS + ServiceNow Project Architecture

## Architecture Flow

CloudWatch Alarm
       |
       v
Amazon EventBridge
       |
       v
AWS Lambda Function
       |
       v
ServiceNow REST API
       |
       v
ServiceNow Incident Created

## Component Description

### 1. Amazon CloudWatch
Monitors metrics such as CPU utilization and generates alarms.

### 2. Amazon EventBridge
Detects CloudWatch alarm state changes and routes events.

### 3. AWS Lambda
Processes the alert and prepares incident information.

### 4. ServiceNow REST API
Receives the incident request from Lambda.

### 5. ServiceNow Incident Management
Stores the incident for the support team to investigate.

## Demo Status
This repository currently provides a documented workflow and sample alert.
Real AWS and ServiceNow integration requires the relevant accounts and configuration.


## Example Alert

Sample alert file: `lambda/sample_alert.json`

Example:
- Alarm Name: High-CPU-Usage
- State: ALARM
- Reason: CPU utilization exceeded 80 percent

Expected result: When the AWS and ServiceNow integration is configured correctly, this alert can be used to test incident creation.
