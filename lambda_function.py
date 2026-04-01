import boto3
import datetime
import json
import os
import requests

# AWS Clients
ce = boto3.client('ce')
sns = boto3.client('sns')

# Environment Variables
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


# 📊 Get Daily Cost Trend
def get_cost_data():
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    end = today.strftime('%Y-%m-%d')

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    dates = []
    costs = []

    for day in response['ResultsByTime']:
        dates.append(day['TimePeriod']['Start'])

        amount = float(day['Total']['UnblendedCost']['Amount'])

        # Handle free tier negative values
        if amount < 0:
            amount = 0

        costs.append(round(amount, 5))

    return dates, costs


# 🧾 Service-wise Breakdown
def get_service_breakdown():
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    end = today.strftime('%Y-%m-%d')

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    services = []
    service_costs = []

    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        cost = float(group['Metrics']['UnblendedCost']['Amount'])

        if cost < 0:
            cost = 0

        services.append(service)
        service_costs.append(round(cost, 5))

    return services, service_costs


# 🤖 Gemini AI Suggestion
def get_ai_suggestion(costs):
    if not GEMINI_API_KEY:
        return None

    prompt = f"My AWS costs for last 7 days are {costs}. Suggest cost optimization steps."

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ]
            }
        )

        data = response.json()
        print("GEMINI RESPONSE:", data)

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return None

    except Exception as e:
        print("Gemini Error:", str(e))
        return None


# 🧠 Rule-based fallback
def get_rule_based_suggestion(costs):
    total = sum(costs)
    avg = total / len(costs)
    max_cost = max(costs)

    if total == 0:
        return (
            "🎉 You are within AWS Free Tier.\n"
            "👉 No costs incurred.\n"
            "👉 Keep monitoring usage."
        )

    if max_cost > avg * 2:
        return (
            "⚠️ Cost spike detected!\n"
            "👉 Check EC2 / Lambda usage.\n"
            "👉 Review recent deployments."
        )

    if total < 10:
        return (
            "📊 Moderate usage.\n"
            "👉 Remove unused resources.\n"
            "👉 Use smaller instance types."
        )

    return (
        "🚨 High cost detected!\n"
        "👉 Use Savings Plans.\n"
        "👉 Optimize infrastructure."
    )


# 🚨 SNS Alert
def send_alert(total_cost):
    if not SNS_TOPIC_ARN:
        print("SNS not configured")
        return

    if total_cost > 1:  # threshold
        message = f"⚠️ AWS Cost Alert!\nTotal cost reached ${total_cost}"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Cost Alert 🚨",
            Message=message
        )


# 🚀 MAIN HANDLER
def lambda_handler(event, context):
    try:
        # Get data
        dates, costs = get_cost_data()
        services, service_costs = get_service_breakdown()

        total_cost = sum(costs)

        # Send alert
        send_alert(total_cost)

        # Try AI first
        ai_suggestion = get_ai_suggestion(costs)

        if ai_suggestion:
            suggestion = ai_suggestion
        else:
            suggestion = get_rule_based_suggestion(costs)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "dates": dates,
                "costs": costs,
                "services": services,
                "service_costs": service_costs,
                "total_cost": round(total_cost, 5),
                "suggestion": suggestion
            })
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
