import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from pathlib import Path

# PATH SETUP

BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "btcusd_1-min_data.csv"

if not data_path.exists():
    raise FileNotFoundError(f"Data CSV not found AT: {data_path}")

# DATA LOADING AND PREPROCESSING

data = pd.read_csv(data_path)
data["Volume"] = (
    data["Volume"]
    .replace("-", np.nan)
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)

data = data.dropna()

# TRAIN / TEST SPLIT (TIME-BASED)

split_index = int(len(data) * 0.8)

trainData = data.iloc[:split_index]
testData = data.iloc[split_index:]

# USER INPUT

O = float(input("Enter The Open Value: "))
H = float(input("Enter The High Value: "))
L = float(input("Enter The Low Value: "))
V = float(input("Enter The Volume Value: "))

p = pd.DataFrame([{
    "Open": O,
    "High": H,
    "Low": L,
    "Volume": V
}])

# TRAINING MODEL

features = ["Open", "High", "Low", "Volume"]

X = trainData[features]
y = np.log(trainData["Close"])

model = DecisionTreeRegressor(
    random_state=1,
    max_depth=8,
    min_samples_leaf=5
)

model.fit(X, y)

# TESTING MODEL

X_test = testData[features]
y_test_actual = testData["Close"]

test_predictions = np.exp(model.predict(X_test))
mae = mean_absolute_error(y_test_actual, test_predictions)

# USING MODEL FOR PREDICTION

prediction = np.exp(model.predict(p))

print("\nFor Given Data:")
print(p)
print("\nPredicted Close Value =", round(prediction[0], 2))

print("Mean Absolute Error on Test Data =", round(mae, 2))
