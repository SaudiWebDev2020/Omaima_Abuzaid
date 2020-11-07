from django.shortcuts import render, redirect
from .models import users
# other imports
from .models import users
# show all of the data from a table
def index(request):
    context = {
        'users': users.objects.all()
    }
    return render(request, "index.html", context)

def new_user (request):
    if request.method=='POST':
        users.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],
        email_address=request.POST['email'], age=int(request.POST['age']))

    return redirect('/')
