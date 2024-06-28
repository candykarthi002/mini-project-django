from django.shortcuts import render, redirect
from . import table, chain, plotter
import pandas as pd
import json
from .models import Chat, Graph
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import matplotlib
matplotlib.use('agg')

CHART_TYPES = ['bar', 'pie', 'doughnut']

PROMPT_FOR_SENTENCE = 'and answer in a complete sentence.'
# PROMPT_CHART = "Pay attention to use only the column names you can see in the tables below.use and don't try to show the figure and don't return imgur link as output instead return in the format as JSON: chart type, data with only numerical value, label regarding the data and title?"
PROMPT_CHART = '''
You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
You should interpret the columns of the dataframe as follows:

1) Only answer questions related to the dataframe. For anything else, say you do not know.
2) Pay attention to use only the column names you can see in the tables below.
3) don't return imgur link as output instead return in the format as JSON(use double quotes for property names): chart type, data with only numerical value, label regarding the data, blueish purple gradient colors for each datapoint and title.
4) Only use the available matplotlib module for plotting.
5) don't try to create a GUI window to show the figure.
6) convert the datatype of the date related column to datetime.

For creating a gradient color palette that transitions smoothly between the colors, use the following colors and don't use repetitive colors:

Starting Color: #FF5733 (a vibrant orange-red)
Midpoint Color: #FFD700 (a bright yellow)
Ending Color: #1E90FF (a vivid blue)

Question: '''

@login_required
def index(request):
    json_records = table.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    columns = list(data[0].keys())[1:]
    chat = Chat.objects.filter(author=request.user)
    graph = Graph.objects.filter(author=request.user)
    context = {'user':request.user, 'table': data, 'columns': columns, 'chat': chat, 'chart': graph, 'chartTypes': CHART_TYPES} 
    return render(request, 'index.html', context)

@login_required
def ask(request):
    if request.method == "POST":
        query = request.POST.get("query")
        result = chain(f"{query} {PROMPT_FOR_SENTENCE}")
        if result:
            generated_code = result.get("intermediate_steps")[1]
            answer = result["result"]
            # answer = result.get("intermediate_steps")[3]
            chat = Chat(author=request.user, question=query, query_text=generated_code, answer=answer)
            chat.save()
        return render(request, 'result.html', {'chat': chat})
    return redirect(index)

@login_required
def plot(request):
    if request.method == "POST":
        chart_type = request.POST.get("chart-type")
        column_name = request.POST.get("column-name")
        query = f"Plot a {chart_type} chart on {column_name} column?"
        result = plotter(f"{PROMPT_CHART} {query} use values_count instead unique and use functions like count, mean, median, etc.")
        print(result)
        if result["output"]:
            result["output"] = result["output"].replace("\'", "\"")
            result["output"] = json.loads(result["output"])
            graph = Graph(author=request.user, question=query, chart_data=result["output"])
            graph.save()
            return render(request, 'chart-result.html', {'result_chart': graph, 'question': query})
    return redirect(index)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request ,user)
            return redirect(index)
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect(login_user)