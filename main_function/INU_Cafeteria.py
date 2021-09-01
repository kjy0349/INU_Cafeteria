import json
import time
import crawling_INUmenu as im


def lambda_handler(event, context):
    # 메시지 내용은 request의 ["body"]에 들어 있음
    request_body = json.loads(event["body"], encoding="utf-8")
    action = request_body["action"]

    # 날짜 보정
    month_to = ["1", "3", "5", "7", "8", "10", "12"]

    # 날짜 출력
    date_obj = json.loads(action["params"]["date"], encoding="utf-8")
    date = date_obj["date"]
    date = int(date[5:].replace('-', ''))
    if date // 10 ** 2 != im.short_date // 10 ** 2:
        if date // 10 ** 2 in month_to:
            date += 68
        else:
            date += 69
    diff_index = im.today_index + date - im.short_date
    day = action["detailParams"]["date"]["origin"]

    # 요청한 메뉴 출력
    that_day_menu_str = ""
    that_day_menu_str += "{} 메뉴\n\n".format(day)
    print(im.today_index, date, im.short_date)
    try:
        for j in range(len(im.all_menu_list[diff_index])):
            that_day_menu_str += "{}\n".format(im.menuTime[j])
            for k in range(len(im.all_menu_list[diff_index][j])):
                if k == len(im.all_menu_list[diff_index][j]) - 1:
                    that_day_menu_str += "{}".format(im.all_menu_list[diff_index][j][k])
                else:
                    that_day_menu_str += "{}\n".format(im.all_menu_list[diff_index][j][k])
            if j == len(im.all_menu_list[diff_index]) - 1:
                break
            else:
                that_day_menu_str += "\n \n"
    except:
        print(im.all_menu_list)

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "{}".format(that_day_menu_str)
                    }
                }
            ]
        }
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": {
            "Access-Control-Allow-Origin": "*",
        }
    }

