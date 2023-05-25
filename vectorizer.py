#https://github.com/stopwords-iso/stopwords-ru/blob/master/stopwords-ru.txt

import pandas as pd
import nltk#
nltk.download('punkt')
from nltk import sent_tokenize, word_tokenize, regexp_tokenize
import pymorphy2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

text = pd.read_csv('C:\\Users\\oigla\\#Algoritmika\\Algoritmika_19-1\\df1000.csv')
#stopwords_ru = pd.read_fwf('C:\\Users\\вяаы\\Downloads\\Хакатон_Лидеры_19\\stop_words_russian.txt').split()
with open('C:\\Users\\oigla\\#Algoritmika\\Algoritmika_19-1\\stopwords-ru.txt', 'r', encoding='utf8') as file:
    stopwords_ru = [line.strip() for line in file.readlines()]
print(stopwords_ru)

text['type3'] = text['type3'].fillna('')


def normalize_tokens(tokens):
    morph = pymorphy2.MorphAnalyzer()
    return [morph.parse(tok)[0].normal_form for tok in tokens]


def remove_stopwords(tokens, stopwords=None, min_length=4):
    if not stopwords:
        return tokens
    stopwords = set(stopwords)
    tokens = [tok
              for tok in tokens
              if tok not in stopwords and len(tok) >= min_length]
    return tokens

def tokenize_n_lemmatize(
    text, stopwords=None, normalize=True,
    regexp=r'(?u)\b\w{4,}\b'):
    words = [w for sent in sent_tokenize(str(text))
             for w in regexp_tokenize(sent, regexp)]
    if normalize:
        words = normalize_tokens(words)
    if stopwords:
        words = remove_stopwords(words, stopwords)
    return words
# в этой строке ошибка, просит строку

words = tokenize_n_lemmatize(text, stopwords=stopwords_ru)

tfidf = TfidfVectorizer()
overview_matrix = tfidf.fit_transform(text['type3'])
similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
mapping = pd.Series(text.index, index=text['type1'])
print(mapping)

# print(f"vectorization done in {time() - t0:.3f} s")
# print(f"n_samples: {X_tfidf.shape[0]}, n_features: {X_tfidf.shape

# def recommend_dolgoletie(content_input):
#     content_index = mapping[content_input]
#     similarity_score = list(enumerate(similarity_matrix[content_index]))
#     similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
#     similarity_score = similarity_score[1:10]
#     content_indices = [i[0] for i in similarity_score]
#     return (text['type1'].iloc[content_indices])
