# Data Dictionary & Insights

## Project: Retail Sales Analytics

---

## 1. Overview

This document describes the dataset used for the Retail Sales Analytics project. It defines each column and explains how the data is used for analysis.

---

## 2. Data Dictionary

| Column Name  | Description                                                    | Data Type   |
| ------------ | -------------------------------------------------------------- | ----------- |
| Ship Mode    | Delivery method used for shipping (e.g., Standard Class)       | Categorical |
| Segment      | Type of customer (Consumer, Corporate, Home Office)            | Categorical |
| Country      | Country where the order was placed                             | Categorical |
| City         | City of the customer                                           | Categorical |
| State        | State of the customer                                          | Categorical |
| Postal Code  | Postal/ZIP code of the customer                                | Numeric     |
| Region       | Region of the country (West, East, Central, South)             | Categorical |
| Category     | Main product category (Furniture, Technology, Office Supplies) | Categorical |
| Sub-Category | Specific product type (e.g., Chairs, Phones)                   | Categorical |
| Sales        | Revenue generated per order line                               | Numeric     |
| Quantity     | Number of items sold                                           | Numeric     |
| Discount     | Discount applied to the product (0–1 range)                    | Numeric     |
| Profit       | Profit earned after discount                                   | Numeric     |

---

## 3. Data Types Summary

- **Categorical Columns:** Ship Mode, Segment, Country, City, State, Region, Category, Sub-Category
- **Numeric Columns:** Sales, Quantity, Discount, Profit, Postal Code

---

## 4. Data Quality Summary

After data cleaning:

- No missing values found
- Duplicate records removed
- Data types validated and standardized
- Dataset is consistent and ready for analysis

---

## 5. Key Insights from Analysis

Based on SQL analysis:

- **Total Revenue:** 2,296,195.59
- **Average Order Value:** 230.15

### Category Performance

- Technology is the highest revenue-generating category (~836K)
- Followed by Furniture (~741K) and Office Supplies (~718K)

### City Performance

- New York City is the top-performing city (~256K)
- Other major contributors: Los Angeles, Seattle, San Francisco

---

## 6. Conclusion

The dataset is clean and structured for analysis. Key insights highlight that revenue is driven by the Technology category and concentrated in major cities, which can guide business decisions and dashboard development.
