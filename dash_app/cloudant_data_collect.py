# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:20:24 2020

@author: ninjaac
"""
def get_datas():
    from cloudant import cloudant
    from cloudant.client import Cloudant
    
    Url='https://995d72fd-116c-482b-9b38-8d60481f9a86-bluemix:2a7c7a6833e3aaa17ee8644a1bfbec515a4403de17136678610e08045e5bc27f@995d72fd-116c-482b-9b38-8d60481f9a86-bluemix.cloudantnosqldb.appdomain.cloud'
    """
    client = Cloudant(USERNAME, PASSWORD, url=your url)
        
    client = Cloudant('995d72fd-116c-482b-9b38-8d60481f9a86-bluemix', 
                      '2a7c7a6833e3aaa17ee8644a1bfbec515a4403de17136678610e08045e5bc27f',
              url=Url
             )
 

    """
    with cloudant('995d72fd-116c-482b-9b38-8d60481f9a86-bluemix', 
                  '2a7c7a6833e3aaa17ee8644a1bfbec515a4403de17136678610e08045e5bc27f',
                  url=Url,
                  auto_renew=True) as client:
   
        session = client.session()
        print('Username: {0}'.format(session['userCtx']['name']))
        print('Databases: {0}'.format(client.all_dbs()))
        
        #open the database
        sentiment_db = client['sentiment']
        emosion_db=client['emotion']
        tweet_db=client['tweets']
    
        #retrive all the documents
        sentiment=[]
        for data in sentiment_db:
            sentiment.append(data['SENTIMENT'])
            #retrive all emosion datas
        emosion=[]
        for emo in emosion_db:
                emosion.append(emo['emotion'])
                #retrive tweets
        tweets=[]
        for te in tweet_db:
                    tweets.append(te['tweets'])
        return sentiment,emosion,tweets
        