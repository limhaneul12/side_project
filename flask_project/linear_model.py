import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('subject_score.csv')
X = data[["time"]]
y = data[["score"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020, shuffle=True)

linear = LinearRegression(n_jobs=-1, normalize=True)
linear.fit(X_train, y_train)
y_predict = linear.predict(X_test)

plt.plot(X_test, y_test, 'o')
plt.plot(X, linear.predict(X.values.reshape(-1, 1)))
plt.show()
