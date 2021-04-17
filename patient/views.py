from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import pandas as pd
from .models import predictions
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home.html")
        else:
             messages.info(request,'invalid credentials')
             return redirect('login')
    else:
         return render(request,'login.html')



def register(request):
    if request.method=="POST": 
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken...')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken...')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not maching...')
            return redirect('register')
            return redirect('/')
    else:
        return render(request,'register.html')



def contact(request):
    return render(request,"contact.html")
def home(request):
    return render(request,"home.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def cancer(request):
    return render(request,"cancer.html")
def predict(request):
    if request.method=='POST':
        gender=int(request.POST['gender'])
        age=int(request.POST['age'])
        smoking=int(request.POST['smoke'])
        yellow_fingers=int(request.POST['yellow'])
        anxiety=int(request.POST['anexiety'])
        peer_pressure=int(request.POST['peer'])
        chronic_disease=int(request.POST['chronic'])
        fatigue=int(request.POST['fatigue'])
        allergy=int(request.POST['allergy'])
        wheezing=int(request.POST['wheezing'])
        alcohol_consuming= int(request.POST['alcohol'])
        coughing= int(request.POST['coug'])
        shortness_of_breath = int(request.POST['short'])
        swallowing_difficulty= int(request.POST['swall'])
        chest_pain= int(request.POST['chest'])

        data=pd.read_csv(r"static\datasets\survey_lung_cancer.csv")
        Input=data.drop("lung_cancer",axis=1)
        Output=data[["lung_cancer"]]
        Input_train, Input_test, Output_train, Output_test = train_test_split(Input, Output, test_size=0.2)
        log = LogisticRegression()
        log.fit(Input_train, Output_train)
        predicting=([[gender,age,smoking,yellow_fingers,anxiety,peer_pressure,chronic_disease,fatigue,allergy,wheezing,alcohol_consuming,coughing,shortness_of_breath,
                  swallowing_difficulty,chest_pain]])
        pred = log.predict(predicting)
        lung_cancer=pred[0]
        lr=predictions(gender=gender,age=age,smoking=smoking,yellow_fingers=yellow_fingers,anxiety=anxiety,peer_pressure=peer_pressure,chronic_disease=chronic_disease,
                  fatigue=fatigue,allergy=allergy,wheezing=wheezing,alcohol_consuming=alcohol_consuming ,coughing=coughing,shortness_of_breath=shortness_of_breath,
                   swallowing_difficulty=swallowing_difficulty,chest_pain=chest_pain,lung_cancer=lung_cancer)
        lr.save()
        if(lung_cancer==1):
           r="Positive"
        else:
           r="Negative"
        if(gender==1):
          g="Female"
        else:
          g="Male"
        if(coughing==1):
            c="No"
        else:
            c="Yes"
        if(smoking==1):
            s="No"
        else:
            s="yes"
        if (alcohol_consuming == 1):
            a = "No"
        else:
            a = "yes"
        if (chest_pain == 1):
            cp = "No"
        else:
            cp= "yes"
        return render(request,'predictions.html',
                  {'predicted':r,'age':age,'gender':g,'cough':c,'smoking':s,'alcohol':a,'chest':cp})
    else:
        redirect(request,'cancer.html')









