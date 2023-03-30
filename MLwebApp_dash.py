from flask import Flask, render_template,request,session
import numpy as np
from werkzeug.utils import secure_filename
import plotly
from plotly.subplots import make_subplots
from plotly.graph_objs import *
from dash import Dash, dcc, html, dash_table, Input, Output, State
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url, load_figure_template
import plotly.express as px
import base64
import io
import json
import subprocess
import platform
from dashApp import *


appServer= Flask(__name__)
appServer.config['SECRET_KEY'] = str(int(np.floor(np.random.random() * np.random.random()* 10000)))
appServer.config["SESSION_PERMANENT"] = False
appServer.config["SESSION_TYPE"] = "filesystem"


app = dash.Dash(name =__name__,server = appServer, url_base_pathname='/dash/')

app.head = [html.Link(rel='stylesheet', href='./assets/css/style.css'), html.Link(rel='stylesheet', href='./assets/css/style_base.css') ]

#app.head = [html.Link(rel='stylesheet', href='./assets/css/style.css')]

app.layout = init_layout2(appServer)
# app.layout = initializeLayout(appServer)







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
    return df


def getGraph(data, title):
    xName = data.columns[0] ; yName = data.columns[-1]
    # data = data.sort_values(xName)
    fig = px.line(data.sort_values(xName), x=xName , y=yName, title = title)
    layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color = 'rgba(255,255,255,1)',
    # title_font = 'rgba(255,255,255,1)',
    )
    fig.layout = layout
    return fig

def getGraph_Pred(inputData,data1,data2):
    layout = Layout(
    paper_bgcolor= 'rgba(0,0,0,0)',
    plot_bgcolor= 'rgba(0,0,0,0)',
    font_color = 'rgba(255,255,255,1)',
    )

    fig = make_subplots(rows=1,
                    cols=1,
                    subplot_titles=('Predição com modelo de Regressão GD'),
                    ) 
    fig.layout = layout
    xName = data1.columns[0] ; yName = data1.columns[-1] ; data = data1.sort_values(xName)
    # fig = px.line(data1.sort_values(xName), x=xName , y=yName, title = title, color = 'blue',name = 'Predição em treino')
    fig.add_trace( go.Scatter(x=data1[xName], y=data1[yName],
                        mode='lines',
                        name='Predição durante treino'))
    
    xName = data2.columns[0] ; yName = data2.columns[-1] ; data = data2.sort_values(xName)
    # fig.add_scatter(x =data2[xName],y=data2[yName], mode='lines', color = 'red',name = 'Predição após domínio original')
    fig.add_trace( go.Scatter(x=data[xName], y=data[yName],
                        mode='lines',
                        name='Predição Futura'))
    
    xName = inputData.columns[0] ; yName = inputData.columns[-1] ;data = inputData.sort_values(xName)
    # fig.add_scatter(x =inputData[xName],y=inputData[yName], mode='lines', color = 'black', name= 'Dados Importados')
    fig.add_trace( go.Scatter(x=data[xName], y=data[yName],
                        mode='lines',
                        name='Dados importados'))
    
    return fig

def verifyData(inputData):

    flagCleanData = True
    for tag in inputData: # Verifica para cada coluna se o dado contém apenas números.
        if(inputData[tag].dtype == np.float64 or inputData[tag].dtype == np.int64):
            pass
        else:
            flagCleanData = False
    # Se o dado for numérico, atualiza a página com dados importados.
    if(flagCleanData == True):
        return True
    else:
        # Flask('Insira uma tabela apenas com dados números!')
        return html.Div('Sua tabela deve ser númerica')#index()

