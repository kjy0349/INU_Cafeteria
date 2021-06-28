from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import time
from tqdm.notebook import tqdm

menu_list = []
menu_aday = 5 # 하루 당 메뉴 개수
is_Monday = False

for i in tqdm(range(2)):
    url = "https://www.uicoop.ac.kr/main.php?mkey=2&w=2&l=1"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    for tr_menu in soup.find(id='menuBox').find_all('tr'):
        if is_Monday is False:
            menu = tr_menu.find(class_ = 'din_lists')
            is_Monday = True
        else:
            menu = tr_menu.find(class_ = 'din_list')

        if menu:
            menu_sub_list = menu.get_text().split('\n')
            for i in range(len(menu_sub_list)):
                if(menu_sub_list[i] is '\r' or
                    menu_sub_list[i][0] is '*' or
                    menu_sub_list[i][0] is '[' or
                    menu_sub_list[i][0] is '('
                ):
                    break
                elif menu_sub_list[i][0] is '<':
                    continue
                else:
                    if '국밥' in menu_sub_list[i]:
                        print(menu_sub_list[i][:4])
                    else:
                        print(menu_sub_list[i])