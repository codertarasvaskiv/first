from django.db import models


class Number(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other):
        return super().__eq__(other)


class TimeDate(models.Model):
    time = models.DateTimeField()
    number_id = models.ForeignKey(Number, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time)

    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other):
        return super().__eq__(other)




