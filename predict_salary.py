
import pickle

def predict_salary(experience, education):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    salary = model.predict([[experience, education]])
    return salary[0]

# Example usage
if __name__ == '__main__':
    exp = 3
    edu = 2
    result = predict_salary(exp, edu)
    print(f"Predicted Salary for {exp} years experience and education level {edu} is ₹{int(result)}")
