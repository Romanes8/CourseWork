import requests
import json


# функция ввода исходных данных, возвращает значения переменных VK токена,
# ID пользователя VK, токена Яндекс Диска, количества фотографий, параметра 'album_id'
def input_data():
    vk_token = input("Введите токен VK: ")
    user_id = input("Введите user id VK: ")
    while user_id.isdigit() == False:
        print('Недопустимое значение, введите корректный user id.')
        user_id = input("Введите user id VK: ")
    user_ids = int(user_id)
    Yan_token = input("Введите токен Яндекс Диска: ")
    count_fhoto = input("Укажите количество загружаемых фотографий(по умолчанию 5 фотографий): ")
    if count_fhoto == '':
        count = 5
        print('На Яндекс Диск загрузится 5 фотографий.')
    else:
        while count_fhoto.isdigit() == False:
            print('Недопустимое значение, введите целое число.')
            count_fhoto = input("Укажите количество загружаемых фотографий(по умолчанию 5 фотографий): ")
        count = count_fhoto
    input_album_id = input("Введите 1 - скачать фотографии профиля ('profile'); 2 - скачать фотографии со стены ('wall'): ")
    while input_album_id not in ['1', '2']:
        print('Такого варианта нет.')
        input_album_id = input("Введите 1 - скачать фотографии профиля ('profile'); 2 - скачать фотографии со стены ('wall'): ")
    if input_album_id == '1':
        album_id = 'profile'
    elif input_album_id == '2':
        album_id = 'wall'
    return vk_token, user_ids, Yan_token, count, album_id


#функция для выгрузки файла отчета
def json_info(parameters_list):
    json_list_js = json.dumps(parameters_list)
    with open('upload_report.json', 'w') as f:
        f.write(json_list_js)






