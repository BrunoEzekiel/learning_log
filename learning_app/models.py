from django.db import models

# Create your models here.
class Topic(models.Model):#titulo do assunto .
    texto = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''devolve uma representaçao em string do modelo'''
        return self.texto

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    texto = models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural ='entries'

    def __str__(self):
        return self.texto[:50] + '...' 