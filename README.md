# INU_Cafeteria

**학식크롤러 카카오톡 스킬 봇 (v1.1)**
**AWS lambda**

**카카오톡 채널 @inu_food**


입력한 날짜(이번주 식단내)의 식사표를 출력해줍니다.<br><br><br>



**현재 구현된 기능**:

**날짜별 메뉴출력(daymenu_show)** **특정 날짜, 특정 시간 메뉴 출력(typemenu_show) // ex) 7월 10일 중식 알려줘**

![ezgif-1-3c0e25c981aa](https://user-images.githubusercontent.com/41959969/125241348-491f9100-e326-11eb-80a5-b386fef2f5fb.gif) ![ezgif-1-1d72dd49f3a7](https://user-images.githubusercontent.com/41959969/125269142-644cc980-e343-11eb-88ec-5a5d5d5b8677.gif)
 <br><br><br>
 
 **PATCH NOTE**
 
v1.0 : 날짜별 메뉴출력(엔티티 포함) ex) 월요일 메뉴 알려줘, 내일 메뉴 알려줘

v1.1 : 날짜별 개별메뉴 출력(엔티티 포함) ex) 월요일 중식 알려줘, 내일 석식 알려줘, 내일 라면 알려줘
       <br>aws lambda function github에 추가
<br><br><br>
**앞으로 구현할 기능**:

**먹었던 메뉴 저장(menu_save) - 히스토리 관리 기능 // ex) 오늘 중식 먹었어. -> 해당 날짜의 중식을 히스토리에 저장**



