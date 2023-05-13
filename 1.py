# Нужно установить бибилотеки, первую - py -m pip install lxml
# чтобы установить нужно прописать команду py -m pip install requests
import requests
#  прописать команду py -m pip install fake_useragent 
import fake_useragent
#  прописать команду py -m pip install beautifulsoup4
from bs4 import BeautifulSoup

image_number = 0
storage_number = 3
link = f"https://zastavok.net/"

# for storage in range(2769) - Обернуть все что ниже в этот цыкл для того 
# чтобы скачать картинки со всех страниц сайта (Осторожно! более 100 ГБ)
for storage in range(10):
    #Отправляем запрос на текущую станицу сайта:
    response = requests.get(f'{link}/{storage_number}').text
    soup = BeautifulSoup(response, 'lxml')
    # Ищим на ней все картинки:
    block = soup.find('div', class_ = 'block-photo')
    all_image = block.find_all('div', class_ = 'short_full')

    # Цикл на прохождение всем картинкам:
    for image in all_image:
        # Извлекаем ссылку на HTML документ картинки:
        image_link = image.find('a').get('href')
        dowloand_storage = requests.get(f'{link}{image_link}').text
        dowload_soup = BeautifulSoup(dowloand_storage, 'lxml')
        # Ищим прямой путь на скачивание:
        dowload_block = dowload_soup.find('div', class_ = 'image_data').find('div', class_ = 'block_down')
        result_link = dowload_block.find('a').get('href')
        # Отправляем запрос на этот путь:
        image_bytes = requests.get(f'{link}{result_link}').content

        #Скачиваем картинку:
        # Указываем в какую папку скачать, в данном случае папка image создана в папке с файлом кода
        with open(f'image/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)
        image_number += 1
        print(f'Изображение {image_number}.jpg успешно скачено')

        # Выше мы скачали все картинки с первой страницы, дописываем ниже инкремент на переход на следующую:
    storage_number += 1