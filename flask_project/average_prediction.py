import pymysql
import joblib
import pandas as pd

def linear_prediction(time):
    linear = joblib.load("score.pkl")
    score_prediction = linear.predict(time)
    return score_prediction

class DataBase:
    def __init__(self):
        self.conn = pymysql.connect(user="root", passwd="000000", db="student_score", host='127.0.0.1')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def database_select(self):
        # database 연결 및 데이터 조회
        sql = "SELECT * FROM student_score.score;"
        self.cursor.execute(sql)
        return pd.DataFrame(self.cursor.fetchall())

    def database_insert(self, average, study_time):
        sql = """INSERT INTO score(평균, 공부시간) VALUES (%s, %s)"""
        db = self.cursor.execute(sql, (average, study_time))
        return self.conn.commit()

class AverageLinearRegression:
    def __init__(self, korean, english, math, social, science, time):
        self.korean = korean
        self.english = english
        self.math = math
        self.social = social
        self.science = science
        self.time = time

    # 총합
    def get_sum(self):
        return self.korean + self.english +\
               self.math + self.social + self.science

    # 데이터 저장 및 평균
    def data_saving_average(self):
        average = self.get_sum() / 5
        saving = DataBase().database_insert(average, self.time)
        return average

