import json


def lambda_handler(event, context):
    body = json.loads(event["body"])
    isinslotfilling = body["isInSlotFilling"]
    utterance = body["utterance"]
    value = body["value"]
    user = body["user"]

    r_value = value["resolved"]


    if r_value == "국밥" or r_value == "라면" or r_value == "중식":
        response = {
            "status": "FAIL",
            "message": "{}의 종류를 정확히 써주세요.".format(r_value)
        }
    else:
        response = {
            "status": "SUCCESS"
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
