from django.shortcuts import render
import requests

SaveChat=[]
botchat=[]

def home(request):
  userpost = 'hey'
  if request.method == "POST":
    userpost =request.POST['myvalue']
  print(userpost)  
  myurl='https://api.dialogflow.com/v1/query?v=20150910&contexts=smalltalk&lang=en&query='+userpost+'&sessionId=12345&timezone=America/New_York'
  Headers = {
    'Authorization': 'Bearer a5aaf3c137ce49b1ae3710de1528036e',
  } 
  r =requests.get(myurl, headers=Headers)
  print("The response", r.json()['result']['fulfillment']['speech'])

  SaveChat.append(userpost)
  SaveChat.append(r.json()['result']['fulfillment']['speech'])
  UserChat={'Chat1': SaveChat}
  #BOTChat={'Bot':UserChat }

  # rendering the template in templates folder
  return render(request, "app.html",UserChat )


