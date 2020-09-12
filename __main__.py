# -*- coding: utf-8 -*-

import sys
import pandas as pd
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup
import form

ADD_DB = 'price.xlsx'
api_key="P5hPbU%2FovAWX4wrPe5RVbi1sJBMPEHp0p8lS4Uz2TXZxuqbDVDXhAw%2Bi0vYZYt0%2BQ22vKj2G62vM9Kbw1MMq3A%3D%3D"

class MainDialog(QDialog, form.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        #uic.loadUi('form.ui', self)
        self.setupUi(self) ## qt designer 변환후 추가   1. import form, 2. form.Ui_Dialog 3. self.setupUi(self) 4. uic 삭제

        self.pushButton.clicked.connect(self.load_BTN_clicked)
        self.pushButton_cal.clicked.connect(self.calculate_clicked)
        self.pushButton_3.clicked.connect(self.clear_tableWidget)
        self.pushButton_4.clicked.connect(self.extract_tableWidget)
        self.pushButton_cal_2.clicked.connect(self.percent_cal_clicked)


    def load_BTN_clicked(self):

        print('load_BTN_clicked!@')
        ###  엑셀 표로 불러오기
        self.df = pd.read_excel(ADD_DB, encoding='cp949')
        self.df.drop_duplicates('pnu', keep='first', inplace=True)  ## 중복행 삭제 ##

        self.setTableWidgetData(self.df)


    def setTableWidgetData(self, df):
        # 필요한사항 정리
        print("테이블 셋팅!!!")
        #엑셀 불러온 df 그래프로 표현
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))

        col_head = df.columns

        self.tableWidget.setHorizontalHeaderLabels(col_head)

        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def clear_tableWidget(self):
        self.tableWidget.clear()


    def extract_tableWidget(self):
        self.df_final_2.to_excel('result.xlsx')


    def calculate_clicked(self):
        self.year = self.lineEdit_year.text()

        self.Public_API()



    def Public_API(self):
        ### 변수초기화
        self.rows_1 = []
        self.rows_2 = []
        self.rows_3 = []
        self.rows_4 = []

        self.stdrYear = self.year
        self.address = self.df.iloc[:,0].astype('str')

        total = self.df.shape[0]
        n1 = 0

        for i in self.address:

            self.IndvdLandPriceService(i, self.stdrYear)
            self.LadfrlService(i, self.stdrYear)
            self.IndvdHousingPrice(i, self.stdrYear)
            self.ApartHousingPrice(i, self.stdrYear)

            n1 += 1
            print(n1 / total * 100, '%')


        col_1 = ['pnu', 'pblntfPclnd']
        self.df_1 = pd.DataFrame(self.rows_1, columns=col_1).astype('str') ###

        col_4 = ['pnu', 'lndpclAr']
        self.df_4 = pd.DataFrame(self.rows_4, columns=col_4).astype('str') ###

        col_2 = ['pnu', 'ladRegstrAr', 'calcPlotAr', 'buldAllTotAr', 'buldCalcTotAr', 'housePc']
        self.df_2 = pd.DataFrame(self.rows_2, columns=col_2).astype('str') ###

        col_3 = ['pnu', 'totalCount', 'prvuseAr', 'pblntfPc']
        self.df_3 = pd.DataFrame(self.rows_3, columns=col_3).astype('str') ###

        self.df_1['lndpclAr']= self.df_4['lndpclAr']
        self.df_temp = pd.merge(self.df_1, self.df_2, how='outer')
        self.df_final = pd.merge(self.df_temp, self.df_3, how='outer')


        self.df_final_2 = self.df_final.iloc[:,1:].astype(float)
        self.df_final_2['pnu'] = self.df_final['pnu']


        ############### pnu를 맨앞으로 불러오기
        cols = self.df_final_2.columns.tolist()
        tmp = cols[-1]
        del cols[-1]
        cols.insert(0, tmp)
        self.df_final_2 = self.df_final_2[cols]

        self.df_final_2['totalCount'].fillna(1, inplace=True)
        self.df_final_2.fillna(0, inplace=True)

        self.df_final_2["토지가격"] = self.df_final_2['pblntfPclnd'] * self.df_final_2['lndpclAr'] / self.df_final_2['totalCount']
        self.df_final_2["개별주택가격"] = self.df_final_2['housePc']
        self.df_final_2["공동주택가격"] = self.df_final_2['pblntfPc']

        self.df_final_2["총가격"] = self.df_final_2["토지가격"] + self.df_final_2["개별주택가격"] + self.df_final_2["공동주택가격"]

        self.setTableWidgetData(self.df_final_2)

    def percent_cal_clicked(self):

        self.land = float(self.lineEdit_land.text())
        self.building = float(self.lineEdit_building.text())
        self.land_p = self.land / (self.land + self.building) * 2
        self.building_p = self.building / (self.land + self.building) * 2

        self.df_final_2["총가격_비율"] = self.df_final_2["토지가격"] * self.land_p + (self.df_final_2["개별주택가격"] + self.df_final_2["공동주택가격"]) * self.building_p
        self.setTableWidgetData(self.df_final_2)

    def IndvdLandPriceService(self, pnu, stdrYear):  # 1. 개별공시지가정보서비스 : 지역코드(19자리), 년도
        numOfRows = '1000'  # 한번 노출 시 불러들이는 거래정보 량
        pageNo = '1'  # 시작 페이지... 1회 호출에 10000건이 넘을 경우 다음페이지로 다시 호출 해야 함.
        Format = 'xml'

        url = 'http://apis.data.go.kr/1611000/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr?pnu=%s&stdrYear=%s&ServiceKey=%s&format=%s&numOfRows=%s&pageNo=%s' %(pnu, stdrYear, api_key, Format, numOfRows, pageNo)

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml-xml')
        it = soup.select('field')

        for node in it:
            n_pnu = node.find('pnu').text
            n_pblntfPclnd = node.find('pblntfPclnd').text  # 공시지가 (원/m2)

            self.rows_1.append({'pnu': n_pnu,
                                'pblntfPclnd': n_pblntfPclnd})

        return self.rows_1


    def IndvdHousingPrice(self, pnu, stdrYear):  # 2. 개별주택가격정보서비스 : 지역코드(19자리), 년도
        numOfRows = '1000'  # 한번 노출 시 불러들이는 거래정보 량
        pageNo = '1'  # 시작 페이지... 1회 호출에 10000건이 넘을 경우 다음페이지로 다시 호출 해야 함.
        Format = 'xml'

        url = 'http://apis.data.go.kr/1611000/nsdi/IndvdHousingPriceService/attr/getIndvdHousingPriceAttr?pnu=%s&stdrYear=%s&ServiceKey=%s&format=%s&numOfRows=%s&pageNo=%s' % (
        pnu, stdrYear, api_key, Format, numOfRows, pageNo)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml-xml')
        it = soup.select('field')

        for node in it:
            n_pnu = node.find('pnu').text
            n_ladRegstrAr = node.find('ladRegstrAr').text  # 토지대장 면적 (m2)
            n_calcPlotAr = node.find('calcPlotAr').text  # 산정대지 면적 (m2)
            n_buldAllTotAr = node.find('buldAllTotAr').text  # 건물 전체 연면적 (m2)
            n_buldCalcTotAr = node.find('buldCalcTotAr').text  # 건물 산정 연면적 (m2)
            n_housePc = node.find('housePc').text  # 주택가격

            self.rows_2.append({'pnu': n_pnu,
                                'ladRegstrAr': n_ladRegstrAr,
                                'calcPlotAr': n_calcPlotAr,
                                'buldAllTotAr': n_buldAllTotAr,
                                'buldCalcTotAr': n_buldCalcTotAr,
                                'housePc': n_housePc})

        return self.rows_2


    def ApartHousingPrice(self, pnu, stdrYear):  # 3. 공동주택가격정보서비스 : 지역코드(19자리), 년도
        numOfRows = '1000'  # 한번 노출 시 불러들이는 거래정보 량
        pageNo = '1'  # 시작 페이지... 1회 호출에 10000건이 넘을 경우 다음페이지로 다시 호출 해야 함.
        Format = 'xml'

        url = 'http://apis.data.go.kr/1611000/nsdi/ApartHousingPriceService/attr/getApartHousingPriceAttr?pnu=%s&stdrYear=%s&ServiceKey=%s&format=%s&numOfRows=%s&pageNo=%s' % (
        pnu, stdrYear, api_key, Format, numOfRows, pageNo)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml-xml')

        count = soup.select('response')
        for n in count:
            n_totalCount = n.find('totalCount').text  # 한개의 주소에 등록된 집주소의 숫자

        it = soup.select('field')
        for node in it:
            n_pnu = node.find('pnu').text  # 고유번호
            n_prvuseAr = node.find('prvuseAr').text  # 전용면적(m2)
            n_pblntfPc = node.find('pblntfPc').text  # 공시가격(원)

            self.rows_3.append({'pnu': n_pnu,
                                'totalCount': n_totalCount,
                                'prvuseAr': n_prvuseAr,
                                'pblntfPc': n_pblntfPc})

        return self.rows_3


    def LadfrlService(self, pnu, stdrYear):  # 4. 토지임야정보조회서비스 : 지역코드(19자리), 년도
        numOfRows = '1000'  # 한번 노출 시 불러들이는 거래정보 량
        pageNo = '1'  # 시작 페이지... 1회 호출에 10000건이 넘을 경우 다음페이지로 다시 호출 해야 함.
        Format = 'xml'

        url = 'http://apis.data.go.kr/1611000/nsdi/eios/LadfrlService/ladfrlList.xml?pnu=%s&stdrYear=%s&ServiceKey=%s&format=%s&numOfRows=%s&pageNo=%s' % (
        pnu, stdrYear, api_key, Format, numOfRows, pageNo)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml-xml')
        it = soup.select('ladfrlVOList')

        for node in it:
            n_pnu = node.find('pnu').text  # 고유번호
            n_lndpclAr = node.find('lndpclAr').text  # 면적(m2)

            self.rows_4.append({'pnu': n_pnu,
                                'lndpclAr': n_lndpclAr})

        return self.rows_4



app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()
