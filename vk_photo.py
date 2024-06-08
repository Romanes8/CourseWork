import requests
from datetime import datetime


#класс VK_photo принимает на вход VK токен, получает и формирует в виде списка словарей информацию о фотографиях, необходимую для загрузки фото на Яндекс Диск.
class VK_photo:
    def __init__(self, vk_token):
        self.vk_token = vk_token

    #метод получения информации о фотографиях из VK
    def get_photo(self, user_ids, count, album_id):
        url_vk = 'https://api.vk.com/method/photos.get'
        params = { 'owner_id': user_ids,
                   'album_id': album_id,
                   'access_token': self.vk_token,
                   'extended': 1,
                   'count': count,
                   'v': '5.199'
                  }
        self.response = requests.get(url=url_vk, params=params).json()
        return self.response

    # метод формирования списков словарей с нужными параметрами фотографий
    def photo_info(self, user_ids, count, album_id):
        parameters_list = []
        response = self.get_photo(user_ids, count, album_id)
        items = response['response']['items']
        for el in items:
            list_sizes = []
            for sizes in el['sizes']:
                size_fhoto = sizes['height']*sizes['width']
                list_sizes.append(size_fhoto)
            list_sizes_sorted = sorted(list(enumerate(list_sizes)), reverse=True, key=lambda x: x[1])
            parameters_dict = {'likes': el['likes']['count'],
                               'date': str(datetime.fromtimestamp(el['date']))[0:10],
                               'url': el['sizes'][list_sizes_sorted[0][0]]['url'],
                               'size': el['sizes'][list_sizes_sorted[0][0]]['type']
                               }
            parameters_list.append(parameters_dict)
        likes_list = []
        json_report_list = []
        info_foto_for_yan = []
        for el in parameters_list:
            likes_list.append(dict['likes'])
        for el in parameters_list:
            if el['likes'] in likes_list:
                name = f"{el['likes']}.jpg_{el['date']}"
            else:
                name = f"{el['likes']}.jpg"
            json_dict = {"file_name": name,
                        "size": el['size']
                            }
            json_report_list.append(json_dict)
            info_dict = {'file_name': name,
                        'url': el['url']}
            info_foto_for_yan.append(info_dict)
        return json_report_list, info_foto_for_yan















