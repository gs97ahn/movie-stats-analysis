from config.config import Config
from utils.data_formatter import DataFormatter
from tqdm import tqdm
from konlpy.tag import Okt
from model.naive_bayes_classifier import NaiveBayesClassifier

import os
import pandas as pd
import pickle
import random

data_formatter = DataFormatter()
config = Config()
okt = Okt()
naive_bayes_classifier = NaiveBayesClassifier()

def split_pos_neg_files():
    print('\n\n**********', 'Splitting POS and NEG files', '**********')
    files = os.listdir(config.c_movie_comments_folder_path)
    pos, neg = list(), list()
    for f in files:
        if f.split('_')[1].split('.')[0] == 'pos':
            pos.append(f)
        else:
            neg.append(f)
    print('Number of positive movies (meaning more profit made in South Korea): ', len(pos))
    print('Number of negative movies (meaning less profit made in South Korea):', len(neg))
    return pos, neg


def split_train_test(positive, negative):
    print('\n\n**********', 'Splitting TRAIN and TEST data', '**********')
    positive_list, negative_list = list(), list()
    data = [positive, negative]
    for i in range(2):
        for f in data[i]:
            df = data_formatter.csv_reader(config.c_movie_comments_folder_path + f)
            for s in df.values:
                if pd.isnull(s):
                    continue
                elif i == 0:
                    positive_list.append((s[0], 'pos'))
                elif i == 1:
                    negative_list.append((s[0], 'neg'))
                else:
                    print('ERROR: Occurred during split_train_test')
                    quit(1)
    print('Number of positive comments:', len(positive_list))
    print('Number of negative comments:', len(negative_list))
    print()
    print('Train positives:', len(positive_list) // 2, 'Train negative:', len(negative_list) // 2)
    print('Test positives:', len(positive_list) - len(positive_list) // 2,
          'Test negatives:', len(negative_list) - len(negative_list) // 2)
    return positive_list[:len(positive_list) // 2] + negative_list[:len(negative_list) // 2], \
           positive_list[len(positive_list) // 2:] + negative_list[len(negative_list) // 2:]


def get_all_words(all_data):
    print('\n\n********** Getting all words **********')
    return naive_bayes_classifier.create_all_words(all_data)


def train_model(train_data, all_words):
    print('\n\n********** Training Model **********')
    train_features = naive_bayes_classifier.extract_features(train_data, all_words)
    model = naive_bayes_classifier.train(train_features)
    if not os.path.isdir(config.model_folder_path):
        os.makedirs(config.model_folder_path)
    f = open(config.model_folder_path + config.model_filename, 'wb')
    pickle.dump(model, f)
    f.close()
    print(model.show_most_informative_features())


def test_model(test_data, all_words):
    print('\n\n********** Testing Model **********')
    f = open(config.model_folder_path + config.model_filename, 'rb')
    model = pickle.load(f)
    f.close()
    correct_cnt = 0
    for d in tqdm(test_data):
        result = naive_bayes_classifier.test(model, d[0], all_words)
        if result == d[1]:
            correct_cnt += 1
    print('Model accuracy:', (correct_cnt / len(test_data)) * 100, '%')


if __name__ == '__main__':
    p, n = split_pos_neg_files()
    train_d, test_d = split_train_test(p, n)
    random.shuffle(train_d)
    random.shuffle(test_d)
    all_w = get_all_words(train_d + test_d)
    train_model(train_d, all_w)
    test_model(test_d, all_w)


