from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    
    #se o usuário postar diversos posts e logo depois deletar a sua conta, esta linha de código apaga os posts feitos por ele.
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField()

    def __str__(self):
        return self.title + ' - ' + str(self.author)
