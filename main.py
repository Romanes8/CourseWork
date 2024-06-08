import requests
from datetime import datetime
import json
from tqdm import tqdm
import functions as f
from vk_photo import VK_photo
from yandex import Yandex


# вызов функции ввода исходных параметров - VK токена, ID пользователя VK, токена Яндекс Диска, количества фотографий, параметра 'album_id'
vk_token, user_ids, Yan_token, count, album_id = f.input_data()

# создание объекта на основе класса VK_photo, который принимает на вход VK токен
VK_photo_info = VK_photo(vk_token)

# вызов метода photo_info из объекта VK_photo_info для получения информации о фотографиях из vk и их параметров в виде списка словарей
# json_report_list - для выгрузки отчета, info_foto_for_yan - для загрузки фото на яндекс диск
json_report_list, info_foto_for_yan = VK_photo_info.photo_info(user_ids, count, album_id)

#создание объекта на основе класса Yandex, который принимает на вход яндекс токен
VK_to_Yan = Yandex(Yan_token)

# вызов метода folder_create объекта класса Yandex для создания папки на Яндекс Диске
folder_name = VK_to_Yan.folder_create()

#Вызов метода photo_to_Yan объекта класса Yandex по загрузке фотографий на Яндекс диск, принимает на вход имя созданной папки и
#информацию о фото в виде списка славарей в формате {'file_name': имя фото, 'url': url фото}
VK_to_Yan.photo_to_Yan(folder_name, info_foto_for_yan)

#вызов функции по созданию файла отчета о загрузке фотографий, принимает на вход список словарей с выгружаемой информацией
f.json_info(json_report_list)






