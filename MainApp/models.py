from django.db import models


class Party(models.Model):
    name = models.CharField('Party Name', max_length=200)
    slogan = models.CharField('Party Slogan', max_length=100)
    votes = models.IntegerField('Total Votes', default=0)
    logo = models.ImageField('Party Logo', upload_to='logos')

    class Meta:
        verbose_name_plural = 'Parties'

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField('Name', max_length=200)
    position = models.CharField('Position', max_length=50)
    votes = models.IntegerField('Number of Votes', default=0)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    img = models.ImageField('Profile Picture', upload_to='profileImage')
    description = models.TextField()

    def __str__(self):
        return self.name
