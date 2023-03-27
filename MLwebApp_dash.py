from flask import Flask, render_template,request,session
import numpy as np
from werkzeug.utils import secure_filename
from plotly.subplots import make_subplots
from plotly.graph_objs import *
from dash import Dash, dcc, html, Input, Output,State
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url, load_figure_template
import plotly.express as px
import base64
import io


from dashApp import *


appServer= Flask(__name__)
appServer.config['SECRET_KEY'] = str(int(np.floor(np.random.random() * np.random.random()* 10000)))

app = dash.Dash(name =__name__,server = appServer, url_base_pathname='/dash/')

app.head = [html.Link(rel='stylesheet', href='./dashApp/assets/style2.css')]



app.layout = initializeLayout(appServer)



def getGraph(data, title='Titulo'):
    xName = data.columns[0] ; yName = data.columns[-1]
    # data = data.sort_values(xName)
    fig = px.line(data.sort_values(xName), x=xName , y=yName, title = title)
    layout = Layout(
    paper_bgcolor= 'rgba(0,0,0,0)',
    plot_bgcolor= 'rgba(0,0,0,0)',
    font_color = 'rgba(255,255,255,1)',
    # title_font = 'rgba(255,255,255,1)',
    )
    fig.layout = layout
    return fig


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
        # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
        # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div([

        dcc.Graph(
            figure = getGraph(df)
            ),        
    ])

# @app.callback(
#     Input(component_id = 'upload-table', component_property='value'),
#     Output(component_id = 'Graph-1-out', component_property='figure')
# )   


@app.callback(Output('Graph-1-out', 'children'),
              [Input('upload-table', 'contents')],
              [State('upload-table', 'filename'),
               State('upload-table', 'last_modified')])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@app.callback(Output('Graphs-Tab-Menu','childen'),
              Input('Visualization-Tabs','value'))

def render_Graph(tab):
    if (tab == 'InputData-Graph'):
        pass
    elif( tab == 'ErroEpoch-Graph' ):
        pass
    elif( tab == 'Prediction-Graph'):
        pass