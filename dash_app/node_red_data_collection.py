# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:41:47 2020

@author: ninjaac
"""
class sentiment_data():
    
    def get_sentiment_data():
        import pandas as pd
        import numpy as np
        #read the files
        tweet=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\tweet.txt',sep='\n')
        tweet.columns=['tweets']
        sentiment=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\sentiment.csv')
        sentiment.columns=['sentiment']
        emotion=pd.read_csv(r'F:\dash_app\dash_ibm_app\dataset\emotion.csv')
        emotion.columns=['emotion']
        
        #prepare the dataframe stuiable for pie chart
        sentiment_values=list(sentiment['sentiment'].value_counts())
        sentimet_names=['positive','negative','neutral']
        
        emotion_value=emotion['emotion'].value_counts()
        print(emotion_value)
        emotion_name=['fear','angery','joy','disgust','sadness']
        return sentiment_values,sentimet_names,emotion_value,emotion_name

        

