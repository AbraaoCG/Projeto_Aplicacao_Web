from flask import Flask, render_template,request, redirect
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)


@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


@app.route('/',methods=["GET", "POST"])

def uploadFiles():
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['file'] # This line uses the same variable and worked fine
            if (uploaded_file.filename != ""):
                file_path = os.path.join(app.instance_path, 'htmlfi', secure_filename(uploaded_file.filename))
                uploaded_file.save(file_path)
            return redirect(('index'))


            
    return render_template('index.html')
