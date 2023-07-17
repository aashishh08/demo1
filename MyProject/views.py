from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms
from service.models import Service


def HomePage(request):

    data = {
        'title': 'Aashish',
        'student_list': [{'name': 'Aashish', 'phone': 9501049605}, {'name': 'kumar', 'phone': 9888199118}]
    }


    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome Aashish")


def course(request, courseid):
    return HttpResponse(courseid)


def calculator(request):
    res = 0
    try:
        if request.method == 'POST':
            n1 = eval(request.POST['num1'])
            n2 = eval(request.POST['num2'])
            operator = request.POST['opr']
            if operator == "+":
                res = n1 + n2
            elif operator == "-":
                res = n1 - n2
            elif operator == "*":
                res = n1 * n2
            elif operator == '/':
                res = n1 / n2
            else:
                pass





    except:
        res = "invalid operator"
    return render(request, 'calculator.html', {'output': res})


def submitForm(request, ans):
    return render(request, "Submit-form.html", ans)


def userForm(request):
    fn = userForms()
    return render(request, 'user-form.html', {'form': fn})


def check(request):
    data = {}
    try:
        if request.method == 'POST':
            num_1 = eval(request.POST['num1'])
            if num_1 == "":
                return render(request, 'checkEvenOdd.html', {'error': True})
            elif num_1 % 2 == 0:
                res = "Even"
            else:
                res = "Odd"
            data = {
                'output': res,
                'n1': num_1
            }

    except:
        print("invalid operator")
    return render(request, 'checkEvenOdd.html', data)


def service(request):
    service_data = Service.objects.all()
    if request.method == 'GET':
        service_data= ""
    return render(request, 'service-page.html', {'data': service_data})
