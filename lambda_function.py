import json
import boto3

def lambda_handler(event, context):
    # Sample event processing
    print("Received event: " + json.dumps(event, indent=2))
    
    # Example response
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    return response
