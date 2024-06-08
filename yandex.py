import requests
import json
from tqdm import tqdm

#класс Yandex принимает на вход токен Яндекс Диска, создает папку на Яндекс Диске и выполняет загрузку на Яндекс Диск.
class Yandex:
    def __init__(self, Yan_token):
        self.Yan_token = Yan_token

    # метод создания папки на Яндекс Диске
    def folder_create(self):
        folder_name = input("Введите название папки для фото на Яндекс Диске: ")
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': self.Yan_token}
        params = {'path': folder_name}
        while requests.get(url=url, params=params, headers=headers).status_code == 200:
            print('Такая папка уже существует, введите другое имя.')
            folder_name = input("Введите название папки для фото на Яндекс Диске: ")
            url = 'https://cloud-api.yandex.net/v1/disk/resources'
            headers = {'Authorization': self.Yan_token}
            params = {'path': folder_name}
        else:
            print(f'Папка {folder_name} создана')
            requests.put(url=url, params=params, headers=headers)
            return folder_name

        # метод загрузки фотографий на Яндекс Диск
    def photo_to_Yan(self, folder_name, parameters_list):
        print(f'Загрузка фотографий в папку {folder_name}:')
        for el in tqdm(parameters_list):
            foto_url = el['url']
            fhoto_name = el['file_name']
            url_yn = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            headers = {'Authorization': self.Yan_token}
            params = {'url': foto_url,
                      'path': f'{folder_name}/{fhoto_name}'}
            response = requests.post(url=url_yn, params=params, headers=headers)
        print('Загрузка фотографий на Яндекс Диск завершена')