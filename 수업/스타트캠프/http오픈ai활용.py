# 1. 파이썬코드로 http 요청 보내기

import requests
import json
# requests : 패키지, 파이썬에서 http 요청을 할 수 있게 하는 기능을 모음
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : 'vSejhUQLxjOy%2FkG%2FOf3p9Qt4k8I0epSEpJrpMu4RWIO68W6pdc9%2FrmodnAhqwlkuvC08ZZHKMk%2Fabil8%2FjwrNA%3D%3D', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '경북', 'ver' : '1.0' }

response = requests.get(url, params=params)
# print(response.content)

# '공단동'에서 p,m10Grade에 해당하는 값 뽑아오기
# 응답은 전부 문자열을 그대로 데이터 처리하기는 힘들다
# { key : value, key : value} : JSON 형태를 가지고 있으니까 잘 해석하면 데이터를 뽑을 수 있음
# 문자열 파싱(구문분석)하여 객체형태로 바꾸어야한다.

data = json.loads(response.text) # json 패키지를 이용해서 json 문자열 파싱하기(파이썬에서 쓸수있는 형태로 변경)

print(data)

# data에서 items를 꺼내온다
# items에서 'stationName'이 '공단동'인 item의
# pm10Grade 가져오기

# print(data['response']['body']['items'])
items = data['response']['body']['items']
# print(items[1])
# print(items[1]['pm10Grade'])


# items를 모두 살펴보면서 동네이름이 '공단동;인 item 찾기
# List의 요소를 모두 살펴봐야한다. >> for 문법을 사용

for i in items :
    # item : 요소 하나
    # item의 동네 이름이 '공단동 찾기'
    # if item['stationName'] == '공단동' :
    #    print(f'공단동의 미세먼지 농도는 {item["pm10Value"]} 등급은 {item["pm10Grade"]}입니다')

    if i['stationName']=='공단동':
        print('공단동의 미세먼지 농도는 :{} 등급은 :{}'.format(i['pm10Value'],i['pm10Grade']))
 

# 2. 응답 받아서 화면에 출력하기



