import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import pymysql

form_class =uic.loadUiType("ui/join2.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입 프로그램")

        #버튼연결
        self.check_btn.clicked.connect(self.idCheck)
        self.join_btn.clicked.connect(self.joinCheck)
        self.login_btn.clicked.connect(self.memberLogin)

    def idCheck(self):
        memberid = self.memberid_edit.text()  # 회원아이디로 입력된 아이디 텍스트 가져오기
        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM nember WHERE memberid='{memberid}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # sql 실행

        result = cur.fetchone()


        if result == None: #회원가입 가능
            QMessageBox.warning(self,'가입가능','입력하신 아이디는 가입 가능한 아이디 입니다.')

        else:
            QMessageBox.warning(self,'가입불가','이미 존재하는 아이디 입니다.')


        cur.close()
        conn.close()

    def joinCheck(self):
        memberid = self.memberid_edit.text()
        memberpw = self.memberpw_edit.text()
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        address = self.address_edit.text()
        age = self.age_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"INSERT INTO nember VALUES ('{memberid}', '{memberpw}', '{name}', '{phone}', '{address}', '{age}')"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # SQL문 실행



        conn.commit()  # insert, delete, update sql문을 사용한 경우에는 반드시 commit 해줘야 함!
        cur.close()
        conn.close()
    def memberLogin(self):
        loginid = self.loginid_edit.text()
        loginpw = self.loginpw_edit.text()

        conn = pymysql.connect(host='localhost', user='root', password='12345', db='memberdb')

        sql = f"SELECT * FROM nember WHERE memberid='{loginid}' and memberpw='{loginpw}'"

        cur = conn.cursor()  # 커서 생성
        cur.execute(sql)  # sql 실행

        result = cur.fetchone()


        # if result==None:
        #     self.logintext_label.setText('로그인실패.')
        # else:
        #     self.logintext_label.setText('성공')
        #     #select memberpw from memberf where memberid='{}'
        #     #result[1]==
        if result == None:
            self.logintext_label.setText('로그인 실패. 아이디 또는 비밀번호를 확인하세요.')
        else:
            self.logintext_label.setText('로그인 성공!')
        cur.close()
        conn.close()






if __name__=='__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())