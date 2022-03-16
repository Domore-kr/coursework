import requests
import json
import yadisk


def load_ya(id, yaTOKEN, album=input('Выберите область, из которой необходимо выгрузить фотографии:'
                                     'wall — фотографии со стены,'
                                     'profile — фотографии профиля ')):
    token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'user_ids': f'{id}',
        'access_token': token,
        'v': '5.131',
        'album_id': f'{album}',
        'extended': 1,
        'photo_sizes': 1
    }
    res = requests.get(URL, params=params)
    with open(f'{id}.json', 'w') as photo:
        name_dict = {}
        name_list = []
        y = yadisk.YaDisk(token=yaTOKEN)
        y.mkdir(f"/{id}/")
        for i in res.json()['response']['items']:
            photo_params = i["likes"]["count"]
            name_dict['file_name'] = f'{photo_params}.jpg'
            name_dict['size'] = i['sizes'][-1]['type']
            name_list.append(name_dict)
            p = requests.get(i['sizes'][-1]['url'])
            out = open(f'{photo_params}.jpg', "wb")
            out.write(p.content)
            y.upload(f'{photo_params}.jpg', f"/{id}/{photo_params}.jpg'")
            out.close()
        json.dump(name_list, photo)


load_ya('begemot_korovin', '')
