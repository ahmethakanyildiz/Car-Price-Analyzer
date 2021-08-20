import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df=pd.read_excel("data.xlsx", engine='openpyxl')

df=df.drop("model",axis=1)
df=df.drop("Unnamed: 0",axis=1)
df=df.drop("Column1",axis=1)
df=df[df.year!=1970]

y=df["price"].values
x=df.drop("price",axis=1).values

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.33,random_state=10)
scaler = MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model = Sequential()

model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(16,activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")

print("Train is started!")
model.fit(x=x_train, y=y_train,validation_data=(x_test, y_test),batch_size=300,epochs=300)
print("Train is finished!")

#lossValue = pd.DataFrame(model.history.history)
#lossValue.plot()
#plt.show()

guessArray = model.predict(x_test)
print("Mean Absolute Error: "+str(mean_absolute_error(y_test,guessArray)))

#plt.scatter(y_test,guessArray)
#plt.plot(y_test,y_test,"g-*")
#plt.show()

model.save("car_price_analyzer_model.h5")

