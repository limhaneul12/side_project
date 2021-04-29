from flask import Flask, render_template, request
from average_prediction import AverageLinearRegression as AL
from average_prediction import linear_prediction as lp
import numpy as np

app = Flask(__name__)

@app.route('/')
def average():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result_average():
    if request.method == 'POST':
        result = request.form
        load = [int(result[i]) for i in result]
        score_data = AL(load[0], load[1], load[2], load[3], load[4], load[5])
        average_data = score_data.data_saving_average()
        print(average_data)

        return render_template('index_result.html', average_data=average_data)

@app.route('/predict', methods=['POST', 'GET'])
def predict_average():
    if request.method == 'POST':
        result = request.form
        load = [int(result[i]) for i in result]
        predict_data = lp(time=np.array(load[0]).reshape(-1, 1))

        return render_template('index_predict.html', predict_data=predict_data)


if __name__ == "__main__":
    app.run(debug=True)
