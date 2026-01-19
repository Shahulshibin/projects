📊 Week 5 – Customer Sales Analysis (Advanced Pandas)
📌 Project Overview

This project focuses on advanced data manipulation and analysis using Pandas.
The goal is to analyze customer purchasing behavior, identify sales trends, discover top-performing customers and products, and generate meaningful business insights using real-world sales data.

The project demonstrates practical use of:

Data aggregation and grouping

Data cleaning and transformation

Merging multiple datasets

Pivot tables for summarization

Professional data visualizations

🎯 Objectives

Analyze customer sales performance

Identify top customers and best-selling products

Understand regional and seasonal sales trends

Create business-ready insights and recommendations

Apply advanced Pandas techniques in a real-world scenario

🛠️ Tools & Technologies Used

Python

Pandas – Data manipulation and analysis

Matplotlib – Data visualization

Seaborn – Enhanced visual styling

Jupyter Notebook

📂 Project Structure
Week-5-Customer-Sales-Analysis/
│
├── customer_analysis.ipynb      # Main analysis notebook
├── sales_data.csv               # Sales dataset
├── customer_data.csv            # Customer dataset
├── analysis_report.pdf          # Final business report
├── requirements.txt             # Required Python libraries
└── README.md                    # Project documentation

📊 Dataset Description
🔹 Sales Dataset (sales_data.csv)

Date – Transaction date

Product – Product name

Quantity – Units sold

Price – Price per unit

Customer_ID – Unique customer identifier

Region – Sales region

Total_Sales – Total transaction value

🔹 Customer Dataset (customer_data.csv)

CustomerID – Unique customer ID

Tenure – Customer relationship duration

MonthlyCharges – Monthly spending

TotalCharges – Total lifetime charges

Contract – Contract type

PaymentMethod – Payment method used

PaperlessBilling – Billing preference

SeniorCitizen – Senior citizen indicator

Churn – Customer churn status

🧪 Key Analysis Performed
✔ Data Cleaning & Preparation

Handled missing values

Converted date columns to datetime format

Extracted year, month, and day from date fields

✔ Data Aggregation & Grouping

Monthly sales totals

Customer lifetime value

Product-wise and region-wise sales analysis

✔ Advanced Operations

Multi-condition filtering (AND / OR)

String operations on text columns

Merging sales and customer datasets

Pivot tables for data summarization

✔ Visualizations

Monthly sales trend (Line Chart)

Sales by region (Bar Chart)

Top-selling products (Bar Chart)

Customer performance analysis

📈 Sample Business Insights

High-value customers contribute a significant portion of revenue

Certain products consistently outperform others

Sales show clear seasonal trends

Specific regions generate higher revenue than others

💡 Business Recommendations

Focus on retaining top customers through loyalty programs

Increase inventory for high-demand products

Target high-performing regions with marketing campaigns

Introduce bundled offers to improve cross-selling

▶️ How to Run the Project

Clone the repository

git clone https://github.com/your-username/Week-5-Customer-Sales-Analysis.git


Navigate to the project directory

cd Week-5-Customer-Sales-Analysis


Install dependencies

pip install -r requirements.txt


Open Jupyter Notebook

jupyter notebook


Run customer_analysis.ipynb

🧾 Testing & Validation

Verified aggregation results using manual checks

Ensured correct merging of datasets using customer IDs

Validated visual outputs against numerical summaries

📌 Learning Outcomes

Mastered advanced Pandas data manipulation techniques

Learned to analyze real business data

Improved data storytelling through visualizations

Gained experience in creating professional project documentation