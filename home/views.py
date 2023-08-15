from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import random

# Create your views here.

def index(request):
    return JsonResponse({
        "message":"This is Home Page"
    })


def get_quiz(request):
    try:
        questions_objs=Question.objects.all()
        data=[]
        for ques in questions_objs:
            data.append({
                "category":ques.category.category_name,
                "question":ques.question,
                "marks":ques.marks,
                "answers":ques.get_answer(),
            })
            random.shuffle(data)
        
        payload={'status': True, 'data':data}
        
        
        return JsonResponse(payload)
    
    except Exception as e:
        print("Error",e.__str__())
    
    JsonResponse({"message":"Something Went Wrong"})