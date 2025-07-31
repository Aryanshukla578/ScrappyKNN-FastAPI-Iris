# 🌸 ScrappyKNN Iris Predictor API

A simple implementation of the K-Nearest Neighbors (KNN) algorithm from scratch (ScrappyKNN) trained on the Iris dataset and deployed using FastAPI with an interactive Swagger UI.

---

## 🚀 Features

- Custom KNN (no scikit-learn classifier used)
- FastAPI-based API for prediction
- Swagger UI for easy testing
- JSON input/output interface
- Predicts Setosa, Versicolor, or Virginica

---

## 📊 Dataset

- **Dataset Used:** `sklearn.datasets.load_iris()`
- **Features:** sepal length, sepal width, petal length, petal width
- **Labels:** 0 = Setosa, 1 = Versicolor, 2 = Virginica

---

## 🧠 Model

The `ScrappyKNN` class implements:
- Euclidean distance manually
- A basic `fit()` method
- Custom `predict()` logic using the closest point from the training set

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/ScrappyKNN-FastAPI.git
cd ScrappyKNN-FastAPI
```
### 2.Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4.Run the API server
uvicorn main:app --reload

### 5. Visit API docs
Open your browser and go to:
Link:http://127.0.0.1:8000/docs
---
🧪 Sample JSON Input
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
---
✅ Sample Output
{
  "prediction": "setosa"
}
---
📁 Project Structure
ScrappyKNN-FastAPI/
├── ml.py                 # KNN model logic
├── main.py               # FastAPI app
├── requirements.txt      # Python dependencies
├── README.md             # You're reading it now
└── example_request.json  # Sample test input
---
## 📸 Screenshots

### 🔹 Homepage Response
![Homepage](./screenshots/img1.png)

### 🔹 Swagger UI - Input Format
![Swagger Input](./screenshots/img2.png)

### 🔹 Prediction Output - versicolor
![versicolor](./screenshots/img3.png)

### 🔹 Second Input Trial
![Second Trial](./screenshots/img4.png)

### 🔹 Final Result with Prediction
![Final Result](./screenshots/img5.png)
---
👨‍💻 Author
Aryan Shukla
📧 Email: as3061693@gmail.com
---
🔗 GitHub: https://github.com/Aryanshukla578
---
💬 License
This project is for learning/demo purposes only. You may freely use and modify it.
---
