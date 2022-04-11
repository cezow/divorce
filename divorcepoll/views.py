from pathlib import WindowsPath
from django.http import response
from django.shortcuts import render
from .models import Question
from joblib import load
import pandas as pd

def index(request):
    global listValues
    questions = Question.objects.all()

    return render(request, 'index.html', {'questions': questions})


def result(request):
    listValues = request.POST.get('listMain')
    listValues = list(map(int, listValues.split(',')))

    model = load('modelDivorce.joblib')
    cols = ["Q"+str(i) for i in range(1,55)]
    df = pd.DataFrame([listValues], columns=cols)

    result = model.predict(df)
    result = result[0]
    if result >= 0.5:
        result = 'Happy marrige'
    else:
        result = 'Divorce'
    
    return render(request, 'result.html', {'result': result})