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

##  Step 6: Deploy API
1. Use the default stage: `$default`  
2. Note: HTTP APIs auto-deploy, no manual deployment needed  
3. Go to **Stages → $default**  
4. Copy the **Invoke URL**  
5. Your API is now live and accessible