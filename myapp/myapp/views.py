from django.http import HttpResponse
import datetime
from django.shortcuts import render


# this is index page views
def home(request):

    isActive =True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True

    date = datetime.datetime.now()
    name = "Code Singh"
    list_of_programs = [
        'WAP to check even or odd numbers',
        'WAP to check pirme numbers',
        'WAP to print all the prime numbers from 1 to 100',
        'WAP to print pascals numbers'
    ]
    student={
        "student_name":"Swag Singh",
        "student_college":"Student University",
        "student_city":"Noida"
    }

    # preparing the data to send it to the home page

    data = {
        "date":date,
        "isActive":isActive,
        "name" :name,
        "list_of_programs":list_of_programs,
        "student_data":student
    }
    # return HttpResponse("<h1>Hello this is a Home page</h1>")
    return render(request,"home.html",data)



# views function for current time and date
def currrent_time_date(request):
    date = datetime.datetime.now()
    print("current function is called form view")
  
    return HttpResponse("<h1>hello this is a index page</h1> "+str(date))




# views function for about page
def about_page(request):
    print("this is about page")
    # return HttpResponse("<h1> This is About page</h1>")
    return render(request,"about.html",{})




def services(request):
    print("this is services page")
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,"services.html",{})
