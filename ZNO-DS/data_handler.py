import data_provider
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

SUBJECT_URLS = data_provider.SUBJECT_URLS


def visualize(data):
    headers = [header for header in data]
    letters = headers[1:]
    letters_num = len(letters)

    cols_num = 3
    rows_num = int(np.ceil(letters_num / cols_num))

    fig = plt.figure(figsize=(20, 20), constrained_layout=True)
    spec = gs.GridSpec(ncols=cols_num, nrows=rows_num, figure=fig)

    for i in range(rows_num):
        for j in range(cols_num):
            if (index := cols_num*i + j) < letters_num:
                ax = fig.add_subplot(spec[i, j])
                ax.barh(data[headers[0]], data[letters[index]], height=0.2)
                ax.set_title(letters[index])
                if j != 0:
                    ax.set_yticks([])
                fig.add_subplot(ax)

    plt.show()


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

        visualize(data)


if __name__ == '__main__':
    main()
