import pymysql

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def database_connect():
    conn = pymysql.connect(user="root", passwd="000000", db="student_score", host='127.0.0.1')
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # database 연결 및 데이터 조회
    sql = "SELECT * FROM student_score.score;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return pd.DataFrame(result)

class AverageLinear:
    def __init__(self):
        self.model = LinearRegression(n_jobs=-1)
        self.X = database_connect().values[:, : database_connect().shape[1] - 1]
        self.y = database_connect().values[:, database_connect().shape[1] - 1]
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
