from django.http import JsonResponse
from django.shortcuts import  render,redirect
from .models import *
import random

# Create your views here.

def index(request):
    context={'categories': Category.objects.all()}
    
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    
    return render(request,"home.html",context)

def quiz(request):
    
    context={'category': request.GET.get('category')}
    return render(request,"quiz.html",context)


def get_quiz(request):
    try:
        questions_objs=Question.objects.all()
        
        if request.GET.get('category'):
            questions_objs = questions_objs.filter(category__category_name__icontains=request.GET.get('category'))

        
        data=[]
        for ques in questions_objs:
            data.append({
                "uuid":ques.uuid,
                "category":ques.category.category_name,
                "question":ques.question,
                "marks":ques.marks,
                "answers":ques.get_answer(),
            })
        #print(data)
        random.shuffle(data)
        payload={'status': True, 'data':data}
        return JsonResponse(payload)
    
    except Exception as e:
        print("Error",e.__str__())
    
    return JsonResponse({"message":"Something Went Wrong"})