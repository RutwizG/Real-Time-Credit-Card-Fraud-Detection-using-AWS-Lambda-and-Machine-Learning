# 💳 Real-Time Credit Card Fraud Detection using AWS Lambda & Machine Learning

This project demonstrates a real-time, scalable credit card fraud detection pipeline built using **AWS Lambda**, **S3**, **API Gateway**, and a **pre-trained machine learning model**. The goal is to detect suspicious transactions as they happen and immediately flag them for review — helping financial institutions reduce fraud-related losses and improve customer trust.

---

## 📌 Why This Project?

Fraud detection is a critical use case in fintech, requiring both high accuracy and fast response times. This solution leverages **serverless architecture** and **lightweight ML models** to build a reactive and cost-effective fraud detection pipeline. It mimics production-scale systems in banks and financial platforms.

---

## ⚙️ Architecture Overview

Client/API ➜ API Gateway ➜ AWS Lambda ➜ Model Inference (via S3 or EFS) ➜ Response (Fraud or Not Fraud)

markdown
Copy code

### 🧠 How It Works:

1. **Transaction Data** is submitted via API Gateway.
2. **AWS Lambda** triggers on request and loads the ML model.
3. The transaction is passed into the model for real-time prediction.
4. If flagged as "fraudulent," an alert is generated (via email/SNS/DB).

---

## 🚀 Tech Stack

- **AWS Lambda** – Serverless compute for model inference  
- **Amazon S3** – Model storage (pickled/scikit-learn model)  
- **AWS API Gateway** – Secure REST endpoint for inference calls  
- **AWS SNS / DynamoDB (Optional)** – For real-time alerting or logging  
- **Python 3.9** – Main programming language  
- **scikit-learn** – ML model development (Random Forest / Logistic Regression)  
- **Jupyter Notebook** – Exploratory Data Analysis & Model Training  

---

## 📊 Model Details

- **Dataset**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
- **Total Records**: 284,807 transactions  
- **Fraud Cases**: ~0.17% of total (highly imbalanced)  
- **Model Used**: Random Forest Classifier  
- **Preprocessing**:
  - Feature scaling with `StandardScaler`
  - SMOTE for balancing the training data
  - AUC-ROC optimization for threshold tuning

---

## 📦 Project Structure

.
├── lambda_function/
│ ├── app.py # Lambda function for model inference
│ └── model.pkl # Pre-trained fraud detection model
├── notebooks/
│ └── training.ipynb # EDA and ML model training
├── api/
│ └── test_postman.json # Sample POST request with transaction
├── requirements.txt # Dependencies for Lambda deployment
├── README.md


---

📈 Results & Performance
Accuracy: 99.2%

Recall (Fraud): 92.4%

Latency: ~200ms average per request on AWS Lambda

Cost: ~Free Tier eligible for low volumes due to Lambda + S3 combo

🔐 Security & Scalability
API secured with AWS API Keys or Cognito

Supports horizontal scaling by design (via Lambda)

Easily extendable with AWS Step Functions, SQS, or Aurora for logs

📬 Future Enhancements
✅ Integrate alerting with Slack / SMS via AWS SNS

✅ Store flagged transactions in DynamoDB for analytics

🔄 Switch to SageMaker endpoint for low-latency batch inference

🧠 Add anomaly detection model for unseen fraud types

👨‍💻 Author
Rutwiz Gullipalli
💻 Software & Systems Enthusiast    
