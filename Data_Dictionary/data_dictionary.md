# Data Dictionary & Initial Insights

## Project: Retail Sales Analytics

---

#  1. Overview

This document explains the dataset used in the project. It helps us understand what each column means and how we can use the data for analysis.

---

#  2. Data Dictionary

| Column Name  | Description                                                    | Data Type   |
| ------------ | -------------------------------------------------------------- | ----------- |
| Ship Mode    | Delivery method used (Standard Class, First Class, etc.)       | Categorical |
| Segment      | Type of customer (Consumer, Corporate, Home Office)            | Categorical |
| Country      | Country of the order                                           | Categorical |
| City         | City of the customer                                           | Categorical |
| State        | State of the customer                                          | Categorical |
| Category     | Main product category (Furniture, Office Supplies, Technology) | Categorical |
| Sub-Category | Type of product (Chairs, Phones, etc.)                         | Categorical |
| Sales        | Total sales amount for the order                               | Numeric     |
| Quantity     | Number of items sold                                           | Numeric     |
| Discount     | Discount given on the product                                  | Numeric     |
| Profit       | Profit earned from the order                                   | Numeric     |

---

#  3. Data Types

* **Categorical Columns:** Ship Mode, Segment, Country, City, State, Category, Sub-Category
* **Numeric Columns:** Sales, Quantity, Discount, Profit

---

#  4. Data Issues (Possible)

While working with the dataset, we may face:

* Missing values in some columns
* Duplicate rows
* Different formats in data
* Unusual values (like very high discount or negative profit)

###  What we can do:

* Remove or fix missing values
* Remove duplicates
* Standardize formats
* Check data correctness

---

#  5. Initial Business Insights

##  1. Category Performance

We can find which category (Furniture, Technology, etc.) gives the most sales and profit.
-->  Helps in focusing on best products.

---

##  2. Sales by Location

We can compare sales across cities and states.
--> Helps identify strong and weak regions.

---

##  3. Discount vs Profit

High discount may reduce profit.
--> Helps in better pricing decisions.

---

##  4. Customer Segments

Different customer types contribute differently to sales.
--> Helps target the right customers.

---

##  5. Product Demand

Quantity shows which products are in high demand.
--> Helps in stock planning.

---

#  6. Conclusion

This data dictionary helps us understand the dataset clearly and prepares us for further analysis, SQL queries, and dashboard creation.

---
