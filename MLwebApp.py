from flask import Flask, render_template,request
from flask_session import Session
import os
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly
import pandas as pd
import json
import subprocess


app = Flask(__name__)

# enable debugging mode
# app.config["DEBUG"] = True
# # app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "redis"
# Session(app)

os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)


@app.route('/')
def index(file_path = 'exampleData/exampleData2.csv'):
    inputData = pd.read_csv(file_path)
    graphIN = getGraph(inputData)
    return render_template('index.html', graphIN=graphIN)

@app.route('/',methods=["GET", "POST"])

def uploadFiles():
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['file'] # This line uses the same variable and worked fine
            if (uploaded_file.filename != ""):     
                file_path = os.path.join(app.instance_path, 'htmlfi', secure_filename(uploaded_file.filename))
                uploaded_file.save(file_path) 
                return verifyData(file_path)
    return index()

def getGraph(data, title):
    xName = data.columns[0] ; yName = data.columns[-1]
    # data = data.sort_values(xName)
    fig = px.line(data.sort_values(xName), x=xName , y=yName, title = title)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def getGraph_Pred(inputData,data1,data2):
    fig = make_subplots(rows=1,
                    cols=1,
                    subplot_titles=('Predição com modelo de Regressão GD')) 


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
    
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



def verifyData(file_path):
    #print("KRL")
    inputData = pd.read_csv(file_path)
    flagCleanData = True
    for tag in inputData: # Verifica para cada coluna se o dado contém apenas números.
        if(inputData[tag].dtype == np.float64 or inputData[tag].dtype == np.int64):
            pass
        else:
            flagCleanData = False
    # Se o dado for numérico, atualiza a página com dados importados.
    if(flagCleanData == True):
        return runML_andPlot(inputData,file_path)
    else:
        # Flask('Insira uma tabela apenas com dados números!')
        return index()

def runML_andPlot(inputData,file_path):
    # Escrita de dados para Machine Learning em Fotran.
    with open ('FT_NN_data/dataPath_Len.txt', 'w') as text_file: # Export do caminho
        text_file.write(f'{file_path}\n{inputData.shape[0]}\n{inputData.shape[1]}' )
    #Chamada do Fortran
    subprocess.call("./fortranML.out")
    # Preparação dos dados para Plots
    erroDF = pd.read_csv('FT_NN_data/output_erro.csv')
    yPredDF1 = pd.read_csv('FT_NN_data/output_Pred1.csv')
    yPredDF2 = pd.read_csv('FT_NN_data/output_Pred2.csv')
    # Geração de Plots e do HTML.
    graphIN = getGraph(inputData, 'Dados Importados')
    graphErro = getGraph(erroDF, 'Erro estimado ao longo das épocas')
    graphPred = getGraph_Pred(inputData,yPredDF1,yPredDF2)
    return render_template('index.html', graphIN=graphIN, graphPred = graphPred, graphErro = graphErro)




def MachineLearningEngine(inputDF):
    xData = inputDF.drop([inputDF.columns[-1]], axis = 1)
    yData =inputDF[inputDF.columns[-1]]
    # x_train, x_test, y_train, y_test = train_test_split(xData, yData, test_size = 0.01, random_state = 42)
    # Possivel continuação de uma Rede Neural aqui.

if __name__ == '__main__':
    app.run(debug=True)