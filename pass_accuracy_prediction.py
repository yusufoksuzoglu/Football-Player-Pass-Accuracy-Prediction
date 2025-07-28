import pandas as pd

import numpy as np

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error

from sklearn.linear_model import SGDRegressor

from sklearn.preprocessing import StandardScaler

# DataFrame oluştur
x_train = pd.DataFrame(identity_of_footballers_train, index=footballers_train)
y_train = pd.Series(footballers_numeric, index=footballers_train)

# Model oluştur ve eğit
model = LinearRegression()
model.fit(x_train, y_train)

# Ağırlıkları ve bias'ı yazdır
w = model.coef_
b = model.intercept_
print("w:", w)
print("b:", b)

x_kimmich = x_train.loc["Joshua Kimmich"]
y_predict_kimmich = np.dot(w, x_kimmich) + b
print("Kimmich's pass accuracy prediction:", y_predict_kimmich)
y_predict = model.predict(x_train)
print("y_predict:", y_predict)

mean_squared_errors = mean_squared_error(y_train, y_predict)
print("mean squared error: ", mean_squared_errors)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
model = SGDRegressor(learning_rate = 'constant', eta0 = 0.01, max_iter = 1000)
model.fit(x_train_scaled, y_train)

w = model.coef_
b = model.intercept_
print("w:", w)
print("b:", b)

y_predict = model.predict(x_train_scaled)
print("y_predict:", y_predict)
mean_squared_errors = mean_squared_error(y_train, y_predict)
print("mean squared error: ", mean_squared_errors)

x_new = [ [80, 95, 85, 95, 85, 90] ] #Xavi Hernandez : [ Orta Saha, Barcelona, Pep, 95, Spain, Orkestra Şefi]
x_new_scaled = scaler.transform(x_new)
y_new = [93] #Kariyer boyu pas isabeti yüzdesi
y_predicto = model.predict(x_new_scaled)
print("predicto: ", y_predicto)
