
# Test Cases - AWS ServiceNow Incident Automation

## Test Case 1: High CPU Alert

**Input:** Alarm state is ALARM  
**Alarm Name:** High-CPU-Usage  
**Expected Result:** The workflow should prepare an incident request with the alarm name and reason.

## Test Case 2: Alarm Returns to OK

**Input:** Alarm state is OK  
**Expected Result:** No new incident should be created by the sample Lambda logic.

## Test Case 3: Missing Alarm Name

**Input:** Alarm event has no alarmName field  
**Expected Result:** The workflow should use the default name AWS Alarm.

## Test Case 4: ServiceNow API Error

**Input:** ServiceNow API returns an error  
**Expected Result:** The error should be logged and handled for troubleshooting.

## Test Status

These are documented test scenarios. They have not been executed against real AWS or ServiceNow services.



## Project Test Results

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | CloudWatch alarm state is ALARM | Incident details are prepared |
| 2 | Alarm state is OK | No new incident should be created |
| 3 | CPU usage exceeds 80% | High CPU alert is identified |
| 4 | Required alert field is missing | Validation error is reported |
| 5 | ServiceNow connection is unavailable | Error is logged for troubleshooting |

## Note

These are planned test cases for the GitHub demonstration. They have not been executed against live AWS or ServiceNow services.
