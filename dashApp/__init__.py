from flask import Flask, render_template, request, session
import os
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objs import *

import dash
from dash import dcc, html, dash_table

from bs4 import BeautifulSoup
from bs4.element import Tag
from dash.html import Div, Button, Img
from dash_core_components import Upload,Tab,Tabs

from assets.dashCode import getLayoutFormated
from assets.convertDash import writeLayout,getLayoutRaw


df2 = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv('./exampleData/exampleData.csv')

tabs_styles = {
    'height': '100%',
    'borderTop': "3px solid rgba(255,255,255,0.5)",
    'borderLeft': "3px solid rgba(255,255,255,0.5)",
    'borderRight': "3px solid rgba(255,255,255,0.5)",
    'border-radius': '30px 30px 30px 30px',

}
tab_style = {
    'border-radius': '30px 30px 30px 30px',
    'borderTop': '2px solid #828282',
    'borderBottom': '0px solid #828282',
    'borderLeft': '0px solid #828282',
    'borderRight': '0px solid #828282',
    'fontWeight': 'bold',
    "background": "rgba(255,255,255,0.05)",
    'text-align': 'center',
    'font': " 400 16px 'Roboto', sans-serif",
    'color': 'white',
}

tab_selected_style = {
    'fontWeight': 'bold',
    'border-radius': '30px 30px 30px 30px',
    'borderTop': '2px solid #828282',
    'borderBottom': '0px solid #828282',
    'borderLeft': '0px solid #828282',
    'borderRight': '0px solid #828282',
    "background": "rgba(255,255,255,0.1)",
    'text-align': 'center',
    'font': " 400 16px 'Roboto', sans-serif",
    'color': 'white',

}


def initializeLayout(app):

    layout = html.Div(
        id='initialize-session',
        className="free_dashboard",
        children=[
            html.Div(
                className="left-menu",
                children=[html.Div(
                    className="website-title",
                    children=[
                        html.Div(
                            className="acg",
                            children=['ACG']
                        )
                    ]
                )]
            ),
            html.Div(
                className="frame-12",
                children=[
                    html.Div(
                        className="center-top",
                        children=[
                            html.Div(
                                className='topleft',
                                children=[
                                    html.Div(
                                        className="my-dashboard",
                                        children=[
                                            'Enviar Dados',
                                        ]
                                    ),
                                    html.Div(
                                        # className="my-dashboard3",
                                        id='Selected-file-name'
                                    ),
                                    html.Button(
                                        className='selectbutton',
                                        children=[
                                            dcc.Upload(
                                                id='upload-table',
                                                children=[html.Div(
                                                    className='my-dashboard2',
                                                    children=[
                                                        'Selecionar Arquivo']
                                                )],
                                                multiple=True
                                            ),
                                            dcc.Store(id='dataML_Results')
                                        ]
                                    ),
                                ]
                            )

                        ]
                    ),
                    html.Div(
                        className="center-bottom",
                        children=[
                            html.Div(
                                className='my-dashboard',
                                children=['Visualização']
                            ),
                            dcc.Tabs(
                                id='Visualization-Tabs',
                                value='InputData-Graph',
                                children=[
                                    dcc.Tab(label='Dados de Entrada', value='InputData-Table',
                                            style=tab_style, selected_style=tab_selected_style),
                                    dcc.Tab(label='Dados de Entrada', value='InputData-Graph',
                                            style=tab_style, selected_style=tab_selected_style),
                                    dcc.Tab(label='Evolução do Erro', value='ErroEpoch-Graph',
                                            style=tab_style, selected_style=tab_selected_style),
                                    dcc.Tab(label='Predição', value='Prediction-Graph',
                                            style=tab_style, selected_style=tab_selected_style),
                                ],
                                style=tabs_styles
                            ),
                            html.Div(id='Tabs-Output1', className='frame-1'),
                            # html.Div(id='Graph-1-out')
                            # dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
                        ]
                    )

                ]
            ),
        ],
    )

    return layout

# 
# writeLayout(InputFilename = './assets/index.html', OutPutFilename = './assets/dashCode.py')
def init_layout2(app):
    # return getLayoutRaw(InputFilename= './assets/index.html')
    return getLayoutFormated()