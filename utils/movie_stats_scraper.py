from config.config import Config
from selenium import webdriver

import selenium.common.exceptions
import os
import time

config = Config()


class MovieStatsScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(os.environ['WEB_DRIVER_PATH'])

    def scrape_top_movies(self, rank):
        self.driver.get(config.movie_stats_url)
        time.sleep(config.s_time_numbers)
        movie_name = self.driver.find_element(
            'xpath',
            config.movie_rank_xml_o + str(rank) + config.movie_rank_xml_c
        ).accessible_name
        print('\n**********', rank, movie_name.upper(), '**********')
        movie_detail_url = \
            self.driver.find_element('xpath', config.movie_detail_xml.replace('*', str(rank))).get_attribute('href')
        movie_countries = list()
        us, us_box_office = self.scrape_us_movie_details(movie_detail_url)
        if us_box_office is None:
            return movie_name, None
        movie_countries.append([us, us_box_office])
        latest_country = us
        for i in range(2, 100):
            country, box_office = self.scrape_global_movie_details(movie_detail_url, i)
            if (country in config.skip_country) or (box_office == 0) \
                    or (movie_countries[-1][0] == country) or (latest_country == country):
                continue
            elif country and box_office:
                latest_country = country
                movie_countries.append([country, box_office])
            else:
                print('WARNING:', str(i - 2), 'countries found and there are no more left')
                break
        return movie_name, movie_countries

    def scrape_us_movie_details(self, movie_detail_url):
        self.driver.get(movie_detail_url)
        time.sleep(config.s_time_numbers)
        country = 'United States'
        box_office = self.driver.find_element('xpath', config.movie_us_xml).text.strip('$').replace(',', '')
        print(country, box_office)
        if box_office == 'n/a':
            return country, None
        return country, int(box_office)

    def scrape_global_movie_details(self, movie_detail_url, i):
        self.driver.get(movie_detail_url)
        time.sleep(config.s_time_numbers)
        self.driver.find_element('xpath', config.intl_menu_btn).click()
        time.sleep(config.s_time_numbers)
        try:
            country = self.driver.find_element(
                'xpath',
                config.movie_intl_xml_o + str(i) + config.movie_intl_xml_c.replace('*', '1') + '/b/a'
            ).text.split('(')[0].strip()
            box_office = self.driver.find_element(
                'xpath',
                config.movie_intl_xml_o + str(i) + config.movie_intl_xml_c.replace('*', '7')
            ).text.strip('$').replace(',', '')
        except selenium.common.exceptions.NoSuchElementException:
            return None, None
        print(country, box_office)
        return country, int(box_office)
