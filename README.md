#  AWS Serverless Task API

##  Project Overview
This project demonstrates a simple **serverless REST API** built using AWS services.  
The API allows users to **create tasks** and **retrieve a list of tasks** without managing any servers.

---

##  Objective
- Build a lightweight backend API using AWS serverless services  
- Demonstrate knowledge of:
  - AWS Lambda  
  - API Gateway  
  - IAM  
  - CloudWatch Logs  

---

##  Architecture
Client → API Gateway → Lambda → CloudWatch Logs

---

##  Services Used

### 1. AWS Lambda
- Used to run backend logic
- Handles GET and POST requests
- No server management required

### 2. API Gateway
- Exposes the API endpoints
- Routes requests to Lambda

### 3. AWS IAM
- Provides permissions for Lambda execution

### 4. CloudWatch Logs
- Stores logs for debugging and monitoring

---

##  Creation & Deployment Steps

###  Step 1: Create Lambda Function
1. Go to AWS Console → Lambda  
2. Click **Create function**  
3. Select **Author from scratch**  
4. Enter function name: `task-api`  
5. Choose runtime: Python 3.x  
6. Click **Create function**  

---

###  Step 2: Add Lambda Code
Replace default code with:

python
`
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
        body = json.loads(event.get("body", "{}"))

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
    `
    ---

## Step 3:
1. Go to AWS Console → API Gateway  
2. Click **Create API**  
3. Select **HTTP API** (important: do not choose REST API)  
4. Click **Build**  

---

##  Step 4: Configure API
1. Enter API name: `task-api`  
2. Under **Integrations**, click **Add integration**  
3. Select **Lambda**  
4. Choose your function: `task-api`  
5. Click **Add integration**  
6. Click **Next**  

---

##  Step 5: Create Routes
Add the following routes:

- Method: `GET`  
  Path: `/tasks`  
  Integration: `task-api`  

- Method: `POST`  
  Path: `/tasks`  
  Integration: `task-api`  

After adding both routes, click **Next**  

---
## 📘 API Design

This project implements a simple REST-style API using AWS Lambda and API Gateway.

### Base URL https://m7aodmr0u6.execute-api.ap-southeast-2.amazonaws.com 

---

### 🔹 GET /tasks
- Returns a list of all tasks  
- Method: `GET`  

#### Example Request:
`
curl https://m7aodmr0u6.execute-api.ap-southeast-2.amazonaws.com/tasks
[]
Or
[
  {
    "title": "My Task",
    "status": "pending"
  }
]
POST /tasks
Creates a new task
Method: POST
{
  "title": "My Task"
}
{
  "title": "My Task"
}
{
  "title": "My Task",
  "status": "pending"
}```

## Deployment Steps
1. Go to AWS Console → Lambda
2. Click Create Function
3. Choose Author from scratch
4. Name: task-api
5. Runtime: Python 3.x
6. Add API code and click Deploy
7. Go to API Gateway
8. Click Create API
9. Select HTTP API
10. Add integration → select Lambda (task-api)
11. Create routes:
12. GET /tasks
13. POST /tasks
14. Use default stage:
15. $default
Deployment is automatic (no manual deploy needed)
Copy the Invoke URL
 Testing Steps (using curl)
Test GET request
curl https://m7aodmr0u6.execute-api.ap-southeast-2.amazonaws.com/tasks
 Test POST (Success)
curl -X POST https://m7aodmr0u6.execute-api.ap-southeast-2.amazonaws.com/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Test Task"}'
 Test POST (Validation Error)
curl -X POST https://m7aodmr0u6.execute-api.ap-southeast-2.amazonaws.com/tasks \
-H "Content-Type: application/json" \
-d '{}'

## Cleanup Steps

To avoid unnecessary AWS charges:

Go to AWS Console → Lambda
Delete function: task-api
Go to API Gateway
Delete the created API
Go to CloudWatch (optional)
Delete log groups

## Future Enhancement: Persistent Storage

Currently, tasks are stored in memory inside the Lambda function.
This means data is lost when the function restarts.

Improvement Plan:
Integrate Amazon DynamoDB for storage
Store tasks permanently in a database
Retrieve tasks from DynamoDB instead of memory
Benefits:
Data persistence
Scalability
Reliability
Additional Enhancements:
Add authentication (AWS Cognito or JWT)
Implement role-based access control
Add monitoring and alerts

---
