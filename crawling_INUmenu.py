from bs4 import BeautifulSoup  # 크롤링을 위해 bs4 라이브러리 사용
from urllib.request import urlopen
import sys

print(sys.version)
today_menu_list = [[[],[],[],[],[]]]
not_today_menu_list = []
for i in range(6): # 첫번째 인덱스를 요일, 두번째 인덱스를 메뉴 시간, 세번째 인덱스를 메뉴 시간별 세부 메뉴를 가진 3차원 배열
    line = []
    not_today_menu_list.append(line)
    for j in range(5):
        line = []
        not_today_menu_list[i].append(line)

def find_td(selected_menu, result_list,real_index):
    index = 0
    for menu_sub_list in selected_menu:  # select는 상단의 코드에서 복수의 td들을 ResultSet(일종의 List형태)로 가져오므로, 반복문을 통해서 각각의 요소들을 get_text()로 처리해줘야함
        oneday_menuplan = menu_sub_list.get_text().split('\n')  # 한칸에 모든 메뉴가 \n으로 나누어져있음
        for j in range(len(oneday_menuplan)):
            if (oneday_menuplan[j] is '\r' or  # 메뉴가 게재된칸에는 가격정보와 제공시간이 적혀있으므로, 메뉴만 얻기위해 예외처리
                    oneday_menuplan[j][0] is '*' or
                    oneday_menuplan[j][0] is '[' or
                    oneday_menuplan[j][0] is '(' or
                    oneday_menuplan[j][0] is '❝'
            ):
                break
            elif oneday_menuplan[j][0] is '<':  # <즉석조리기기>칸의 라면 메뉴들을 가져오기위한 예외처리
                continue
            else:
                if '국밥' in oneday_menuplan[j]:  # 국밥칸에서 칼로리 정보를 제외하고 메뉴 이름만 가져오기위한 예외처리
                    result_list[index][real_index].append(oneday_menuplan[j][:4].strip())
                else:
                    result_list[index][real_index].append(oneday_menuplan[j].strip())
        index += 1



url = "https://www.uicoop.ac.kr/main.php?mkey=2&w=2&l=1"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")  # 원하는 태그 정보를 뽑아줄 bs4 인스턴스 생성
index = 0
index1 = 0
Today_served = False

for tr_menu in soup.find(id='menuBox').find_all('tr'):  # menuBox라는 이름을 가진 테이블에서 한줄씩 뽑아냄
    not_today_menu = tr_menu.select('.din_list')
    today_menu = tr_menu.select('.din_lists')

    if not_today_menu:  # 찾은 내용이 있을 경우
        find_td(not_today_menu, not_today_menu_list, index)
        index += 1

    if today_menu:
        find_td(today_menu, today_menu_list, index1)
        index1 += 1

for i in range(len(not_today_menu_list)):
    print(not_today_menu_list[i])
print('오늘 메뉴', today_menu_list)
