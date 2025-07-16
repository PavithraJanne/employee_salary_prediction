
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample data
data = pd.DataFrame({
    'Experience': [1, 2, 3, 4, 5],
    'Education': [1, 2, 2, 3, 3],  # 1: High School, 2: Bachelors, 3: Masters, 4:PhD
    'Salary': [30000, 40000, 50000, 60000, 70000]
})

X = data[['Experience', 'Education']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
