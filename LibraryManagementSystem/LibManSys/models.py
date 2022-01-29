from django.db import models

# Create your models here.
class book(models.Model):
    """Model definition for post."""

    # TODO: Define fields here
    id = models.CharField(max_length=50, blank=True, null=False)
    title = models.CharField(max_length=200 , blank=True, null=False)
    author = models.CharField(max_length=200 , blank=True, null=False)
    publisher = models.CharField(max_length=200 , blank=True, null=True)

    class Meta:
        """Meta definition for post."""

        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        """Unicode representation of book."""
        return self.title