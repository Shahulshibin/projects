# Preprocessing Report  
## Customer Churn Prediction Project

---

## 1. Introduction

This document describes the complete data preprocessing pipeline used in the **Customer Churn Prediction** project.  
The purpose of preprocessing is to transform raw customer data into a clean, numerical, and machine-learning-ready format while preserving meaningful business information.

Proper preprocessing ensures:
- Higher model accuracy
- Reduced errors during training
- Reproducibility and scalability of the pipeline

---

## 2. Dataset Overview

- **Dataset Name:** customer_churn.csv  
- **Total Records:** ~500  
- **Target Variable:** Churn  

### Original Columns:
- CustomerID
- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen
- Churn

---

## 3. Data Cleaning Steps

### 3.1 Removal of Irrelevant Features

**CustomerID** was removed from the dataset because:
- It is a unique identifier
- It does not contribute to churn prediction
- It causes errors when passed to machine learning algorithms

This step prevents unnecessary noise in the model.

---

### 3.2 Handling Data Type Issues

The **TotalCharges** column was initially read as a string due to formatting inconsistencies.

**Action Taken:**
- Converted TotalCharges to numeric
- Invalid values were coerced to NaN
- Missing values were filled using the median

**Rationale:**  
Median imputation is robust to outliers and maintains numerical stability.

---

## 4. Target Variable Processing

### 4.1 Cleaning Target Values

The `Churn` column contained categorical values (`Yes` / `No`) with potential formatting issues.

**Action Taken:**
- Trimmed whitespace
- Converted values to binary representation

| Original Value | Encoded Value |
|---------------|--------------|
| Yes | 1 |
| No | 0 |

This ensures compatibility with classification algorithms.

---

## 5. Handling Categorical Variables

Three different encoding techniques were applied as required:

### 5.1 Label Encoding
- Applied to: `Contract`
- Reason: Contract types have a logical order

### 5.2 One-Hot Encoding
- Applied to: `PaymentMethod`
- Reason: Nominal variable with no inherent order

### 5.3 Binary Encoding
- Applied to: `PaperlessBilling`
- Reason: Binary Yes/No attribute

All categorical features were successfully converted into numerical format.

---

## 6. Feature Scaling

Two scaling techniques were used:

### 6.1 Standardization
- Applied using `StandardScaler`
- Centers data around mean with unit variance

### 6.2 Normalization
- Applied using `MinMaxScaler`
- Scales values between 0 and 1

**Rationale:**  
Scaling ensures that features contribute equally to the model and prevents dominance of large-magnitude values.

---

## 7. Outlier Detection and Handling

The **Interquartile Range (IQR)** method was used to detect outliers in `MonthlyCharges`.

**Steps:**
- Calculated Q1 and Q3
- Removed values outside 1.5 × IQR

**Rationale:**  
Outliers can negatively affect model performance and distort feature distributions.

---

## 8. Feature Engineering Summary

The following new features were created to enhance predictive power:

- Customer Lifetime Value (CLV)
- Long_Tenure indicator
- High_Spender indicator
- Average Monthly Cost
- Engagement Score

These features capture customer behavior more effectively than raw attributes.

---

## 9. Final Dataset Validation

After preprocessing:
- All features were numerical or boolean
- No missing values in the target variable
- Dataset was ready for machine learning

A final verification was performed using:
- Data type inspection
- Missing value checks
- Sample predictions through the pipeline

---

## 10. Conclusion

This preprocessing pipeline transformed raw customer data into a clean, structured, and model-ready dataset.  
Each step was carefully designed to improve data quality, reduce noise, and enhance predictive accuracy.

The preprocessing approach follows industry-standard machine learning practices and ensures reliable model performance.

---

**End of Preprocessing Report**
