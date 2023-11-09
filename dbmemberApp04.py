import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class =uic.loadUiType("ui/ed.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원조회 프로그램")
        
        self.search_btn.clicked.connect(self.db_search)#조회 버튼 누르면 db 서치 함수 호출
        self.modify_btn.connect(self.db_modify)#조회 버튼 누르면 db 모디파이 함수 호출
        self.reset_btn.connect(self.db_modify)  # 조회 버튼 누르면 db 모디파이 함수 호출

        #db서치 함수만들기
    def db_search(self):
        memberid = self.memberid_edit.text()#회원아이디로 입력된 아이디 텍스트 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM nember WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # sql 실행

        result = cur.fetchone()
        #print(result)
        if result != None:
            self.memberpw_edit.setText(result[1])
            self.name_edit.setText(result[2])
            self.phone_edit.setText(result[3])
            self.address_edit.setText(result[4])
            self.age_edit.setText(str(result[5]))  # age는 정수 이므로 문자열 변환
        else:
            self.memberpw_edit.setText('회원정보없음')
            self.name_edit.setText('회원정보없음')
            self.phone_edit.setText('회원정보없음')
            self.address_edit.setText('회원정보없음')
            self.age_edit.setText(str('회원정보없음'))  # age는 정수 이므로 문자열 변환

        #db모디파이 함수만들기

        def db_modify(self):
            memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기
            memberpw = self.memberpw_edit.text() # 회원비밀번호로 입력된 아이디 텍스트 가져오기
            name = self.name_edit.text()
            phone = self.phone_edit.text()
            address = self.address_edit.text()
            age = self.age_edit.text()

            conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

            sql=(f"UPDATE member SET memberpw='{memberpw}',name='{name}',"
                 f"phone='{phone}',adress='{address}',memberage={age} WHERE memberid='{memberid}")

            cur = conn.cursor()  # 커서 생성
            cur.execute(sql)  # sql 실행
            result = cur.fetchone()

            cur.close()  # 작성 하지 않아도 에러는 나지 않지만, db과부하 날수 있음
            conn.close()

        def reset(self):
            self.memberpw_edit.clear()
            self.name_edit.clear()
            self.phone_edit.clear()
            self.address_edit.clear()
            self.age_edit.clear()


if __name__=='__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())