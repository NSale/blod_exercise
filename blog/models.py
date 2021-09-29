from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(default='', null=False, max_length=200)
    image = models.CharField(max_length=50)
    date = models.DateTimeField(verbose_name='date')
    slug = models.SlugField(max_length=30, default='', null=False, db_index=True)
    content = models.TextField(default='', null=False, max_length=2000)
    author = models.ForeignKey(Author, null=False, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.title} {self.date}'
