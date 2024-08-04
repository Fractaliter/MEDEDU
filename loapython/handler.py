import json
import boto3
from botocore.exceptions import ClientError

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def get_patient(event, context):
    table = dynamodb.Table('Patients')
    patient_id = event['pathParameters']['id']

    try:
        response = table.get_item(
            Key={
                'PatientID': patient_id
            }
        )
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    if 'Item' in response:
        return {
            "statusCode": 200,
            "body": json.dumps(response['Item'])
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Patient not found"})
        }
