from django.db import models

class Blog(models.Model):   # models.Model 상속
    title = models.CharField(max_length=200) #CharField 제한이 있다
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField() #TextField 제한이 없다

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

#python manage.py makemigrations: imgration 폴더에 models.py의 변경사항 저장
#python manage.py migrate: imgration 폴더 실행시켜 데이터베이스에 적용
