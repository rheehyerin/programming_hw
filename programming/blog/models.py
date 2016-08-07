import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator
from .fields import PhoneNumberField, ZipCodeField, ZipCodeField_ver_2


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')
''' #closer의 문법 사용을 위한 것이었으나, migration의 정책상, 등록 되지 않은 함수는 migrate가 불가함. 함수 wrap의 경우 함수 안에서 만들어지는 함수이기때문에 외부에서 지정되지는 않는 함수임. 그래서 에러가 난다. 큰 문제가 되는 건 아니지만, validators.py 파일에서 실행하는 것이 더 나음.
def min_length_validator(min_length):
    def wrap(value):
        if len(value) < min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(min_length))
    return wrap

#closer
def max_length_validator(max_length):
    def wrap(value):
        if len(value) > max_length:
            raise ValidationError('{}글자를 초과하였습니다.'.format(max_length))
    return wrap

min_length_4_validator = min_length_validator(4)
'''
min_length_2_validator = MinLengthValidator(2)


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, validators = [min_length_2_validator],verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)



class Contact(models.Model):
    phone_number1 = PhoneNumberField()
    phone_number2 = PhoneNumberField()


class Member(models.Model):
    phone_number = PhoneNumberField()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    author = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ZipCode(models.Model):
    zipcode = ZipCodeField()

    def __str__(self):
        return str(self.zipcode)

class ZipCode_ver_2(models.Model):
    zipcode_2 = ZipCodeField_ver_2()

    def __str__(self):
        return str(self.ZipCode_2)

class ZipCode2(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    code = models.CharField(max_length=7)




