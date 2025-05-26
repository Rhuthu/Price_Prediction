# Price_Prediction

An end-to-end machine learning web application to estimate the price of homes in Bangalore based on location, size, BHK, and bathrooms.

This project integrates a trained ML model with a Flask backend and a frontend built using HTML, CSS, and JavaScript.

## Features

- Predict house prices in Bangalore using real estate data.
- Trained regression model using cleaned and preprocessed data.
- Interactive web UI for user input and instant prediction.
- Deployed using Flask as the backend framework.

---

##  Tech Stack

**Frontend:**
- HTML5
- CSS3
- JavaScript (jQuery)

**Backend:**
- Python
- Flask

**Machine Learning:**
- pandas, numpy
- scikit-learn
- matplotlib (for EDA)

---
## How the Model Works

1. Data cleaning and feature engineering (removing outliers, encoding locations).
2. Trained a linear regression model using scikit-learn.
3. Saved the model using `pickle`.
4. Exposed a prediction API via Flask that the frontend can call.

---

##  Installation and Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Rhuthu/Price_Prediction.git
cd Price_Prediction

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

cd server
python server.py
```
---
Dataset Source: Kaggle - Bangalore Home Prices


