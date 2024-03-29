from django.db import models
from django.contrib.auth. models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=400, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'blog_posts')
    updated_on = models.DateField(auto_now= True)
    created_on = models.DateField(auto_now_add= True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title