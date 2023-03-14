from flask import Flask, render_template,request, redirect
import os
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
import plotly.express as px
import plotly
import pandas as pd
import json

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)


@app.route('/')
def index(file_path = 'exampleData/exampleData2.csv'):
    graphIN = getGraph(file_path)
    print(file_path)
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

def getGraph(file_path):
    data = pd.read_csv(file_path)
    xName = data.columns[0] ; yName = data.columns[-1]
    data = data.sort_values(xName)
    fig = px.line(data, x=xName , y=yName, title = 'Dados Importados')
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def verifyData(file_path):
    inputData = pd.read_csv(file_path)
    flagCleanData = True
    for tag in inputData: # Verifica para cada coluna se o dado contém apenas números.
        if(inputData[tag].dtype == np.float64 or inputData[tag].dtype == np.int64):
            pass
        else:
            flagCleanData = False
    # Se o dado for numérico, atualiza a página com dados importados.
    if(flagCleanData == True):
        graphIN = getGraph(file_path)
        
        return render_template('index.html', graphIN=graphIN)
    else:
        # Flask('Insira uma tabela apenas com dados números!')
        return index()
    
def MachineLearningEngine(inputDF):
    xData = inputDF.drop([inputDF.columns[-1]], axis = 1)
    yData =inputDF[inputDF.columns[-1]]
    # x_train, x_test, y_train, y_test = train_test_split(xData, yData, test_size = 0.01, random_state = 42)


if __name__ == '__main__':
    app.run(debug=True)