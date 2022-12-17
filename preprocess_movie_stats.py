from config.config import Config
from utils.data_formatter import DataFormatter

import os

config = Config()
data_formatter = DataFormatter()


def load_movie():
    m_filenames = os.listdir(config.c_movie_statistics_folder_path)
    m_data = dict()
    for f in m_filenames:
        m_data[f.replace('.csv', '')] = data_formatter.csv_reader(config.c_movie_statistics_folder_path + f)
    return m_data


def calculate_stats(movie_data):
    m_stats = list()
    for key, value in movie_data.items():
        print('\n**********', key, '**********')
        c_cnt, r_all, r_kor = 0, 0, 0
        for i in range(len(value)):
            if (value['country'][i] not in config.oecd_countries) and (value['country'][i] not in config.g20):
                continue
            elif value['country'][i] == 'South Korea':
                r_kor = value['ratio'][i]
            else:
                r_all += value['ratio'][i]
                c_cnt += 1

        if r_kor >= r_all/c_cnt:
            res = 1
        else:
            res = 0
        m_stats.append([key, r_all/c_cnt, r_kor, res])
        print(key, r_all/c_cnt, r_kor, res)
    print()
    return m_stats


def save_data(movie_data):
    if not os.path.isdir(config.p_movie_statistics_folder_path):
        os.makedirs(config.p_movie_statistics_folder_path)
    data_formatter.csv_writer(
        config.p_movie_statistics_folder_path + config.csv_filename.replace('*', 'movie_ratio_stats'),
        ['title', 'World', 'KOR', 'result'],
        movie_data
    )


if __name__ == '__main__':
    m_d = load_movie()
    m_s = calculate_stats(m_d)
    save_data(m_s)

