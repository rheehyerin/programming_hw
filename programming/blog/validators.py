import re
import requests
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
from django.conf import settings
import mmap

#호출 가능한 객체로 만들기
@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError("Error")


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


def phone_number_validator(value):
    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')


def zip_code_validator(value):
    if not re.match(r'[0-6]\d{4}$', value):
        raise ValidationError('우편 번호 형식이 잘못되었습니다.')


def zip_code_check(value):
    with open('blog/extracted_cd.txt', 'rb', 0) as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if not s.find(str.encode(value)) != -1:
                raise ValidationError('존재하지 않는 우편 번호 입니다.')


@deconstructible
class ZipCodeValidator(object):
    def __init__(self, is_check_exist = False):
        self.is_check_exist = is_check_exist

    '''
    def __init__(self, is_check_exist = False, zipcode_cls):
        self.is_check_exist = is_check_exist
        self.
    '''

    def __call__(self, zip_code):
        if not re.match(r'^\d{5}$', zip_code):
            raise ValidationError('write in 5 digits')

        if self.is_check_exsit:
            self.check_exsit(zip_code)

    def check_exist_from_db(self, zip_code):
        from blog.models import ZipCode2
        if not ZipCode2.objects.filter(code=zip_code).exist():
            raise ValidationError('없는 우편 번호 입니다.')


    def check_exist(self, zip_code):
        parmas = {
            'regkey':settings.EPOST_API_KEY,
            'taget' : 'postNew',
            'query' : zip_code,
        }

        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response = xmltodict.parse(xml)

        try:
            error = response('error')
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))
















