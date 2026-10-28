
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
