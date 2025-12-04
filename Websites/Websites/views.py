from django.http import HttpResponse
from django.shortcuts import render

def render_page(request):
    data={
            'login':'Login Page',
            'welcome':'Welcome to the login page',
            'names':["siddhu","shiva","achyut","eswar","hemalath","yadaiah",],
            'details':[{'name':'siddhu','id':'71375'}, {'name':'shiva','id':'71388'}]
          }
    return render(request,"login.html",data)




