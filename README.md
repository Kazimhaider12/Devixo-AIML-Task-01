# Devixo Solutions - AI/ML Internship Program
## Task 01: Python Programming, Data Analysis & Visualization

### 📌 Project Overview
This project delivers a complete end-to-end data analysis pipeline on an Employee Workforce & Salary dataset (750+ records). It demonstrates data extraction, cleaning and preprocessing, rigorous exploratory data analysis (EDA), statistical computations, ten diverse visualizations, actionable business findings, and an interactive Streamlit dashboard.

---

### 📂 Project Structure
```
Task_01_AI_ML/
├── dataset/
│   ├── employee_data.csv          # Raw Dataset (>750 records with intentional anomalies)
│   └── cleaned_employee_data.csv  # Cleaned, validated dataset
├── notebook/
│   └── Task_01_Data_Analysis.ipynb # Full Jupyter Notebook with code, EDA & statistics
├── images/                        # All 10 high-resolution charts
│   ├── 01_histogram_salary.png
│   ├── 02_bar_dept_salary.png
│   ├── 03_pie_education.png
│   ├── 04_scatter_exp_salary.png
│   ├── 05_line_age_salary.png
│   ├── 06_box_dept_salary.png
│   ├── 07_heatmap_correlation.png
│   ├── 08_countplot_remote.png
│   ├── 09_pairplot.png
│   └── 10_violin_performance.png
├── report/
│   └── Task_01_Report.pdf         # Complete 20-section formal technical PDF documentation
├── app/
│   └── app.py                     # Streamlit interactive dashboard
├── requirements.txt
└── README.md
```

---

### ⚙️ Technologies & Libraries Used
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Interactive UI:** `streamlit`

---

### 🔍 Key Findings & 10 Core Insights
1. **Strong Experience-Salary Coupling:** Correlation between `Years_Experience` and `Monthly_Salary` is extremely high ($r \approx 0.95$), indicating strong tenure-based compensation.
2. **Data Science Premium:** Data Science command the highest departmental median salary ($123,000+), while Support/HR have lower median compensation.
3. **Education Dividend:** Employees holding PhD and Master's degrees earn statistically significant salary premiums compared to Bachelor's and High School credentials across identical tenure brackets.
4. **Normal Performance Distribution:** Performance ratings form a near-normal curve centered around 3.5/5.0 across all departments without strong systemic departmental bias.
5. **Remote Work Distribution:** IT and Data Science exhibit the highest percentage of remote personnel (~48%), whereas Operations is predominantly on-site.
6. **Low Overtime Correlation:** Overtime hours do not directly drive higher compensation or performance evaluations ($r \approx 0.05$), signaling that performance is evaluated by outcome rather than raw hours.
7. **Age-Salary Linearity:** Salary shows steady upward progression from age 22 to 59, reflecting continuous annual increments.
8. **Outlier Detection:** Box plot analysis confirmed that salary outliers are concentrated in senior leadership roles within Sales and IT.
9. **Gender Diversity:** Departmental gender distributions are well balanced, with female participation exceeding 44% overall.
10. **Data Hygiene Impact:** Proper median imputation preserving department clusters prevented distorting true organizational pay bands.

---

### 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Task_01_AI_ML.git
   cd Task_01_AI_ML
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:
   ```bash
   jupyter notebook notebook/Task_01_Data_Analysis.ipynb
   ```
4. Run Streamlit Dashboard (Bonus):
   ```bash
   streamlit run app/app.py
   ```
