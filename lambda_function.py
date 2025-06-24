import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from io import StringIO
import boto3

# Initialize AWS S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Read the CSV file from S3
    bucket_name = 'credit-fraud-rlt'  # Replace with your S3 bucket name
    file_key = 'creditcard.csv'  # Replace with your file path in S3
    
    response = s3.get_object(Bucket=credit-fraud-rlt, Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')
    
    # Load CSV into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_content))
    
    # Feature Engineering: amount spike, high risk time, etc.
    df['amount_spike'] = df['amount'] > 500  # Flag if transaction amount is greater than 500
    df['high_risk_time'] = df['timestamp'].apply(lambda x: 'night' if int(x.split()[1].split(':')[0]) > 18 else 'day')
    
    # Model: Load the pre-trained fraud detection model (this model is pre-trained and uploaded to S3)
    # For simplicity, we have a pre-trained RandomForest model
    # train in AWS SageMaker and use it here
    model = RandomForestClassifier(n_estimators=100)
    
    # Simulate some training for demo purposes (replace with your actual model training)
    X = df[['amount', 'amount_spike']]  # Example features
    y = df['fraud_label']  # Simulate fraud_label column for training
    model.fit(X, y)  # Training the model (use actual training in real scenarios)
    
    # Predict fraud (0 = Not Fraud, 1 = Fraud)
    df['predicted_fraud'] = model.predict(X)
    
    # Log suspected fraudulent transactions
    fraudulent_transactions = df[df['predicted_fraud'] == 1]
    if not fraudulent_transactions.empty:
        print("Fraudulent transactions detected:")
        print(fraudulent_transactions)
    
    # Save the processed data to S3 (optional, for storing processed data or logs)
    processed_credit = 'processed_creditcard.csv'
    df.to_csv(processed_credit, index=False)
    s3.upload_file(processed_credit, credit-fraud-rlt, f'processed/{processed_credit}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed and detected fraud successfully')
    }
