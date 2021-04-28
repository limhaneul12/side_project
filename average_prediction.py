import pymysql

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class DataBase:
    def __init__(self):
        self.conn = pymysql.connect(user="root", passwd="000000", db="student_score", host='127.0.0.1')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def database_select(self):
        # database 연결 및 데이터 조회
        sql = "SELECT * FROM student_score.score;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return pd.DataFrame(result)

class Score:
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

    # 평균
    def get_average(self):
        average = self.get_sum() / 5

        sql = """INSERT INTO score(국어, 영어, 수학, 사회, 과학, 평균, 공부시간) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (self.korean, self.english, self.math, self.social, self.science, average, self.time)
        db = DataBase()
        data_base_into = db.cursor.execute(sql, data)
        db.conn.commit()

class AverageLinear:
    def __init__(self):
        self.model = LinearRegression(n_jobs=-1)
        self.X = DataBase().database_select().values[:, 1: DataBase().database_select().shape[1] - 1]
        self.y = DataBase().database_select().values[:, DataBase().database_select().shape[1] - 1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3,
                                                                                shuffle=True, random_state=2021)

    def linear_prediction(self):
        linear = self.model.fit(self.X_train, self.y_train)
        model_prediction = linear.predict(self.X_test)

        return model_prediction

    def score_prediction_visualization(self):
        plt.scatter(self.y_test, self.linear_prediction(), alpha=0.4)
        plt.xlabel("score")
        plt.ylabel("subject")
        plt.title("score average or prediction")
        plt.show()


test = AverageLinear().linear_prediction()


