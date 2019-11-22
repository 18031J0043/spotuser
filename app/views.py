from django.shortcuts import render
import pyrebase
# Create your views here.
from django.http import HttpResponse
from django.contrib import auth

config = {
    "apiKey": "AIzaSyDqixuuv9s9wTuGyPYg7aPkp4t1SPpSUZI",
    "authDomain": "spotme-cadbd.firebaseapp.com",
    "databaseURL": "https://spotme-cadbd.firebaseio.com",
    "projectId": "spotme-cadbd",
    "storageBucket": "spotme-cadbd.appspot.com",
    "messagingSenderId": "310507672139",
    "appId": "1:310507672139:web:d25515d874640bfbe933ce",
    "measurementId": "G-R04HBJKRJM"
}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
# def index(request):
#     return render("Hello, world. You're at the polls index.")
def signin(request):
    return render (request,"signIn.html")

def postsignin(request):
    email=request.POST.get('email')
    passw=request.POST.get("pass")
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request, "signIn.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"welcome.html",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,"signIn.html")

def signup(request):
    return render(request,"signup.html")


def postsignup(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request, "signup.html", {"messg": message})

    return render(request, "signIn.html")


def create(request):

    return render(request, 'create.html')


def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    work = request.POST.get('work')
    progress = request.POST.get('progress')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    data = {
        "work": work,
        'progress': progress
    }
    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child(
        'details').child('name').get().val()
    return render(request, 'welcome.html', {'e': name})



