from config.config import Config
from utils.data_formatter import DataFormatter
from utils.movie_stats_scraper import MovieStatsScraper

import os

config = Config()
data_formatter = DataFormatter()
movie_stats_scraper = MovieStatsScraper()


def load_population():
    w_p_data = data_formatter.csv_reader(config.c_world_population_file_path)
    w_p_dict = dict()
    for i in range(len(w_p_data)):
        if w_p_data['country'][i] == 'Central African Republic':
            w_p_dict['Central Africa'] = int(w_p_data['pop2022'][i] * 1000)
        elif w_p_data['country'][i] == 'North Macedonia':
            w_p_dict['Macedonia'] = int(w_p_data['pop2022'][i] * 1000)
        else:
            w_p_dict[w_p_data['country'][i]] = int(w_p_data['pop2022'][i] * 1000)
    return w_p_dict


def get_movie_stats(world_population):
    if not os.path.isdir(config.c_movie_statistics_folder_path):
        os.makedirs(config.c_movie_statistics_folder_path)
    for i in range(1, 50):
        m_name, m_country_list = movie_stats_scraper.scrape_top_movies(i)
        if m_country_list is None:
            print('WARNING:', m_name, 'skipped due to no information')
            continue
        c_set = set()
        for c in range(len(m_country_list)):
            c_set.add(m_country_list[c][0])
            m_country_list[c].append(world_population[m_country_list[c][0]])
            m_country_list[c].append(m_country_list[c][1] / m_country_list[c][2])
        if 'South Korea' not in c_set:
            print('WARNING:', m_name, 'data not saved as there is no South Korean information')
            continue
        else:
            data_formatter.csv_writer(config.c_movie_statistics_folder_path + config.csv_filename.replace('*', m_name),
                                      ['country', 'total box office', 'population', 'ratio'],
                                      m_country_list)


if __name__ == '__main__':
    world_population_dict = load_population()
    get_movie_stats(world_population_dict)
