## SALES DATA GENERATOR: SYNTHETIC E-COMMERCE TRANSACTIONS

A Python-based project that generates synthetic Indonesian e-commerce sales data with realistic variations, anomalies, duplicates, and inconsistencies. The dataset can be used for practicing **data cleaning, preprocessing, and analytics** workflows.

---

### 📊 Project Overview
- **Dataset Size**: 300 synthetic transactions (+5% duplicates)  
- **Features**: Order ID, Date, Customer Name, Product Category, Brand, Product, Quantity, Unit Price, City, Payment Method  
- **Data Variations**: Inconsistent formatting, anomalies (negative prices/quantities, missing values), mixed date formats, and duplicates.  
- **Use Cases**: Data wrangling, anomaly detection, preprocessing, reporting, and visualization practice.  

---

### ⚙️ Data Generation Logic
1. **Customer Names** → Generated with different formats (case sensitivity, extra spaces, commas, etc.).  
2. **Categories & Brands** → Electronics & Fashion with multiple variations in spelling.  
3. **Products** → Items with inconsistent casing and spacing.  
4. **Quantities** → Normal (1–5), high (6–10), anomalies (0, negative).  
5. **Prices** → Ranges based on product type, anomalies (0, negative).  
6. **Dates** → Random across 2023 with mixed formats (`YYYY-MM-DD` & `DD/MM/YYYY`).  
7. **Duplicates** → ~5% of rows duplicated with slight modifications.  

---

### 📦 Requirements
- Python >=3.8 (tested on 3.13.7)  
- Pandas library >=2.0 (tested on 2.3.2)  
- (Optional) Jupyter Notebook or Google Colab (for interactive use)

---

### 📂 Output
- File: `sales_data_raw.csv`  
- Rows: 300 (285 unique + 15 duplicates)  
- Columns: Order_ID, Order_Date, Customer_Name, Product_Category, Merk, Product_Name, Quantity, Unit_Price, City, Payment_Method  

---

### 📝 Note about Synthetic Data
- This dataset is synthetic and intentionally includes duplicates, anomalies, and inconsistent formatting to simulate real-world scenarios.  
- It is designed only for practice and learning purposes (data cleaning, preprocessing, and analytics).  
- It should not be used as a source of actual business intelligence.  

---

### 📧 Contact
- **Author**: Abu Sofian  
- **Email**: [abusofian.id@gmail.com](mailto:abusofian.id@gmail.com)  
- **LinkedIn**: [linkedin.com/in/abusofianid](https://www.linkedin.com/in/abusofianid)  
