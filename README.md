
# Employee Salary Predictor

This project predicts the estimated salary of an employee based on two inputs:
- Years of Experience
- Education Level (High School, Bachelors, Masters, PhD)

## 👩‍💻 Created by
**J. Pavithra**

## 📂 Project Structure

Here’s a quick overview of what each file does:

- `index.html`: A simple interactive web page (runs without Python) where users can input experience and education level to see an estimated salary instantly.
- `main.py`: This is where the model would normally be trained using data. (In this version, we simulate it.)
- `app.py`: A Streamlit app (Python-based) that could be used to host a dynamic web interface. If you're using Python, you can run this using `streamlit run app.py`.
- `employee_data.csv`: Sample dataset containing historical data of salaries based on experience and education level.
- `model.pkl`: Simulated output of a trained model saved using Python's `pickle` module. If real training was done, this would store a `LinearRegression` or similar model.
- `salary_prediction.ipynb`: Placeholder for the Jupyter Notebook where data analysis and model training could be performed.
- `requirements.txt`: List of Python libraries required (like `streamlit`, `scikit-learn`, `pandas`).
- `README.md`: This documentation file.

## ⚙️ How It Works

1. The user enters years of experience and selects education level.
2. A simple formula estimates the salary:
   - `Base Salary + (Experience × Coefficient) + (Education Level × Bonus)`
   - This is implemented directly in `index.html` using JavaScript.
3. If using Python (`app.py`), the model can be loaded from `model.pkl` and predictions served dynamically.

## 🚀 How to Run (Python Web App)

If you want to run this project with Python:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Note

This is a **demonstration project** meant to show how a basic ML pipeline and web deployment might work. Real models would require training and saving the model to `model.pkl`.

