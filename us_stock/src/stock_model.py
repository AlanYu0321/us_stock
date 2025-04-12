from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))  # 預測下1天的收盤價
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

model = build_lstm_model()
model.fit(X_train, y_train, epochs=10, batch_size=32)
