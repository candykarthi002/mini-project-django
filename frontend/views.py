from django.shortcuts import render, redirect
from . import table, chain
import pandas as pd
import json
from .models import Chat

def index(request):
    json_records = table.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    columns = list(data[0].keys())[1:]
    chat = Chat.objects.all()
    context = {'table': data, 'columns': columns, 'chat': chat} 
    return render(request, 'index.html', context)

def ask(request):
    if request.method == "POST":
        query = request.POST.get("query")
        result = chain(query)
        if result:
            generated_code = result.get("intermediate_steps")[1]
            answer = result["result"]
            chat = Chat(question=query, query_text=generated_code, answer=answer)
            chat.save()
        return render(request, 'result.html', {'chat': chat})
    return redirect(index)