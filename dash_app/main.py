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

import json
import plotly.express as px
import plotly.graph_objects as go

total_confirmed,sorted_confirmed,total_deaths,sorted_deaths,total_recovered,sorted_recovered,total_active,sorted_active=tweets_analyse.get_data()
time_series_df=tweets_analyse.time_series_creation()

colors={
        'background':'black',
        
        }
#total count of deatha and confirmed cases
total=[total_confirmed,total_deaths,total_recovered]
total_name=['    -  Global confirmed','     -   Global Death','     -   Global Recovery']

#sorted cases among the country

#generate scrolabel data for death and confirm cases
def generate_tabel(df,title):
    return html.Table([

        html.Caption(title),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(len(df))
            ])
        ])


#map creation
    
#access token from mapbox https://account.mapbox.com/
token='pk.eyJ1IjoibmluamFhYyIsImEiOiJja2J5bjB4YmQwaXg2MzBuNHNzaTA0bXk2In0.BVaAwyDqBSPCCYqRFQBdcA'   

fig = px.scatter_mapbox(time_series_df, 
                        lat="Lat", lon="Long", 
                        hover_name="Country/Region", 
                        hover_data=['Country/Region'],
                        zoom=1,
                        color_discrete_sequence=["fuchsia"],
                        height=500)

fig.update_layout(mapbox_style="dark",mapbox_accesstoken=token)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#time series map ceration based on the map cover data
colors={
    'backgroud':"black",
    'text':'gray',
}
def create_time_series(df,country_name,col_name,title):
    fig=dict(
        data=[
            {'x':list(df['date']), 'y':list(df[col_name]),
             'type' : 'bar' ,
             'name' : 'Date',
             
                 },
            ],
        layout={'title' : country_name +'\t' + title,
                
                'plot_bgcolor':colors['backgroud'],
                'paper_bgcolor':colors['backgroud'],
                'font' :{
                    'color':colors['text']  
                    }
                },
        )
    return fig


app=dash.Dash(__name__)


app.layout=html.Div(children=[
                    html.Div(className='header',
                             children=[html.H1('Covid19 Dashboard')],
                             style={'textAlign':'center',} ),
                                      

                    html.Div(className='first_box',
                             style={'width':'17%',
                                    'display':'inline-block',
                                    'float':'left'},
                             children=[html.Ol(id='total_list',children=[html.Li(html.Div(style={'height':'30px'},className='list',children=[html.H2(i),html.H6(j)])) for i,j in zip(total,total_name)])
                                       ]),
                    
                    html.Div(className='confirm_countrywise',
                             style={'width':'17%',
                                    'display':'inline-block,',
                                    'float':'right'},
                             children=[generate_tabel(sorted_confirmed,"Total Confirmed cases"),
                                       
                                       ]),

                    html.Div(className='sentiment_emotion_graph',
                             style={'width':'64%',
                                    'display':'inline-block',
                                    'float':'right',},
                             children=[html.Div('ssdfghb')]),

                    html.Div(className='death_countrywise',
                             style={'width':'17%',},
                             children=[generate_tabel(sorted_deaths,'Total Death In Counties'),
                                      ]
                             ) ,
                    html.Div(className='death_countywise_name',
                             style={"width":"17%",},
                             children=[html.Div('Death Basedon Country')]),
                                       
                    html.Div(className='map',
                             style={'width':'60%',
                                    'display':'inline-block',
                                    'height':'5%',
                                    'float':'left'},
                             children=[
                                
                                     dcc.Graph(
                                             id='scatter_world_map',
                                             hoverData={'points':[{'customdata':['India']}]},
                                             figure=fig,
            )
                                 ]),
                    html.Div(className='time_series_map',
                             style={'dispaly':'inline-block',
                                    'width':'38%',
                                    "float":'right'},
                             children=[
                                 dcc.Graph(
                                     id='death_time_series_map',
                                     ),
                                 dcc.Graph(
                                     id='conifrm_time_series_map',
                                     )
                                 ]),
                   
                        
                        ])

"""
@app.callback(Output(component_id='check', component_property='children'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

"""
@app.callback(Output(component_id='death_time_series_map', component_property='figure'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def ubdate_death_time_series(hoverData):
    #full=full_table_f[full_table_f['Country/Region'] == 'Afghanistan']
    country_name = hoverData['points'][0]['customdata'][0]
    time_df=time_series_df[time_series_df['Country/Region'] == country_name]
    time_df_death=time_df[['Death','date']]
    col_name='Death'
    title='Death rate Date wise'
    return create_time_series(time_df_death,country_name,col_name,title)
    

@app.callback(Output(component_id='conifrm_time_series_map', component_property='figure'),
              [Input(component_id='scatter_world_map',component_property='hoverData')])
def ubdate_confirm_time_series(hoverData):
    #full=full_table_f[full_table_f['Country/Region'] == 'Afghanistan']
    country_name = hoverData['points'][0]['customdata'][0]
    time_df=time_series_df[time_series_df['Country/Region'] == country_name]
    time_df_death=time_df[['Confirmed','date']]
    col_name='Confirmed'
    title='Confirm cases Date wise'
    return create_time_series(time_df_death,country_name,col_name,title)
   

  
if __name__=='__main__':
    app.run_server(debug=True)

