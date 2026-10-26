
# AWS CloudWatch Alarm Setup

## Objective
Monitor AWS resources and trigger an event when an alarm enters the ALARM state.

## Services Required
- Amazon CloudWatch
- AWS Lambda
- Amazon EventBridge

## Setup Instructions

1. Sign in to the AWS Management Console.
2. Open Amazon CloudWatch.
3. Select Alarms and choose Create alarm.
4. Select an available metric, such as EC2 CPUUtilization.
5. Configure a threshold, for example CPU utilization greater than 80%.
6. Set the evaluation period and create the alarm.
7. Configure an Amazon EventBridge rule to detect CloudWatch alarm state changes.
8. Set the AWS Lambda function as the target of the rule.
9. Grant EventBridge permission to invoke the Lambda function.
10. Test the workflow using a test alarm event.

## Expected Result
When the alarm enters the ALARM state, the Lambda function receives the event and can send the alert details to ServiceNow.

## Note
An EC2 CPU alarm requires an EC2 instance and appropriate metric data. Use a test event first to verify the integration.
