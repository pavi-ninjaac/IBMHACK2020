# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:41:58 2020

@author: ninjaac
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input,Output
import pandas as pd
from tweetwrangling import tweets_analyse


total_confirmed,sorted_confirmed,total_deaths,sorted_deaths,total_recovered,sorted_recovered,total_active,sorted_active=tweets_analyse.get_data()
time_series_df=tweets_analyse.time_series_creation()

colors={
        'background':'black',
        
        }
total=[total_confirmed,total_deaths,total_recovered]
total_name=['    -  Global confirmed','     -   Global Death','     -   Global Recovery']
app=dash.Dash(__name__)

app.layout=html.Div(children=[
                    html.Div(className='header',
                             children=[html.H1('Covid19 Dashboard')],
                             style={'textAlign':'center',} ),
                                      

                    html.Div(className='first_box',
                             style={'width':'17%','display':'inline-block',},
                             children=[html.Ol(id='total_list',children=[html.Li(html.Div(style={'height':'30px'},className='list',children=[html.H2(i),html.H6(j)])) for i,j in zip(total,total_name)])
                                       ]),
                                 
                        
                        
                        
                        ])
 
if __name__=='__main__':
    app.run_server(debug=True)

