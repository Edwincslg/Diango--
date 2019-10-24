from django.db import models



class Note(models.Model):
    seq = models.IntegerField(default=0)
    subject = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Note002(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)
