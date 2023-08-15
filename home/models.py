import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
class Question(BaseModel):
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answer(self):
        answer_objs=Answer.objects.filter(question=self)
        data=[]
        
        for ans in answer_objs:
            data.append({
                'answer':ans.answer,
                'is_correct':ans.is_correct
            })
        return data

class Answer(BaseModel):
    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.answer