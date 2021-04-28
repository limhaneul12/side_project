import pymysql
import joblib
import pandas as pd

class DataBase:
    def __init__(self):
        self.conn = pymysql.connect(user="root", passwd="000000", db="student_score", host='127.0.0.1')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def database_select(self):
        # database 연결 및 데이터 조회
        sql = "SELECT * FROM student_score.score;"
        self.cursor.execute(sql)
        return pd.DataFrame(self.cursor.fetchall())

    def database_insert(self, average, study_time, predict_study):
        sql = """INSERT INTO score(평균, 공부시간, 예상공부시간) VALUES (%s, %s, %s)"""
        db = self.cursor.execute(sql, (average, study_time, predict_study))
        return self.conn.commit()

class AverageLinearRegression:
    def __init__(self, korean, english, math, social, science, time, predict_time):
        self.korean = korean
        self.english = english
        self.math = math
        self.social = social
        self.science = science
        self.time = time
        self.predict_time = predict_time

        self.X = DataBase().database_select().values[:, 1:2]

    # 총합
    def get_sum(self):
        return self.korean + self.english +\
               self.math + self.social + self.science

    # 데이터 저장 및 평균
    def data_saving_average(self):
        average = self.get_sum() / 5
        saving = DataBase().database_insert(average, self.time, self.predict_time)

    def linear_prediction(self):
        linear = joblib.load("score.pkl")
        score_prediction = linear.predict(self.X)
        return score_prediction

