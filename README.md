# 🚀 Serverless CRUD Application (AWS Lambda + API Gateway + DynamoDB)

## 📌 Overview

This project is a fully serverless CRUD (Create, Read, Update, Delete) web application built using AWS managed services.

It demonstrates:

- REST API development
- Serverless backend architecture
- NoSQL database integration
- Secure HTTPS configuration
- Monitoring and logging
- Real-world AWS debugging experience

---

# 🏗 Architecture Diagram


<img width="1498" height="510" alt="AWS Lambda + API Gateway + DynamoDB-new" src="https://github.com/user-attachments/assets/51ac36aa-44d0-47c6-9691-9d3659ce0ff5" />

---

# 🏛 Architecture Flow

```
Route 53 + SSL (ACM)
        ↓
Amazon API Gateway
        ↓
AWS Lambda (Python)
        ↓
AWS Step Functions (Optional Orchestration)
        ↓
Amazon DynamoDB
        ↑
CloudWatch Logs (Monitoring & Logging)
```

---

# 🧱 Architecture Components

## 1️⃣ Amazon Route 53

- DNS routing service
- Maps custom domain to API Gateway
- Provides high availability DNS resolution

---

## 2️⃣ AWS Certificate Manager (ACM)

- Provides SSL certificate
- Enables HTTPS for secure API communication
- Attached to API Gateway custom domain

---

## 3️⃣ Amazon API Gateway

- Entry point for all HTTP requests
- Handles REST methods:
  - GET
  - POST
  - PUT
  - DELETE
- Uses Lambda Proxy Integration
- Manages CORS
- Enables request routing and validation

---

## 4️⃣ AWS Lambda (Python Backend)

- Implements CRUD logic
- Fully serverless compute
- Auto scaling
- Pay-per-use model

### Responsibilities:

- Insert records
- Fetch records
- Update records
- Delete records
- Handle CORS
- Handle Decimal conversion from DynamoDB

---

## 5️⃣ AWS Step Functions (Optional Layer)

- Orchestrates complex workflows
- Handles multi-step processing
- Adds retry logic and workflow management
- Useful for production-grade business logic

---

## 6️⃣ Amazon DynamoDB

Fully managed NoSQL database.

### Table Schema

| Attribute | Type   | Key Type       |
|------------|--------|---------------|
| email      | String | Partition Key |
| 1          | Number | Sort Key |

### Why DynamoDB?

- Serverless
- Low latency
- Auto scaling
- Highly available
- No infrastructure management

---

## 7️⃣ Amazon CloudWatch

Used for:

- Lambda logs
- Debugging
- Performance monitoring
- Error tracking
- Operational visibility

---

# 🔄 End-to-End Request Flow

Example: Update Record

1. User clicks Update in UI
2. Browser sends PUT request
3. Route 53 resolves domain
4. HTTPS secured via ACM
5. API Gateway receives request
6. API Gateway invokes Lambda
7. Lambda processes business logic
8. DynamoDB updates record
9. CloudWatch logs execution details
10. Response returned to user

---

# 🛠 Deployment Steps

## Step 1 – Create DynamoDB Table

- Table Name: `devdb`
- Partition Key: `id` (String)
- Sort Key: `1` (Number)
- Region: us-east-1

---

## Step 2 – Create Lambda Function

- Runtime: Python 3.x
- Upload:
  - lambda_function.py
  - index.html
  - view.html
  - edit.html
  - success.html
- Attach IAM Role:
  - DynamoDB access policy

---

## Step 3 – Create API Gateway (REST API)

1. Create resource `/`
2. Add methods:
   - GET
   - POST
   - PUT
   - DELETE
3. Enable Lambda Proxy Integration
4. Enable CORS
5. Deploy API (stage: dev)

---

## Step 4 – Configure SSL (ACM)

- Request certificate
- Validate domain
- Attach certificate to API Gateway

---

## Step 5 – Configure Route 53

- Create A record
- Alias to API Gateway
- Map custom domain

---

# 🧠 Technical Challenges Solved

- Decimal serialization error in DynamoDB
- PUT request not updating records
- CORS preflight handling
- API Gateway redeployment mismatch
- DynamoDB key type sensitivity
- Numeric sort key handling

---

# 📊 Features

- Full CRUD operations
- REST API architecture
- Modern responsive UI
- HTTPS enabled
- Serverless infrastructure
- CloudWatch monitoring
- Proper error handling
- Decimal conversion support

---

# 🔐 Future Improvements

- JWT Authentication
- API Key protection
- Pagination support
- Search functionality
- S3 static frontend hosting
- CloudFront CDN
- Terraform infrastructure as code
- CI/CD pipeline integration
- CloudWatch alarms

---

# 🏆 Key Learnings

- Serverless architecture design
- API Gateway routing and CORS configuration
- Lambda proxy event structure
- DynamoDB key design considerations
- Handling Decimal type in Python
- Debugging silent database update failures
- Production-grade API setup

---

# 🎯 Conclusion

This project demonstrates a complete serverless application built using AWS cloud-native services.

It highlights backend development, cloud architecture, security implementation, monitoring, and real-world debugging experience.

---

# 👨‍💻 Author
Salman Sayeed, MSc - salmansohailuk@gmail.com
AWS | Azure | GCP | DevOps | Serverless Architect
