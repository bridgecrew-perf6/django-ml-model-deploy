from django.shortcuts import render,redirect
from django.http import HttpResponse
import numpy as np
import pandas as pd

import joblib as jb
modelReload=jb.load('./Model/Model.pkl')
i=0
def result(request):
    array=np.array([[int(request.GET['duration']),int(request.GET['budget']),float(request.GET['imdb']),int(request.GET['likes'])]])
    modelReload.predict(array)
    return render(request,'prediction.html',{'result':int(modelReload.predict(array)[0])})

def ML_model(request):
   return  render(request,'index.html')
def predictform(request):
    return render(request,'prediction.html')

def dataset(request):
    data=pd.read_csv('./Model/Movie_data1 - Sheet1.csv')
    data_html=data.to_html()
  
    # response = HttpResponse()
    # res= response.write(data_html)
    return HttpResponse("<title>Dataset</title><style> body{ width:100%; background-color : rgb(16, 24, 54);} h1{color: white;}table {padding : 10px;border-width: 5px;width: 90%}  thead tr,th { color:red; border-width :1px; border-color: yellow;} tbody td {color:white;}</style>"+"<h1>Movie IMDb Dataset......</h1>"+ data_html)
    # context={'load_data':res}
    # return render(request,'dataset.html',context)