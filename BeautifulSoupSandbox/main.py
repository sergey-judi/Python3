import json

import requests
import re
from bs4 import BeautifulSoup

HOST = 'https://zno.osvita.ua/'
URL = 'https://zno.osvita.ua/mathematics/384/'
SUBJECT_URLS = [
    'https://zno.osvita.ua/ukrainian/',
    'https://zno.osvita.ua/mathematics/',
    'https://zno.osvita.ua/ukraine-history/',
    'https://zno.osvita.ua/geography/',
    'https://zno.osvita.ua/biology/',
    'https://zno.osvita.ua/physics/',
    'https://zno.osvita.ua/chemistry/',
    'https://zno.osvita.ua/english/',
    'https://zno.osvita.ua/german/',
    'https://zno.osvita.ua/french/',
    'https://zno.osvita.ua/spanish/'
]
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
        if any(map(str.isdigit, letters)):
            letters_num = len(list(filter(lambda x: x.isalpha(), letters)))
            letters_table = [letter for letter in letters if letter.isdigit()]
            answers_table = []
            for i in range(len(letters)):
                answers_table.append(dict(zip(letters, answers[i*letters_num:(i+1)*letters_num])))
            letters = letters_table
            answers = answers_table

        task_dict = dict(zip(letters, answers))
        if all(map(lambda x: not x, task_dict.values())):
            return None
        else:
            return task_dict


def get_answers_schema(answers):
    answers_len = list(map(lambda x: len(x.values()), answers))
    schema_index = answers_len.index(max(answers_len))
    return list(answers[schema_index].keys())


def get_right_answer(test_answer):
    answers_table = dict()

    for letter, picked in test_answer.items():
        if 'ok' in picked:
            return letter
        if letter.isdigit():
            answers_table[letter] = get_right_answer(picked)

    return answers_table


def get_count_dict(answers, schema):
    answers_dict = dict((letter, 0) for letter in schema)

    for answer in answers:
        right_answer = get_right_answer(answer)
        if isinstance(right_answer, dict):
            for letter in right_answer.values():
                if letter:
                    answers_dict[letter] += 1
        elif right_answer.isalpha():
            answers_dict[right_answer] += 1

    return answers_dict


def get_urls(host):
    html = get_html(host).text

    soup = BeautifulSoup(html, 'lxml')
    li_items = soup.find_all('li', {'class': 'test-item'})

    test_urls = []
    for li_item in li_items:
        test_url = host + li_item.find('a').get('href').split('/')[-2] + '/'
        spans = li_item.find_all('span')
        test_year = spans[0].get_text(strip=True).split()[0]
        test_type = spans[-1].get_text(strip=True)
        test_urls.append(
            {
                "url": test_url,
                "year": test_year,
                "type": test_type
            }
        )

    subject = host.split('/')[-2]
    file_name = subject + '.json'

    with open('test_urls/' + file_name, mode='w') as file:
        json.dump(test_urls, file, indent=4, ensure_ascii=False)


def parse(url, from_file=True):
    if from_file:
        with open('test.html', encoding='utf-8') as file:
            html = file.read()
    else:
        html = get_html(url).text

    answers = []

    for task in get_tasks(html):
        if s := get_answers(task):
            answers.append(s)

    tasks_num = len(answers)
    print(f'Total tasks done: {tasks_num}')

    schema = get_answers_schema(answers)
    print(f"Answers' schema: {schema}")

    count_dict = get_count_dict(answers, schema)
    print(f'Counted answers: {count_dict}')

    return count_dict


def save_page(url):
    html = get_html(url)
    if html.status_code == 200:
        with open('index.html', mode='w', encoding='utf-8') as file:
            file.write(html.text)
    else:
        raise Exception('Was not able to connect to the specified url')


if __name__ == '__main__':
    for subject_url in SUBJECT_URLS:
        get_urls(subject_url)
    # save_page(URL)
    # parse(URL)
