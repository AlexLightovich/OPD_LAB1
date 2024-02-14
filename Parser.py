from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import ssl



def parse():
    facultets = []
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    if soup.find('div', class_='main__content'):
        block = soup.find('div', class_='main__content').findAll('li') # находим  контейнер с нужным классом
        for data in block: # проходим циклом по содержимому контейнера
            if data.find('span'): # находим тег <p>
                facultetName = data.find('a').text
                print(facultetName)
                facultets.append(facultetName)
    print("Parsing done! Writing in file....")
    writeInFile(facultets)
def writeInFile(data):
    f = open('test.txt', 'w')
    for facult in data:
        f.write(facult+"\n")
    f.close()
    print("Wrote in file!")
