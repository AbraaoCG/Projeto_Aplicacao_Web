from flask import Flask, render_template,request, redirect
import os
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])

def hello():
    data = []
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            return redirect(request.url)
    return render_template('index.html', data=data)

app.config['FILE_UPLOADS'] = "/home/abraaonote/Documentos/projetos/flaskApp/Ups"
