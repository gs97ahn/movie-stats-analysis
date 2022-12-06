class Config:
    def __init__(self):
        # The numbers - Website provides movie statistics
        self.the_numbers_url = 'https://www.the-numbers.com'
        self.movie_stats_url = self.the_numbers_url + '/box-office-records/worldwide/all-movies/cumulative' \
                                                      '/released-in-2022'

        self.movie_detail_xml = '/html/body/div/div[3]/div[3]/center/table/tbody/tr[*]/td[2]/b/a'
        self.movie_rank_xml_o = '//*[@id="page_filling_chart"]/center/table/tbody/tr['
        self.movie_rank_xml_c = ']/td[2]/b/a'
        self.movie_us_xml = '/html/body/div/div[3]/table/tbody/tr[2]/td[2]'
        self.intl_menu_btn = '//*[@id="a_international"]'
        self.movie_intl_xml_o = '/html/body/div/div[3]/div[3]/div[5]/div[1]/center/table/tbody/tr['
        self.movie_intl_xml_c = ']/td[*]'

        self.skip_country = ('Central America', 'Middle East Region', 'Others Middle East', 'Serbia / Others Balkans',
                             'Serbia and Montenegro', 'Trinidad', 'South Africa / Others Africa',
                             'Trinidad / Others Caribbean')

        self.s_time_numbers = 5

        # Naver - Website provides South Korean movie comments
        self.naver_url = 'https://movie.naver.com'
        self.movie_comments_url = self.naver_url + '/movie/bi/mi/pointWriteFormList.naver?code=*&type=after' \
                                                   '&isActualPointWriteExecute=false' \
                                                   '&isMileageSubscriptionAlready=false' \
                                                   '&isMileageSubscriptionReject=false&page='

        self.search_ipt = '/html/body/div/div[2]/div/div/fieldset/div/span/input'
        self.search_btn = '/html/body/div/div[2]/div/div/fieldset/div/button'
        self.movie_rating_xml = '/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[*]/dl/dd[1]/em[1]'
        self.movie_search_result_xml = '/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[*]/dl/dt/a'
        self.movie_comment_id = '_filtered_ment_'

        self.s_time_naver = 5

        # Data folder path
        self.parent_data_folder_path = './data/'

        # Collected data folder path
        self.collected_data_folder_path = self.parent_data_folder_path + 'collected/'
        self.c_movie_statistics_folder_path = self.collected_data_folder_path + 'movie_statistics/'
        self.c_world_population_file_path = \
            self.collected_data_folder_path + 'population/world_population_by_country.csv'
        self.c_movie_comments_folder_path = self.collected_data_folder_path + 'movie_comments/'

        # Preprocessed data folder path
        self.preprocessed_data_folder_path = self.parent_data_folder_path + 'preprocessed/'
        self.p_movie_statistics_folder_path = self.preprocessed_data_folder_path + 'movie_ratio/'

        # CSV filename
        self.csv_filename = '*.csv'

        # Countries by group
        self.g20 = ('Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia',
                    'Italy', 'Japan', ' South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa', 'Turkey',
                    'United Kingdom', 'United States')
        self.oecd_countries = ('Iceland', 'United States', 'Georgia', 'New Zealand', 'Singapore', 'Australia', 'Canada',
                               'Spain', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland',
                               'Ireland', 'Israel', 'Italy', 'Japan', 'South Korea', 'Latvia', 'Lithuania',
                               'Luxembourg', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal',
                               'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'United Kingdom',
                               'United States')

        # Model folder path
        self.model_folder_path = self.parent_data_folder_path + 'model/'

        # Model filename
        self.model_filename = 'model.pickle'
