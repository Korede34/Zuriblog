from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('post-detele', kwargs={'pk': self.pk})

    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username