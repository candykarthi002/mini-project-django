from django.shortcuts import render, redirect
from . import table, chain
import pandas as pd 
import json

def index(request):
    json_records = table.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    columns = list(data[0].keys())[1:]
    context = {'table': data, 'columns': columns} 
    return render(request, 'index.html', context)

def ask(request):
    if request.method == "POST":
        query = request.POST.get("query")
        result = chain(query)
        generated_code = result.get("intermediate_steps")[1]
        answer = result.get("intermediate_steps")[3]
        return render(request, 'result.html', {'answer': answer, 'query': generated_code})
    return redirect(index)