from django.contrib.auth.models import User
from django.db import models


class AdderGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    total = models.IntegerField(default=10)


class AdderQuestion(models.Model):
    game = models.ForeignKey(AdderGame, on_delete=models.CASCADE, related_name='questions')
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    user_answer = models.IntegerField()
    correct = models.BooleanField()
