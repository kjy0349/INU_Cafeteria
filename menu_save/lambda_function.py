import json
import boto3
import crawling_INUmenu as im


def lambda_handler(event, context):
    body = json.loads(event["body"])
    typemenu_list = ["중식(백반)", "중식(일품)", "석식"]
    food_name = body["action"]["params"]["food_list"]
    user_id = body["userRequest"]["user"]["id"]

    # Date and index
    date_obj = json.loads(body["action"]["params"]["sys_date"])
    date = date_obj["date"]
    date_tmp = int(date[5:].replace('-', ''))
    diff_index = im.today_index + date_tmp - im.short_date

    # food list
    food_list = []
    if typemenu_list[i] in food_name:
        for i in range(len(typemenu_list)):

            for j in range(len(im.all_menu_list[diff_index][i])):
                food_list.append(im.all_menu_list[diff_index][i][j])
    # DB insert
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FHistory')
    table.put_item(
        Item={
            'Userid': user_id,
            'Write_Date': date,
            'food_name': food_name
        }
    )

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "사용자 id: {}\n날짜 : {}, 음식이름 : {} 추가되었습니다.".format(user_id, date, food_name)
                    }
                }
            ]
        }
    }
    return {
        'statusCode': 200,
        "body": json.dumps(result, sort_keys=True, indent=4),
        "headers": {
            "Access-Control-Allow-Origin": "*",
        }
    }

