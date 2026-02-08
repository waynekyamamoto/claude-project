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


class WordleGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=5)
    won = models.BooleanField()
    attempts = models.IntegerField()
    played_at = models.DateTimeField(auto_now_add=True)


class WordleGuess(models.Model):
    game = models.ForeignKey(WordleGame, on_delete=models.CASCADE, related_name='guesses')
    guess_number = models.IntegerField()
    word = models.CharField(max_length=5)


# --- Transparency Analytics Models ---

class CreditRating(models.Model):
    issuer = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    outlook = models.CharField(max_length=50)
    is_previous = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.issuer} - {self.rating}"


class Insight(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    external_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)
    photo_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Methodology(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Methodologies'

    def __str__(self):
        return self.title


class FAQItem(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"


class RatingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} ({self.status})"


class RatingRequestDocument(models.Model):
    request = models.ForeignKey(RatingRequest, on_delete=models.CASCADE, related_name='documents')
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='rating_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


class RatingRequestMessage(models.Model):
    request = models.ForeignKey(RatingRequest, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Message by {self.user.username} on {self.created_at:%Y-%m-%d}"
