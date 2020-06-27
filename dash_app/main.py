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
#total count of deatha and confirmed cases
total=[total_confirmed,total_deaths,total_recovered]
total_name=['    -  Global confirmed','     -   Global Death','     -   Global Recovery']

#sorted cases among the country


def generate_tabel(df,title):
    return html.Table([

        html.Caption(title),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(len(df))
            ])
        ])

app=dash.Dash(__name__)

app.layout=html.Div(children=[
                    html.Div(className='header',
                             children=[html.H1('Covid19 Dashboard')],
                             style={'textAlign':'center',} ),
                                      

                    html.Div(className='first_box',
                             style={'width':'17%','display':'inline-block','float':'left'},
                             children=[html.Ol(id='total_list',children=[html.Li(html.Div(style={'height':'30px'},className='list',children=[html.H2(i),html.H6(j)])) for i,j in zip(total,total_name)])
                                       ]),
                    
                    html.Div(className='confirm_countrywise',
                             style={'width':'17%','display':'inline-block,','float':'right'},
                             children=[generate_tabel(sorted_confirmed,"Total Confirmed cases"),
                                       
                                       ]),

                    html.Div(className='sentiment_emotion_graph',
                             style={'width':'64%','display':'inline-block','float':'right',},
                             children=[html.Div('ssdfghb')]),

                    html.Div(className='death_countrywise',
                             style={'width':'17%',},
                             children=[generate_tabel(sorted_deaths,'Total Death In Counties'),
                                      ]
                             ) ,
                    html.Div(className='death_countywise_name',
                             style={"width":"17%",},
                             children=[html.Div('Death Basedon Country')]),
                                       
                    html.Div('esrxdcfghbjnbhvgcfvhbvcfgv')
                        
                        ])
  
if __name__=='__main__':
    app.run_server(debug=True)

