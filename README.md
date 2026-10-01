# E-Commerce Sales & Customer Experience Analysis

An end-to-end data analytics project analyzing e-commerce sales, customer behavior, payment preferences, discounts, delivery performance, and customer satisfaction using **Python, SQL, and Power BI**.

## 📌 Project Overview

The objective of this project is to transform raw e-commerce transaction data into actionable business insights.

The analysis focuses on understanding revenue performance, product categories, regional performance, customer contribution, discount patterns, delivery experience, and payment preferences.

## 🎯 Business Objectives

The analysis answers seven key business questions:

1. How does revenue change over time?
2. Which product categories generate the most revenue and sales volume?
3. Which regions perform best and worst?
4. How are discounts associated with revenue and quantity sold?
5. Which customers contribute the most revenue?
6. Is delivery time associated with customer ratings?
7. Which payment methods are most popular, and does preference vary by region?

## 🛠️ Tools & Technologies

- **Python** – Data cleaning, exploration, analysis, and visualization
- **Pandas** – Data manipulation and analysis
- **Matplotlib & Seaborn** – Data visualization
- **MySQL** – SQL-based business analysis
- **Power BI** – Interactive dashboard and data visualization
- **GitHub** – Project documentation and version control

## 📊 Dataset

The dataset contains **5,000 e-commerce orders** with 12 attributes:

- Order ID
- Order Date
- Customer ID
- Product Category
- Region
- Quantity
- Unit Price
- Discount
- Payment Method
- Delivery Days
- Customer Rating
- Revenue

The dataset covers transactions from **2022 to 2035**, with 2035 containing partial-year data.

## 🔎 Analysis Workflow

### 1. Python Analysis

Python was used to:

- Understand the dataset structure
- Check for missing values and duplicates
- Convert and process date fields
- Calculate business KPIs
- Analyze revenue trends
- Compare product categories and regions
- Analyze discounts and average order value
- Identify high-value customers
- Analyze delivery time and customer ratings
- Analyze payment method usage
- Create supporting visualizations

### 2. SQL Analysis

MySQL was used to perform business-focused analysis including:

- Overall business KPIs
- Revenue trends and year-over-year growth
- Product category performance
- Regional performance
- Discount analysis
- Customer revenue contribution
- Customer segmentation
- Product × region analysis
- Monthly and seasonal performance
- Repeat customer analysis
- Customer revenue ranking using window functions

### 3. Power BI Dashboard

The final Power BI dashboard combines the analysis into an interactive business report.

It includes:

- KPI cards
- Revenue by product category
- Revenue by region
- Revenue by payment method
- Annual revenue trend
- Quantity sold by product category
- Average order value by discount level
- Top 10 customers by revenue
- Customer rating vs delivery time
- Region, product category, and payment method slicers

## 📈 Key Findings

### Revenue Performance

Total revenue was approximately **₹5.11M** across 5,000 orders.

Revenue remained relatively stable but fluctuated year over year. Among complete years, revenue reached its highest level in **2033 at approximately ₹408.7K**.

### Product Categories

**Electronics** generated the highest revenue at approximately **₹1.83M** and also recorded the highest sales volume with **7,109 units sold**.

### Regional Performance

The **West region** generated the highest revenue at approximately **₹1.35M**, while the **East region** generated approximately **₹1.24M**.

### Discounts

Higher discount levels were generally associated with lower average order values in the dataset.

This represents an observed association and does not establish a causal relationship.

### Customer Contribution

Customer **1663** generated the highest individual customer revenue at approximately **₹17.68K**.

Customer segmentation and repeat-customer analysis were also used to understand differences in customer value.

### Delivery & Customer Satisfaction

The relationship between delivery time and customer rating was very weak, with a correlation of approximately **-0.018**.

Customer ratings remained relatively stable across different delivery durations.

### Payment Methods

**Card payments** were the most frequently used payment method, followed by **Cash on Delivery (COD)** and **Wallet**.

Card payments were the most popular payment method across all four regions.

## 📂 Project Structure

```text
E-Commerce-Sales-Customer-Experience-Analysis/
│
├── Charts/
│   ├── delivery_vs_rating.png
│   ├── discount_vs_aov.png
│   ├── payment_method_usage.png
│   ├── revenue_by_category.png
│   ├── revenue_by_region.png
│   ├── revenue_trend_by_year.png
│   └── top_10_customers.png
│
├── Data/
│   └── ecommerce_sales_analytics_5000.csv
│
├── Power BI/
│   └── E-Commerce_Sales_Customer_Experience.pbix
│
├── Python/
│   └── ecommerce_analysis.py
│
├── SQL/
│   └── ecommerce_analysis.sql
│
├── .gitignore
└── README.md
