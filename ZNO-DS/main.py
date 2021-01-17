import os
import json
import zno_driver
import zno_parser

HOST = 'https://zno.osvita.ua/'
SUBJECT_URLS = [
    # 'https://zno.osvita.ua/ukrainian/',
    'https://zno.osvita.ua/mathematics/',
    # 'https://zno.osvita.ua/ukraine-history/',
    # 'https://zno.osvita.ua/geography/',
    # 'https://zno.osvita.ua/biology/',
    # 'https://zno.osvita.ua/physics/',
    # 'https://zno.osvita.ua/chemistry/',
    # 'https://zno.osvita.ua/english/',
    # 'https://zno.osvita.ua/german/',
    # 'https://zno.osvita.ua/french/',
    # 'https://zno.osvita.ua/spanish/'
]


def save_html(url, path_to_file):
    try:
        if os.path.exists(path_to_file):
            with open(path_to_file, mode='r', encoding='utf-8') as file:
                html = file.read()
        else:
            html = zno_driver.get_html(url, path_to_file=path_to_file)
            print(f'Successfully saved page {url}')
        return html
    except Exception as e:
        print(f'Page {url} was not saved')


def parse_html(path_to_file):
    with open(path_to_file, mode='r', encoding='utf-8') as file:
        html = file.read()
    return zno_parser.parse(html)


def get_file_name(test):
    subject_name = get_folder_name(test['url'][:-1])
    file_name = subject_name + '-' + test['year'] + '-' + test['type'] + '.html'
    return file_name


def get_folder_name(subject_url):
    url_split = subject_url.split('/')
    folder_name = url_split[-2]
    return folder_name


def main():
    for subject_url in SUBJECT_URLS:
        tests = zno_parser.get_urls(subject_url, from_file=True)
        # print(json.dumps(urls, indent=4, ensure_ascii=False))
        for test in tests:
            file_name = get_file_name(test)
            folder_name = get_folder_name(subject_url)
            path = folder_name + '/' + file_name
            save_html(test['url'], path)
            print(path)
            parse_html(path)
            print('---------------------------------')

if __name__ == '__main__':
    main()
