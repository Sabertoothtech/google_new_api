from django.shortcuts import render
from math import sqrt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from sqlalchemy import create_engine
from GoogleNews import GoogleNews
#from newspaper import Article
import pandas as pd
from datetime import date
from datetime import date
import datetime

today = date.today()

@api_view(['GET'])
def get_news(request,name):
    googlenews=GoogleNews(start=today-datetime.timedelta(days=6),end=today)
    googlenews.search(name)
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(df.head())
    return Response(df)

