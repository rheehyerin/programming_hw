import os
os.environ.setdefault("DJANGO_SETTINGS_MODULES", "programming.settings")
import django
djnago.setup()

import csv

CSV_PATH = ''

reader = csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter='|')

from blog.models import ZipCode2

columns = next(reader)

zip_code_list = []

for idx, row in enumerate(reader):
    data = dict(zip(columns, row))
    zip_code = ZipCode2(
        city=data['시도'],
        road=data['도로명'],
        dong=data['법정동명'],
        gu=data['시군구'],
        code=data['우편번호']
        )
    zip_code_list.append(zip_code)

print('zip_code size : {}'.format(len(zip_code_list)))
ZipCode2.objects.bulk_create(zip_code_list, 100)
#뒷자리에 있는 인자는 100개 단위로 끊어서 날리는게 디비에 부담을 주지 않는다. 모든 상황에 따라 100개가 될 수도 1000개가 될 수도 있다.