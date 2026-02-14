# Bitcoin Price Predictor

This is a beginner-level machine learning project that predicts Bitcoin closing prices using a Decision Tree Regressor.

The goal of this project is to practice key machine learning concepts, including:

- Data preprocessing
- Time-based train-test splitting
- Log transformation of the target variable
- Model training using scikit-learn
- Model evaluation using Mean Absolute Error (MAE)

---

## Project Description

The model is trained on historical Bitcoin price data.

The main steps in this project include:

1. Loading and cleaning the dataset
2. Converting volume values to numeric format and removing missing values
3. Splitting the data into training and testing sets (80/20 split)
4. Applying log transformation to the target variable
5. Training a Decision Tree Regressor
6. Evaluating model performance using MAE
7. Predicting the closing price based on user input

This project was developed as part of my learning process in machine learning.

## Model Information

Algorithm: DecisionTreeRegressor  
Max Depth: 8  
Min Samples Leaf: 5  
Train/Test Split: 80% training / 20% testing  
Evaluation Metric: Mean Absolute Error (MAE)

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn

---

## Project Structure

```
bitcoin-price-predictor/
│
├── PREDICT.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── data/   (dataset not included)
```

---

## Dataset

The dataset is not included in this repository because the file size exceeds GitHub limits.

To run this project:

1. Download the Bitcoin historical dataset.
2. Place the file inside the `data/` folder.
3. Rename it to:

btcusd_1-min_data.csv

---

## How to Run

Clone the repository:

```
git clone https://github.com/prashantJha-git/bitcoin-price-predictor.git
cd bitcoin-price-predictor
```

Install required libraries:

```
pip install -r requirements.txt
```

Run the script:

```
python PREDICT.py
```

Enter the following values when prompted:
- Open value
- High value
- Low value
- Volume value

The model will print the predicted closing price and the Mean Absolute Error.

---

## License

This project is licensed under the MIT License.
