
# Employee Salary Prediction

This project predicts employee salary based on experience and education level using a machine learning model built in Python. It provides a simple web interface to input data and see the predicted result.

---

## 👩‍💻 Developed by:
**J. Pavithra**

---

## 🚀 Technologies Used

| Layer            | Technology       | Description                                   |
|------------------|------------------|-----------------------------------------------|
| Machine Learning | Python, scikit-learn | Trains a Linear Regression model to predict salary |
| Backend          | Python, Flask     | Connects model to the web app                 |
| Frontend         | HTML, CSS         | Provides input form and displays output       |

---

## 🧠 How It Works

1. **Model Training** (`train_model.py`)
   - Trains a Linear Regression model on sample data
   - Saves model as `model.pkl`

2. **Prediction** (`predict_salary.py`)
   - Loads `model.pkl`
   - Takes input: experience, education level
   - Returns predicted salary

3. **Web Interface** (`index.html`)
   - User enters values in a form
   - Form is submitted to Flask (`app.py`)
   - Flask uses the model to predict salary
   - Result is shown on the same page

---

## 🔗 File & Folder Descriptions

| File / Folder           | Description |
|--------------------------|-------------|
| `app.py`                | Flask app that connects frontend and model |
| `model.pkl`             | Saved ML model used for prediction |
| `salary_prediction/`    | Contains training and prediction Python scripts |
| `templates/index.html`  | User interface for entering inputs and showing output |
| `README.md`             | Project documentation (this file) |
| `static/` (optional)    | For future CSS or JS files if needed |

---

## 🖼 Simple Architecture Diagram

```
User Input (HTML form)
        ↓
   Flask Backend (app.py)
        ↓
 ML Model (model.pkl via predict_salary.py)
        ↓
   Predicted Salary (HTML Output)
```

---

## 🧪 Example Input
- Experience: `5`
- Education Level: `3`

**→ Output: ₹72,000 (example)**

---

## 📦 How to Run

1. Train the model (optional if model.pkl already exists):
   ```bash
   python train_model.py
   ```

2. Start the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://localhost:5000
   ```

---

## 📄 License

This project is licensed under the MIT License.  
(C) 2025 J. Pavithra

---

Feel free to use, modify, or extend this project with credit.