def runML_andPlot(inputData,file_path):
    # Escrita de dados para Machine Learning em Fotran.
    with open ('FT_NN_data/dataPath_Len.txt', 'w') as text_file: # Export do caminho
        text_file.write(f'{file_path}\n{inputData.shape[0]}\n{inputData.shape[1]}' )
    #Chamada do Fortran
    if ( platform.system() == 'Windows'):
        subprocess.call("./NN_Process.exe")
    else:
        subprocess.call("./fortranML.out")
    # Preparação dos dados para Plots
    erroDF = pd.read_csv('FT_NN_data/output_erro.csv')
    yPredDF1 = pd.read_csv('FT_NN_data/output_Pred1.csv')
    yPredDF2 = pd.read_csv('FT_NN_data/output_Pred2.csv')
    # Geração de Plots e do HTML.
    graphIN = getGraph(inputData, 'Dados Importados')
    graphErro = getGraph(erroDF, 'Erro estimado ao longo das épocas')
    graphPred = getGraph_Pred(inputData,yPredDF1,yPredDF2)

    return graphIN,graphErro,graphPred


# CallBack para receber uploads e prepará-los para ML.
@app.callback(Output('Selected-file-name', 'children'),
              Output('dataML_Results','data'),
              [Input('upload-table', 'contents')],
              [State('upload-table', 'filename'),
               State('upload-table', 'last_modified')])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        dfList = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        
        # Definindo caminho viável para armazenar tabelas.
        user_IP = request.remote_addr.replace('.','_')
        userPath = os.path.join(app.server.instance_path, user_IP)

        # Armazenando tabelas
        df_dict = {}
        for (df,filename) in zip(dfList,list_of_names):
            df_dict[filename] = {}
            if ( verifyData(df) == True ): # Se tabela for estritamente numérica.
                # Escrevo a tabela na pasta do usuário (por IP) para realizar ML com fortran.
                filePath = os.path.join(userPath, filename)
                df.to_csv(filePath, index=False)
                # Realizo o 'ML' com arquivo fortran utilizando função auxiliar.
                graphIN,graphErro,graphPred = runML_andPlot(df,filePath)
                # Armazeno gráficos obtidos em um dicionário duplo para poder utilizá-los na sessão
                df_dict[filename]['dataTable'] = df.to_dict('records')
                df_dict[filename]['dataGraph'] = graphIN
                df_dict[filename]['dataErroGraph'] = graphErro
                df_dict[filename]['dataPredictGraph'] = graphPred
            
        # Gerar lista de Divs com nomes dos arquivos.
        nameDivs = []
        contTables = 0
        for name in list_of_names:
            contTables += 1
            nameDivs.append(html.Div(f'Tabela {contTables}: '+ name ,className='my-dashboard3'))  
        print('BBBBBBBBBBBBBBBB')
        return nameDivs,df_dict
    else:
        return html.Div('Nenhum arquivo selecionado', className= 'my-dashboard3'),{}


# CallBack para Realizar o ML e retornar gráficos em função da Tab.
@app.callback(Output(component_id= 'Tabs-Output1',component_property='children'),
              Input(component_id= 'Visualization-Tabs',component_property='value'),
              Input('dataML_Results', 'data'),
              State('upload-table', 'filename')
              )

def render_Graph(tab,df_dict,filenames):
    if(filenames) is not None:
        filename1 = filenames[0]
        #print(df_dict[filename1]['dataTable'])
        #divChildren = []
        if  ( tab == 'InputData-Table'):
            dataDF = pd.DataFrame.from_dict(df_dict[filename1]['dataTable'])
            return dash_table.DataTable(
                data = df_dict[filename1]['dataTable'] , 
                columns = [ {"name": i,"id": i} for i in dataDF.columns ],
                page_size=10,
                style_data={
                    'backgroundColor': 'rgba(0, 0, 0, 0.3)',
                    'color': 'white',
                    'fontSize': 16
                }
                )
            
        elif( tab == 'InputData-Graph'):
            return dcc.Graph(figure=df_dict[filename1]['dataGraph'])
        elif( tab == 'ErroEpoch-Graph'):
            return dcc.Graph(figure=df_dict[filename1]['dataErroGraph'])
        elif( tab == 'Prediction-Graph'):
            return dcc.Graph(figure=df_dict[filename1]['dataPredictGraph'])
        #print(divChildren)
        #return html.Div(children=divChildren)

# @app.callback(Input('initialize-session'))

# def initializeSessionPath():

# @app.server.route('/dash/',methods=["GET", "POST"])
