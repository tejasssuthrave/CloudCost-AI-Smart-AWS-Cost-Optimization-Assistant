# 🚀 CloudCost AI – Smart AWS Cost Optimization Assistant

A serverless, AI-powered FinOps system that monitors AWS usage, analyzes costs, and provides intelligent optimization recommendations with real-time alerts.

---

## 📌 Overview

Managing cloud costs without visibility is risky. This project provides a complete solution to track, analyze, and optimize AWS spending using a modern serverless architecture.

It integrates cost analytics, AI insights, and alerting mechanisms into a single dashboard.

---

## 💡 Key Features

- 📊 **Daily Cost Trend Analysis**  
  Visualize AWS spending over time

- 🧾 **Service-wise Cost Breakdown**  
  Identify cost usage across services like EC2, S3, Lambda, RDS, etc.

- 🤖 **AI-Powered Recommendations**  
  Uses Google Gemini API to generate optimization suggestions

- 🧠 **Rule-Based Fallback System**  
  Ensures reliability if AI API fails

- 🚨 **Automated Alerts (SNS)**  
  Sends email notifications when cost exceeds threshold

- 📉 **Edge Case Handling**  
  Handles zero-cost, negative billing, and anomalies

- 💻 **Interactive Dashboard**  
  Built using JavaScript and Chart.js for visualization

- ⚡ **100% AWS Free Tier Compatible**

---

## 🛠️ Tech Stack

- AWS Lambda  
- AWS Cost Explorer  
- Amazon SNS  
- API Gateway (REST API)  
- Google Gemini API  
- JavaScript (Frontend)  
- Chart.js  

---

## 🏗️ Architecture
<img width="1536" height="1024" alt="ChatGPT Image Mar 30, 2026, 11_33_08 AM" src="https://github.com/user-attachments/assets/9bf2d2c2-5d10-443f-8ff6-95c87e13ee26" />


---

## 🔄 Workflow

1. Fetch cost data from AWS Cost Explorer  
2. Process and clean data in Lambda  
3. Generate AI-based insights using Gemini  
4. Apply rule-based fallback logic if needed  
5. Trigger alerts via SNS  
6. Send processed data to frontend via API Gateway  
7. Display insights in dashboard  

---

## 📂 Project Structure
📁 project-root
┣ 📄 lambda_function.py
┣ 📁 frontend/
┃ ┣ 📄 index.html
┃ ┣ 📄 script.js
┃ ┗ 📄 style.css
┣ 📄 architecture.png
┗ 📄 README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/your-username/cloudcost-ai.git

cd cloudcost-ai

---

### 2️⃣ Deploy Lambda Function

- Create Lambda function
- Upload `lambda_function.py`
- Add environment variables:
- GEMINI_API_KEY=your_key
SNS_TOPIC_ARN=your_topic_arn

---

### 3️⃣ Configure Permissions

Attach IAM permissions:
ce:GetCostAndUsage
sns:Publish

---

### 4️⃣ Setup SNS

- Create SNS topic  
- Add email subscription  
- Confirm subscription  

---

### 5️⃣ Deploy API Gateway

- Create REST API  
- Connect to Lambda  
- Deploy stage  

---

### 6️⃣ Run Frontend

- Open `index.html`  
- Connect API endpoint  

---

## 🔥 Highlights

- Serverless & scalable architecture  
- Fault-tolerant AI integration  
- Real-world FinOps use case  
- Lightweight and efficient design  

---

## 💡 What I Learned

- Designing fault-tolerant systems  
- Implementing FinOps principles  
- Handling real AWS billing data  
- Building full-stack serverless applications  
- Importance of cost monitoring in DevOps  

---

## 🚀 Future Enhancements

- 🔍 Anomaly detection (cost spikes)  
- 📈 Cost prediction using ML  
- 🌍 Multi-cloud support (Azure, GCP)  
- 📱 Mobile-friendly dashboard  

---

## 📌 Status

✅ Completed and deployed  

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📬 Contact

If you have any feedback or suggestions, feel free to connect!

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!


