from json.encoder import JSONEncoder
import random
import json
from django.db.models.aggregates import Count
from .models import Category, Exsam,SoalAns
from django.http.response import Http404, HttpResponse, JsonResponse
from random import randint
from django.views.decorators.csrf import csrf_exempt

  
  
  
  
  
from random import randint

def create_test(requset,id):

    if requset.method == "GET":

        try:
            return JsonResponse({"data":Exsam.objects.get(my_ID=id).soalat})

        except:
            category = Category.objects.all()
            temp = {}
            for elm in category:
                qustion = elm.soalans_set.values_list("test","optionA","optionB","optionC","optionD")
                qs = qustion.count()
                Count = 1
                for i in range(2):
                    rand = randint(0, qs-1)
                    temp[Count]=qustion[rand]
                    Count+=1
            exsam =Exsam.objects.create(my_ID=id,soalat=temp)
            return JsonResponse({"data":exsam.soalat})

@csrf_exempt
def reusalt(request,id):

    if request.method == "POST":
        try: 
            javab_user = json.loads(request.body.decode("utf-8"))
            print(type(javab_user))
            print(javab_user)
            exsam:dict =Exsam.objects.get(my_ID=id).soalat
       
            javab_exsam = []
        
            for k in exsam:
                javab_exsam.append(SoalAns.objects.get(test=exsam[k][0]).true_ans)    

            right_count = 0
            wrong_count = 0
            for v , c in zip(javab_user, javab_exsam):
                if v == c :
                    right_count+=1
                else:
                    wrong_count+=1
            return JsonResponse ({"right_count":right_count,"wrong_count":wrong_count})      
        except:
            return HttpResponse("BYE")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  