# Customer Churn Prediction  
## Data Preprocessing & Feature Engineering (Week 10 Capstone Project)

---

## 📌 Project Overview

Customer churn refers to customers who stop using a company’s product or service.  
This project focuses on building a **complete data preprocessing and feature engineering pipeline** to prepare customer data for churn prediction using machine learning.

The project demonstrates industry-standard practices including data cleaning, categorical encoding, feature scaling, feature engineering, pipeline construction, and model evaluation.

---

## 🎯 Objectives

- Understand and explore customer churn data
- Clean and preprocess raw datasets
- Handle categorical and numerical features correctly
- Engineer meaningful features using business logic
- Build an end-to-end machine learning pipeline
- Evaluate model performance using standard metrics

---

## 📊 Dataset Information

- **Dataset Name:** `customer_churn.csv`
- **Records:** ~500 customers
- **Target Variable:** `Churn`

### Features Used
- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen
- Churn (Target)

---

## 🛠️ Technologies & Tools Used

- **Programming Language:** Python
- **Libraries:**
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - SciPy
  - Jupyter Notebook
- **IDE:** Visual Studio Code / Jupyter Notebook

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python
- Recommended Version: **Python 3.9 – 3.11**
- Download from: https://www.python.org/downloads/

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv churn_env

Activate environment:

Windows: churn_env\Scripts\activate

Mac/Linux: source churn_env/bin/activate

3️⃣ Install Required Libraries
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter

4️⃣ Run the Project
jupyter notebook


Open:

churn_prediction_pipeline.ipynb

📁 Project Structure
Customer-Churn-Pipeline/
│
├── churn_prediction_pipeline.ipynb
├── customer_churn.csv
├── preprocessing_report.md
├── feature_engineering_documentation.md
├── README.md
├── requirements.txt

Preprocessing Workflow

Dataset loading and exploration

Removal of irrelevant columns (CustomerID)

Handling missing values in TotalCharges

Encoding categorical variables:

Label Encoding

One-Hot Encoding

Binary Encoding

Feature scaling:

Standardization

Normalization

Outlier detection using IQR

Feature engineering

Train-test split

Pipeline creation

Model training and evaluation

🧠 Feature Engineering Highlights

Customer Lifetime Value (CLV)

Long Tenure Indicator

High Spender Indicator

Average Monthly Cost

Engagement Score

These features enhance customer behavior understanding and improve churn prediction.

🤖 Machine Learning Model

Algorithm Used: Random Forest Classifier

Why Random Forest?

Handles non-linear relationships

Robust to noise and overfitting

Performs well with engineered features

📈 Model Evaluation

Evaluation metrics used:

Accuracy

Precision

Recall

F1-score

The pipeline was tested end-to-end to ensure error-free execution and consistent predictions.

🧪 Testing & Validation

Stratified train-test split to preserve churn ratio

End-to-end pipeline testing using unseen data

Validation through classification report and accuracy score

📸 Visual Documentation

The notebook includes:

Churn distribution plot

Feature importance analysis

Model evaluation outputs

Screenshots can be included for submission as proof of execution.

✅ Quality Checklist

✔ Clean preprocessing pipeline
✔ Multiple encoding techniques
✔ Multiple scaling methods
✔ Feature engineering (5+ features)
✔ Pipeline-based ML approach
✔ Evaluation metrics included
✔ Well-documented structure

🧾 Conclusion

This project successfully demonstrates a complete data preprocessing and feature engineering workflow for customer churn prediction.
The structured pipeline ensures reproducibility, scalability, and real-world applicability.

👨‍🎓 Author

Name: Shahul shibin TP
Project Type: Internship / Academic Capstone
Topic: Data Preprocessing & Feature Engineering