import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')
#db와 파이썬 파일 사이의 연결통로가 생성

sql = "INSERT INTO nember VALUES('blackcat','12345','이순신','010-8888-9999','경기도 안산시','61')"
#반드시 작은따옴표로 넣고, 끝에 세미콜론 제외



cur = conn.cursor()#커서 생성
cur.execute(sql)#sql 실행

cur.close() #커서종료
conn.commit()# insert,delete, update sql문을 사용한 경우에는 반드시 commit해야 한다
conn.close()#커넥션 종료
