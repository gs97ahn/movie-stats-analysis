from config.config import Config
from selenium import webdriver
from utils.web_requester import WebRequester
from bs4 import BeautifulSoup

import os
import time

config = Config()
web_requester = WebRequester()


class MovieCommentsScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(os.environ['WEB_DRIVER_PATH'])

    def search_by_title(self, title):
        self.driver.get(config.naver_url)
        time.sleep(config.s_time_naver)
        search_input = self.driver.find_element('xpath', config.search_ipt)
        search_input.clear()
        if title.__contains__('('):
            search_input.send_keys(title.split('(')[1].split(')')[0].strip())
        else:
            search_input.send_keys(title)
        time.sleep(config.s_time_naver)
        self.driver.find_element('xpath', config.search_btn).click()
        time.sleep(config.s_time_naver)
        index = 1
        for i in range(1, 6):
            try:
                float(self.driver.find_element('xpath', config.movie_rating_xml.replace('*', str(i))).text)
            except ValueError:
                continue
            index = i
            break
        movie_id = self.driver.find_element('xpath',
                                            config.movie_search_result_xml.replace('*', str(index))) \
            .get_attribute('href').split('code=')[1]
        return movie_id

    def scrape_comments(self, movie_id):
        comments = list()
        latest_page_comment = str()
        is_done = False
        for i in range(1, 10000):
            response = web_requester.requester(config.movie_comments_url.replace('*', movie_id) + str(i))
            time.sleep(config.s_time_naver)
            document = BeautifulSoup(response.text, 'html.parser')
            print('********** page', i, '**********')
            for c in range(10):
                try:
                    comment = document.find('span', {'id': config.movie_comment_id + str(c)}).string.strip()
                except AttributeError:
                    break
                if c == 0 and latest_page_comment == comment:
                    is_done = True
                    break
                elif c == 0:
                    latest_page_comment = comment
                comments.append(comment)
                print(str(c) + ':', comment)
            if is_done:
                print('END OF COMMENT\n')
                break
        return comments
