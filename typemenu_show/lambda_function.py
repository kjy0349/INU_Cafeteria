import json
from bs4 import BeautifulSoup
import crawling_INUmenu as im


def lambda_handler(event, context):
    menu_type_list = ["중식", "중식", "석식", "라면", "국밥"]
    request_body = json.loads(event["body"], encoding="utf-8")
    action = request_body["action"]

    # 날짜 출력
    date_obj = json.loads(action["params"]["date"])
    date = date_obj["date"]
    date = int(date[5:].replace('-', ''))
    diff_index = im.today_index + date - im.short_date
    day = action["detailParams"]["date"]["origin"]

    # 요청한 메뉴 시간

    request_typemenu = action["params"]["menu_type"]
    tm_index = 0
    for i in range(len(menu_type_list)):
        print(i, menu_type_list[i], request_typemenu)
        if menu_type_list[i] == request_typemenu:
            tm_index = i
            break

    # 요청한 메뉴 출력

    typemenu_show_str = ""
    typemenu_show_str += "{} {} 메뉴\n\n".format(day, request_typemenu)
    if tm_index == 0 or tm_index == 1:
        typemenu_show_str += "중식(백반)\n"
        for i in range(len(im.all_menu_list[diff_index][0])):
            typemenu_show_str += "{}\n".format(im.all_menu_list[diff_index][0][i])
        typemenu_show_str += "\n중식(일품) \n"
        for i in range(len(im.all_menu_list[diff_index][1])):
            typemenu_show_str += "{}\n".format(im.all_menu_list[diff_index][1][i])

    else:
        for i in range(len(im.all_menu_list[diff_index][tm_index])):
            typemenu_show_str += "{}\n".format(im.all_menu_list[diff_index][tm_index][i])

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "{}".format(typemenu_show_str)
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

