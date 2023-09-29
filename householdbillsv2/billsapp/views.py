from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Bill
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required


@csrf_exempt
def newbill(request):
    procd = Bill.objects.values_list('id', flat=True)
    if request.method == "GET":
        return HttpResponse(str(procd))   
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        if id not in procd:
            newbill = Bill(**(dict(body)))
            newbill.save()
            print(newbill.id)
        else: 
            return JsonResponse({'status':f'Already Registered {id}'})
        return JsonResponse({'status':f'Success {id}'})

@login_required
def bills(request):
    if request.method == "POST" and "master" in request.POST:
            id = request.POST.get("master")
            bill = Bill.objects.get(id=id)
            bill.fullpaid = True  
            bill.save()    
            return redirect(request.path_info)
    elif request.method == "POST":
        id = request.POST.get("id")
        username = request.user.username
        if username == 'Liam':
            bill = Bill.objects.get(id=id)
            bill.liampaid = True  
            bill.save()
        elif username == 'Santi':
            bill = Bill.objects.get(id=id)
            bill.santipaid = True  
            bill.save()
        elif username == 'John':
            bill = Bill.objects.get(id=id)
            bill.johnpaid = True  
            bill.save()
        elif username == 'Sam':
            bill = Bill.objects.get(id=id)
            bill.sampaid = True  
            bill.save()
        return redirect(request.path_info)
    else:
        bills = Bill.objects.all()
        unpaid = []
        for bill in bills: 
            if bill.sampaid == True and bill.liampaid == True and bill.johnpaid == True and bill.santipaid == True:
                bill.fullpaid = True
                bill.save()
        for bill in bills:
            if bill.fullpaid != True:
                unpaid.append(bill)
        return render(request,'billsapp/bills.html', {'bills': unpaid})
        



    
 