import pandas as pd
import json

def lambda_handler(event, context):
    # Sample data (you can later replace this with data from S3 or Kinesis)
    data = {
        "timestamp": "2025-06-20 19:55:00",
        "open": 281.2000,
        "high": 282.0000,
        "low": 281.2000,
        "close": 282.0000,
        "volume": 60
    }

    # Convert data to a DataFrame using Pandas
    df = pd.DataFrame([data])

    # Print out the DataFrame (you can replace this with your actual processing logic)
    print(df)

    return {
        'statusCode': 200,
        'body': json.dumps('Pandas processed successfully')
    }

