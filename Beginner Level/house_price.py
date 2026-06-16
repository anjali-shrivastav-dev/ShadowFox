import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =============================
# Step 1: Load the dataset
# =============================
df = pd.read_csv("boston.csv")


df = df.dropna()
print("Shape after dropping missing values:", df.shape)

# =============================
# Step 2: Explore dataset
# =============================
print(df.head())       # First 5 rows
print(df.info())       # Data info
print("Shape:", df.shape)

# =============================
# Step 3: Features (X) and Target (y)
# =============================
X = df.drop("MEDV", axis=1)   # Features
y = df["MEDV"]                # Target

print("Feature matrix (X) shape:", X.shape)
print("Target vector (y) shape:", y.shape)

# =============================
# Step 4: Train-Test Split
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# =============================
# Step 5: Train Linear Regression
# =============================
model = LinearRegression()
model.fit(X_train, y_train)
print("Model training completed!")

# =============================
# Step 6: Model Evaluation
# =============================
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# =============================
# Step 7: Visualization
# =============================
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.xlabel("Actual Prices (MEDV)")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Boston House Prices")
plt.show()
