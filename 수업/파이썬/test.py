import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

# API 요청
response = requests.get(API_URL)

# JSON -> dict 데이터 변환
parsed_data = response.json()
data_list = list(parsed_data)
dummy_data = []
censored_user_company = []
censored_user_name = []
censored_user_list = []

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

# 실습 3 결과 6팀
for i in range(len(data_list)):
    company = (data_list[i]['company']['name'])
    lat = (data_list[i]['address']['geo']['lat'])
    lng = (data_list[i]['address']['geo']['lng'])
    name = (data_list[i]['name'])
    dummy_list = {'company': company, 'lat': lat, 'lng' : lng, 'name' : name}
    if float(lat) < 80 and float(lat) > -80 and float(lng) < 80 and float(lng) > -80 :
        dummy_data.append(dummy_list)

   
# def censorship(user):
#    for i in range(len(black_list)):
#        if censored_user_list.keys() != black_list :

    

def create_user(dummy_data):
    for i in range(len(dummy_data)):
        company = dummy_data[i]['company']
        name = dummy_data[i]['name']
        censored_user_company.append(company) 
        censored_user_name.append(name)

    censored_user_list = dict(zip(censored_user_company, censored_user_name))
    print(censored_user_list)
    print(censored_user_list.keys())
    print(censored_user_list.values())

#    censorship()

    return censored_user_list


create_user(dummy_data)
