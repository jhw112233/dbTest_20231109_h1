#1)DB가 설치된 컴퓨터 내 주소 
#2)DB의 계정 ROOT
#3)DB비번 12345
#4)DB이름

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
#db와 파이썬 파일 사이의 연결통로가 생성

sql = "SELECT * FROM nember"
#sql문 생성하여 문자열로 저장

cur = conn.cursor()#커서 생성
cur.execute(sql)#sql 실행

result = cur.fetchall()

print(result[1])

for nember in result:#디비 리스트 일렬로 확인가능
    print(nember)

for nember in result:#이름만 나오게 함
    print(nember[2])

cur.close() #작성 하지 않아도 에러는 나지 않지만, db과부하 날수 있음
conn.close()



