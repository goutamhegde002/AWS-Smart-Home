# AWS Smart Home Project

This project demonstrates how to integrate AWS services to create a smart home system. It uses AWS Lambda for processing events, Amazon Alexa for voice control, AWS IoT Core for device communication, and Amazon DynamoDB for storing device states.

## Project Structure

```
smart-home-aws/
│
├── lambda/
│   └── lambda_function.py
│
├── iot/
│   └── iot_rule.json
│
└── dynamodb/
    └── dynamodb_table.json

```


## Components

### 1. AWS Lambda Function

The Lambda function processes events and interacts with AWS services.

**`lambda_function.py`**:
```python
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
```
### 2. Amazon Alexa Skill

The Alexa Skill is configured to use the Lambda function for voice control.

Endpoint: Use the ARN of your Lambda function.

Interaction Model: Define intents and sample utterances to control your smart home devices.

### 3. AWS IoT Core

AWS IoT Core handles device communication and triggers the Lambda function based on device events.

**`iot_rule.json`**

```json
{
  "sql": "SELECT * FROM 'smart_home/+/status'",
  "ruleDisabled": false,
  "actions": [
    {
      "lambda": {
        "functionArn": "arn:aws:lambda:region:account-id:function:your-function-name"
      }
    }
  ]
}
```
### 4. Amazon DynamoDB

Amazon DynamoDB stores the states of your smart home devices.

**`dynamodb_table.json`**

```json
{
  "TableName": "SmartHomeDevices",
  "KeySchema": [
    {
      "AttributeName": "deviceId",
      "KeyType": "HASH"
    }
  ],
  "AttributeDefinitions": [
    {
      "AttributeName": "deviceId",
      "AttributeType": "S"
    }
  ],
  "ProvisionedThroughput": {
    "ReadCapacityUnits": 5,
    "WriteCapacityUnits": 5
  }
}
```
## How to Use

### AWS Lambda
1. Go to the [AWS Lambda console](https://console.aws.amazon.com/lambda/home).
2. Create a new function and upload `lambda_function.py`.
3. Set the function's role and permissions.

### Amazon Alexa
1. Create a new Alexa skill in the [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask).
2. Set the skill's endpoint to the Lambda function's ARN.
3. Define intents and sample utterances.

### AWS IoT Core
1. Create a new IoT Thing and configure it.
2. Create a rule using `iot_rule.json` and attach it to your Lambda function.

### Amazon DynamoDB
1. Go to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home).
2. Create a table using `dynamodb_table.json`.

## Deployment

To deploy these resources, you can use AWS CloudFormation for infrastructure as code or deploy manually using the AWS Management Console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Notes

- Ensure you have the necessary permissions and roles set up for Lambda, IoT Core, and DynamoDB.
- Adjust the device communication rules and DynamoDB schema based on your specific smart home setup.

Feel free to adjust any specific details or instructions according to your project's needs!
