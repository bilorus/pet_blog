from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', editable=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(unidecode(self.title))
            all_slugs = Post.objects.values('slug')
            while any(map(lambda item: item['slug'] == new_slug, all_slugs)):
                new_slug += '-1'
            self.slug = new_slug
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.author}'

    class Meta:
        ordering = ['-time_create']