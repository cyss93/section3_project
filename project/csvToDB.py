import csv
import sqlite3

fileName = 'CarPrice.csv'
file = open(fileName, 'r', encoding="unicode_escape")
reader = csv.reader(file)

# db생성, table 생성
dbConn = sqlite3.connect('C:/Users/dhckd/CodestatesSection3/project/CarPriceDB.db')
cs = dbConn.cursor()

sqlscript = """CREATE TABLE CarPrice(
    car_ID INTEGER,
    symboling INTEGER,
    CarName VARCHAR(60),
    fueltype VARCHAR(30),
    aspiration VARCHAR(30),
    doornumber VARCHAR(30),
    carbody VARCHAR(30),
    drivewheel VARCHAR(30),
    enginelocation VARCHAR(30),
    wheelbase REAL,
    carlength REAL,
    carwidth REAL,
    carheight REAL,
    curbweight INTEGER,
    enginetype VARCHAR(30),
    cylindernumber VARCHAR(30),
    enginesize INTEGER,
    fuelsystem VARCHAR(30),
    boreratio REAL,
    stroke REAL,
    compressionratio REAL,
    horsepower INTEGER,
    peakrpm INTEGER,
    citympg INTEGER,
    highwaympg INTEGER,
    price INTEGER
    )"""
cs.execute(sqlscript)
# dbConn.commit()



# csv DB로 저장

arr = []

for row in reader:
    arr.append(row)

for row in arr:
    strSQL = 'INSERT INTO CarPrice(car_ID, symboling, CarName, fueltype, aspiration, doornumber, carbody, drivewheel,  enginelocation,  wheelbase, carlength, carwidth, carheight, curbweight, enginetype,  cylindernumber,  enginesize,  fuelsystem,  boreratio,  stroke, compressionratio, horsepower, peakrpm, citympg,  highwaympg, price)values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cs.execute(strSQL, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25]))
# 맨 윗줄에 컬럼명이 저장됨. 이를 삭제해주자
DEL_FIRST = """DELETE FROM CarPrice WHERE car_ID = 'car_ID'"""
cs.execute(DEL_FIRST)
dbConn.commit()

print('csv파일의 데이터가 DB에 입력되었습니다.')

cs.close()
dbConn.close()