import requests
from pprint import pprint as print

dummy_data = []

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 
              'Johns Group', 'Romaguera-Crona']

censored_user_list = {}

def create_user(lst):
    for a in range(len(lst)):
        if censorship(lst[a]) == True:
            censored_user_list[lst[a]['company name']] = lst[a]['name']

    return censored_user_list
        

def censorship(lst):
    for b in range(len(black_list)):
        if black_list[b] == lst['company name']:
            print('{} 소속의 {} 은/는 등록할 수 없습니다.'.format(black_list[b], lst['name']))
            return False
    
    print('이상 없습니다.')
    return True


for a in range(1, 11): 
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(a)
    response = requests.get(API_URL)
    parsed_data = response.json()

    dict_data = {'name' : parsed_data['name'], 
                 'lat' : parsed_data['address']['geo']['lat'],
                 'lng' : parsed_data['address']['geo']['lng'],
                 'company name' : parsed_data['company']['name']
                 }
    
    if int(float(dict_data['lat'])) < 80 and int(float(dict_data['lat'])) > -80 \
        and int(float(dict_data['lng'])) > -80 and int(float(dict_data['lng'])) < 80:
        dummy_data.append(dict_data)



print(create_user(dummy_data))
