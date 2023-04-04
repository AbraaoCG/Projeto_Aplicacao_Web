from flask import Flask, render_template,request,session
import numpy as np
from werkzeug.utils import secure_filename
from plotly.subplots import make_subplots
from plotly.graph_objs import *
from dash import dcc, html
import plotly.express as px
from bs4 import BeautifulSoup
from bs4.element import Tag
from dash.html import Div , Button 

def parse_html(tag):
    if ( not tag.name):
        return html.Div()
    children = []
    tag_name = tag.name.lower()
    tag_class = tag.get('class', [])
    #if (tag_class == 'select_but_upload'): print(tag_class)
    flag = False
    id_value = tag_class[0] if tag_class else None
    class_value = tag_class[0] if tag_class else None

    if(tag.children):
        for child in tag.children:
            
            if ( isinstance(child, str )  and child.strip() != ''):
                children.append(child.strip())
            elif isinstance(child, Tag):
                children.append(parse_html(child))


    if(len(tag_class) > 0):
        if tag_name == 'img':        
            tag_src = tag.get('src', [])
            component =html.Img(className=class_value, src=f'./assets/imgs/{tag_src}')
            return component
        elif 'button_dash' in class_value:
            component = html.Button(className = class_value,id = f'{id_value}_BUTTON', children = children)
            return component
        elif 'tabs_dash' in class_value:
            component = dcc.Tabs(className = class_value ,id = f'{id_value}_TABS' ,value='YOUR_DEFAULT_TAB_VALUE',children = children)
            return component
        elif 'tab_dash' in class_value:
            component = dcc.Tab(className = class_value,label=tag_class[0], value = f'{id_value}_TAB' , children = children)
            return component
        elif 'upload_dash' in class_value:
            component = dcc.Upload(className = class_value, id = f'{id_value}_UPLOAD' ,multiple=True, children = children)
            return component
        elif 'input_dash' in class_value:
            component = dcc.Input(className = class_value, id = f'{id_value}_INPUT' , type = "number", placeholder = "")
            return component
        elif 'dropdown_dash' in class_value:
            component = dcc.Dropdown(options = ["Adicione Opções ao código"],value = "Adicione Opções ao código", className = class_value, id = f'{id_value}_INPUT' )
            return component

    if class_value:
        return html.Div(children=children, id=id_value, className=class_value)
    else:
        return html.Div(children=children)


def parse_html_file(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')  
    initialTag = soup.find('body')
    return parse_html(initialTag)


def writeLayout(InputFilename, OutPutFilename):
    # Ler Arquivo HTML
    with open(InputFilename, "r", encoding='utf-8') as f:
        html_str= f.read()
    
    # Transformar HTML em Dash
    dash_code = parse_html_file(html_str)

    # Preparação para arquivo de saida
    importStr = """from dash.html import Div , Button, Img \nfrom dash.dcc import Tabs,Tab,Input,Upload,Store,Dropdown\n\n"""
    # Escrever python de saída com função para retornar estrutura.
    with open(OutPutFilename, "w", encoding='utf-8') as f:
        f.write(importStr)
        f.write('def getLayoutFormated():\n    return ')
        f.write(str(dash_code))

def getLayoutRaw(InputFilename):
    # Ler Arquivo HTML
    with open(InputFilename, "r", encoding='utf-8') as f:
        html_str= f.read()

    # Retornar código Dash não formatado.
    return parse_html_file(html_str)


# ------------------------------------------------------------------------



# writeLayout(InputFilename = 'index.html', OutPutFilename = 'dashCode.py')

# getLayoutRaw( InputFilename = 'index.html' )

# -------------------------------------------------------------------------
