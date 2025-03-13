#!/usr/bin/env python
# coding: utf-8
#Movie Recommendation
import numpy as np
import pandas as pd
import sklearn

import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
# Convert text to numerical values
from sklearn.metrics.pairwise import cosine_similarity

movies_data =pd.read_csv(r"C:\Users\ComputerCenter3\Desktop\Movie Recommendation\movies.csv")
movies_data.head()

#Data Exploration

movies_data.shape

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

movies_data.info()

movies_data.isna().sum()

movies_data[selected_features].head()

movies_data[selected_features].isna().sum()

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
print(movies_data.head())

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_features)

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors.shape)
print (feature_vectors)

similarity = cosine_similarity(feature_vectors)
print  (similarity )

similarity.shape

movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)
print(len(list_of_all_titles))

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

print(len(similarity_score))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print(sorted_similar_movies)

#Data Presentation
print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1
movie_name = input(' Enter your favourite movie name : ')
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1
