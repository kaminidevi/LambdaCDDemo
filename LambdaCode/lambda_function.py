import boto3
import json
import base64

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.get_metric_widget_image(
        MetricWidget = json.dumps(
            {
                "view": "timeSeries",
                "stacked": False,
                "metrics": [[ "AWS/Lambda", "Duration", "FunctionName", "indlasdemo2-saaLambdaCheckOpenDevices-KSHBXB8JWNK6" ]],
                "width": 1054,
                "height": 180,
                "start": "-PT3H",
                "end": "P0D"
                }
                ))
    #OutputFormat = "png"
    #print(response.keys())
    return {
        "statuscode" : 200,
        "body" : base64.b64encode(response['MetricWidgetImage']).decode(encoding='utf-8'),
        "isBase64Encoded": False,
        }         
