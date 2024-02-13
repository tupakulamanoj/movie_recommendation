import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import numpy as np
c=CountVectorizer()
warnings.filterwarnings('ignore')
movie_data=pd.read_csv(r"C:\Users\manoj\Desktop\movie_recommendations\datasets\movie_data.csv")
c.fit_transform(movie_data['genres'])
def get_similarties(movie,data=movie_data):
    similarities=[]
    text1=c.transform(data[data['title']==movie]['genres']).toarray()
    num1=data[data['title']==movie].select_dtypes(include=np.number).to_numpy()
    for i,j in data.iterrows():
        name=j['title']
        text=c.transform(data[data['title']==name]['genres']).toarray()
        num=data[data['title']==name].select_dtypes(include=np.number).to_numpy()
        sim=cosine_similarity(text,text1)[0][0]
        sim2=cosine_similarity(num,num1)[0][0]
        similars=(sim+sim2)
        similarities.append(similars)
    return similarities
def recommend_movie(movie_name):
    movie_data['similarity']=get_similarties(movie_name)
    movie_data.sort_values(by='similarity',ascending=False,inplace=True)
    recommendations=movie_data[['title','genres','release_year','crew_director']][2:7]
    return recommendations