import requests
import re
from bs4 import BeautifulSoup

HOST = 'https://zno.osvita.ua/'
URL = 'https://zno.osvita.ua/mathematics/384/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_tasks(html):
    soup = BeautifulSoup(html, 'lxml')
    tasks = soup.find_all('div', {'class': re.compile('task-card')})
    return tasks


def get_answers(task):
    table = task.find('table', {'class': 'select-answers-variants'})
    if table:
        letters = [header.get_text(strip=True) for header in table.find_all('th') if header.get_text(strip=True)]
        answers = [option.get('class') for option in table.find_all('span')]
        return dict(zip(letters, answers))


def parse(url, from_file=True):
    if from_file:
        with open('index.html', encoding='utf-8') as file:
            html = file.read()
    else:
        html = get_html(url)

    tasks_num = len(get_tasks(html))
    print(f'Total number of tasks: {tasks_num}')

    for task in get_tasks(html):
        task_num = task.find('div', {'class': 'counter'}).get_text(strip=True)
        answers = get_answers(task)

        if answers and all(map(lambda x: x.isalpha(), answers.keys())):
            print(task_num)
            print(f'Answers: {answers}')


def save_page(url):
    html = get_html(url)
    if html.status_code == 200:
        with open('index.html', mode='w', encoding='utf-8') as file:
            file.write(html.text)
    else:
        raise Exception('Was not able to connect to the specified url')


save_page(URL)
parse(URL)
