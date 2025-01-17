import csv
import os
import zno_driver
import zno_parser

HOST = 'https://zno.osvita.ua/'
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


def save_html(url, path_to_file):
    try:
        if not os.path.exists(path_to_file):
            html = zno_driver.get_html(url)
            with open(path_to_file, mode='w', encoding='utf-8') as file:
                file.write(html)
            print(f'Successfully saved page {url}')
    except Exception as e:
        print(f'Page {url} was not saved')


def parse_html(path_to_file, output=False):
    with open(path_to_file, mode='r', encoding='utf-8') as file:
        html = file.read()
    return zno_parser.parse(html, output)


def get_file_name(test):
    subject_name = get_folder_name(test['url'][:-1])
    file_name = subject_name + '-' + test['year'] + '-' + test['type']
    return file_name


def get_folder_name(subject_url):
    url_split = subject_url.split('/')
    folder_name = url_split[-2]
    return folder_name


def save_csv(data, path_to_file):
    header = zno_parser.get_answers_schema(data)
    with open(path_to_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(data)


def update_data(output=False):
    for subject_url in SUBJECT_URLS:
        tests = zno_parser.get_urls(subject_url)
        # print(json.dumps(urls, indent=4, ensure_ascii=False))
        all_answers = []
        for test in tests:
            folder_name = get_folder_name(subject_url)
            file_name = get_file_name(test)
            path = folder_name + '/' + file_name + '.html'

            if output: print(file_name)

            save_html(test['url'], path)
            answers = parse_html(path, output)
            all_answers.append(dict({'Тест': file_name}, **answers))

            if output: print('---------------------------')

        data_folder_name = 'csv-data'
        subject_name = get_folder_name(subject_url)
        path_to_csv = data_folder_name + '/' + subject_name + '.csv'

        save_csv(all_answers, path_to_csv)


if __name__ == '__main__':
    update_data(True)
