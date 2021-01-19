import data_provider
import pandas as pd

SUBJECT_URLS = data_provider.SUBJECT_URLS


def main():
    for subject_url in SUBJECT_URLS:
        data_folder_name = 'csv-data'
        subject_name = data_provider.get_folder_name(subject_url)
        path_to_csv = data_folder_name + '/' + subject_name + '.csv'

        with open(path_to_csv, mode='r', encoding='utf-8') as file:
            header = file.readline().strip().split(',')

        data = pd.read_csv(path_to_csv)
        df = pd.DataFrame(data, columns=header)
        df.fillna(0, inplace=True)

        print('{0:-^20}'.format(subject_name))
        print('{0} {1:>5} {2:>5} {3:>5}'.format(' ', 'Avg', 'Min', 'Max'))
        for letter in header[1:]:
            print('{0} {1:>5.1f} {2:>5} {3:>5}'.format(letter, df[letter].mean(), df[letter].min(), df[letter].max()))
        print()


if __name__ == '__main__':
    main()
