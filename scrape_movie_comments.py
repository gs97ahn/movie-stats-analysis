from config.config import Config
from utils.data_formatter import DataFormatter
from utils.movie_comments_scraper import MovieCommentsScraper

import os

config = Config()
data_formatter = DataFormatter()
movie_comments_scraper = MovieCommentsScraper()


def load_movie_ratio():
    m_r_file = os.listdir(config.p_movie_statistics_folder_path)
    m_r_data = data_formatter.csv_reader(config.p_movie_statistics_folder_path + m_r_file[0])
    return m_r_data


def get_movie_comments(movie_ratio):
    if not os.path.isdir(config.c_movie_comments_folder_path):
        os.makedirs(config.c_movie_comments_folder_path)
    for i in range(15, len(movie_ratio)):
        print('\n\n******************************')
        print('**********', movie_ratio['title'][i], '**********')
        print('******************************\n')
        m_id = movie_comments_scraper.search_by_title(movie_ratio['title'][i])
        m_comments = movie_comments_scraper.scrape_comments(m_id)
        if movie_ratio['result'][i] == 1:
            r = 'pos'
        else:
            r = 'neg'
        data_formatter.csv_writer(
            config.c_movie_comments_folder_path + config.csv_filename.replace('*', movie_ratio['title'][i] + '_' + r),
            ['comments'],
            m_comments
        )


if __name__ == '__main__':
    m_r_d = load_movie_ratio()
    get_movie_comments(m_r_d)
