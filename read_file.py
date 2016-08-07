import csv

CSV_PATH =""

reader = csv.reader(opne(CSV_PATH, 'rt', encoding='cp494'), delimiter="|")

columns = next(reader)

for idx, row in enumerate(reader):
    row = dict(zip(columns, row))
    print(data['우편번호'])
    if idx > 100:
        break


#만약 db에 있는 데이터를 가져 오는 경우라면
'''
    유니코드로 사용하다가 데이터를 가장 마지막에 밖으로 내보내야 할 때 인코딩을 한다.
    cp949 = 한글 문자열만 처리 가능함.
    utf8 = 모든 언어를 다 통달.

    msql의 경우
    create database (default encoding="utf8")

    unicode >> utf8 : decoding
    utf8 >> unicode : encoding

'''