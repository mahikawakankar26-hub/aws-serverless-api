import json

tasks = []

def lambda_handler(event, context):
    print("Event received:", event)

    method = event.get("requestContext", {}).get("http", {}).get("method")

    if method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(tasks)
        }

    if method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
        except:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON"})
            }

        title = body.get("title")
        status = body.get("status", "pending")

        if not title:
            print("Validation failed: title missing")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Title is required"})
            }

        task = {
            "title": title,
            "status": status
        }

        tasks.append(task)

        print("Task created:", task)

        return {
            "statusCode": 201,
            "body": json.dumps(task)
        }

    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Method not allowed"})
    }