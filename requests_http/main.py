import requests
import os

base_url = 'https://akabab.github.io/superhero-api/api/'
all = base_url + 'all.json'

resp = requests.get(all)

def brainest(heroes_input_list):
    superhero_list = resp.json()
    heroes_compare = {}
    for hero in superhero_list:
        if hero['name'] in heroes_input_list:
            heroes_compare[hero['name']] = hero['powerstats']['intelligence']

    winner = max(heroes_compare, key=heroes_compare.get)  #Не сработает, если будут одинаковые значения
    winner_score = heroes_compare[winner]
    winners = {}
    for k, v in heroes_compare.items():
        if v == winner_score:
            winners[k] = v
    print('The brainest superhero(es):')
    return winners

print(brainest(['Hulk', 'Captain America', 'Thanos']))

#Задача 2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        href = response.json().get('href', '')
        send_to_cloud = requests.put(href, data=open(file_path, 'rb'))

file_name = 'list.txt'
files_dir = ''
root_path = os.getcwd()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(root_path, files_dir, file_name)
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)