from django.db import models

# Create your models here.

STATUS = (
    (1, 'read'),
    (2, 'currently reading'),
    (3, 'want to read'),
    (4, 'did not finish'),
)


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    CATEGORY_OF_THE_BOOK = {
        (0, 'Fantasy'),
        (1, 'Mystery and Thriller'),
        (2, 'Nonfiction'),
        (3, 'Horror'),
        (4, 'Memoir and Autobiography'),
        (5, 'Novel'),
        (6, 'Romance'),
        (7, 'Fiction')
    }

    name = models.PositiveSmallIntegerField(default=0, choices=CATEGORY_OF_THE_BOOK)

    def show_category(self):
        if self.name == 0:
            return 'Fantasy'
        elif self.name == 1:
            return 'Mystery and Thriller'
        elif self.name == 2:
            return 'Nonfiction'
        elif self.name == 3:
            return 'Horror'
        elif self.name == 4:
            return 'Memoir and Autobiography'
        elif self.name == 5:
            return 'Novel'
        elif self.name == 6:
            return 'Romance'
        elif self.name == 7:
            return 'Fiction'

    def __str__(self):
        return f"{self.show_category()}"


class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.ImageField(upload_to='cover', null=True, blank=True)
    average_rating = models.FloatField(null=True)
    thumbnail = models.URLField(null=True)


    def __str__(self):
        return self.title

