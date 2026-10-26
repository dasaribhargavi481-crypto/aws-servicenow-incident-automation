
import json
import os
import base64
import urllib.request
import urllib.error


def lambda_handler(event, context):
    # Read ServiceNow settings from environment variables
    instance = os.environ["SN_INSTANCE"].rstrip("/")
    username = os.environ["SN_USERNAME"]
    password = os.environ["SN_PASSWORD"]

    # Extract CloudWatch alarm details
    detail = event.get("detail", {})
    alarm_name = detail.get("alarmName", "AWS Alarm")
    state = detail.get("state", {})
    alarm_state = state.get("value", "UNKNOWN")
    reason = state.get("reason", "No reason provided")

    # Ignore alarms that are not in ALARM state
    if alarm_state != "ALARM":
        return {
            "statusCode": 200,
            "body": json.dumps("No incident needed")
        }

    # Prepare ServiceNow incident
    incident = {
        "short_description": f"AWS Alert: {alarm_name}",
        "description": (
            f"Alarm: {alarm_name}\n"
            f"State: {alarm_state}\n"
            f"Reason: {reason}"
        ),
        "category": "software",
        "impact": "2",
        "urgency": "2"
    }

    url = f"{instance}/api/now/table/incident"
    credentials = base64.b64encode(
        f"{username}:{password}".encode()
    ).decode()

    request = urllib.request.Request(
        url,
        data=json.dumps(incident).encode(),
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode())

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Incident created",
                "incident": result.get("result", {})
            })
        }

    except urllib.error.HTTPError as error:
        print("ServiceNow API error:", error.code)
        print(error.read().decode())
        raise

    except urllib.error.URLError as error:
        print("Connection error:", str(error.reason))
        raise
