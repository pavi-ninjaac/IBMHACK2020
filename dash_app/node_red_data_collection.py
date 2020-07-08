# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:41:47 2020

@author: ninjaac

"""
import pandas as pd
import numpy as np

  
class sentiment_data():

    def get_sentiment_data():

        #read the files

        sentiment=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\sentiment.csv')
        sentiment.columns=['sentiment']
        emotion=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\emotion.csv')
        emotion.columns=['emotion']
        
        #future emotions and sentiment of people
        future_sentiment=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\sentiment_future.csv')
        future_sentiment.columns=['sentiment']
        
        #prepare the dataframe stuiable for pie chart
        sentiment_values=list(sentiment['sentiment'].value_counts())
        sentimet_names=['positive','negative','neutral']
        
        emotion_value=emotion['emotion'].value_counts()
        emotion_name=['fear','angery','joy','disgust','sadness']
        
        future_sentiment_value=list(future_sentiment['sentiment'].value_counts())
        future_sentimet_names=['positive','negative','neutral']
        
        #total values 
        sentiment_total=sentiment.shape[0]
        emotion_total=emotion.shape[0]
        future_sentiment_total=future_sentiment.shape[0]
        
        total=[sentiment_total,emotion_total,future_sentiment_total]
        
        return sentiment_values,sentimet_names,emotion_value,emotion_name,future_sentiment_value,future_sentimet_names,total

    def get_frequent_word():
        tweet=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\tweet.txt',sep='\n')
        tweet.columns=['tweets']
        
        count=tweet.tweets.str.split(expand=True).stack().value_counts()
        count=[word for word in count]
        word=tweet.tweets.str.split(expand=True).stack().value_counts().index.tolist()
        df=pd.DataFrame({'word':word,'count':count})
        
        
