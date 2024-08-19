from django.shortcuts import render
from VTRAPP.models import Register
from VTRAPP.models import Signup

# Create your views here.
def index(request):
    return render (request, "index.html")

def home(request):
    return render (request, "home.html")

def signup(request):
    return render (request, "signup.html")
def login(request):
    return render (request, "login.html")

def Videocall(request):
    return render (request, "Videocall.html")

def Myportfolio(request):
    return render (request, "Myportfolio.html")

def about(request):
    return render (request, "about.html")

def contact(request):
    return render (request, "contact.html")

def resume(request):
    return render (request, "resume.html")

def services(request):
    return render (request, "services.html")

def skills(request):
    return render (request, "skills.html")

def signup(request):
    if request.method=='POST':
        name = request.POST.get('name')
        Mail = request.POST.get('mail')
        Password = request.POST.get('pwd')
        Confirm_Password = request.POST.get('cpwd')
        print (name, Mail, Password, Confirm_Password)
        query = Signup (name= name, Mail=Mail, Password=Password, Confirm_Password=Confirm_Password)
        query.save()
        print ("I have done")
    return render (request, "signup.html")

def login(request):
    return render (request, "login.html")

def reg(request):
    return render (request, "reg.html")

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        mother_name = request.POST.get('mname')
        print ("I have done")
        father_name = request.POST.get('frname')
        address = request.POST.get('adrs')
        dob = request.POST.get('dob')
        print ("I have done")
        state = request.POST.get('stt')
        pin = request.POST.get('pin')
        course = request.POST.get('crs')
        print ("I have done")
        email = request.POST.get('email')
        print (last_name, mother_name, father_name, address, dob, state, pin, course, email)
        query = Register (First_Name= first_name, Last_Name= last_name, Mother_Name=mother_name, Father_Name=father_name, Address=address,States = state, DOB=dob, Pin=pin,Course=course, Email=email)
        query.save()
        print ("I have done")
    return render (request, "reg.html")

