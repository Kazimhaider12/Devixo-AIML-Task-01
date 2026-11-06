import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Workforce & Salary EDA Dashboard", layout="wide")

st.title("💼 Devixo Solutions - Task 01: Employee Workforce Analytics")
st.markdown("Interactive EDA & Statistical Insights Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/cleaned_employee_data.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
departments = st.sidebar.multiselect("Select Department", options=df['Department'].unique(), default=df['Department'].unique())
education = st.sidebar.multiselect("Select Education Level", options=df['Education_Level'].unique(), default=df['Education_Level'].unique())

filtered_df = df[(df['Department'].isin(departments)) & (df['Education_Level'].isin(education))]

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Headcount", len(filtered_df))
col2.metric("Average Salary", f"${filtered_df['Monthly_Salary'].mean():,.2f}")
col3.metric("Median Experience", f"{filtered_df['Years_Experience'].median():.1f} Yrs")
col4.metric("Avg Performance", f"{filtered_df['Performance_Score'].mean():.2f} / 5.0")

st.divider()

# Visualization Tabs
tab1, tab2, tab3 = st.tabs(["📊 Salary & Distribution", "📈 Experience & Department", "📋 Dataset View"])

with tab1:
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.histplot(filtered_df['Monthly_Salary'], kde=True, color='teal', ax=ax1)
    ax1.set_title("Salary Distribution")
    st.pyplot(fig1)

with tab2:
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=filtered_df, x='Years_Experience', y='Monthly_Salary', hue='Education_Level', ax=ax2)
    ax2.set_title("Experience vs Monthly Salary")
    st.pyplot(fig2)

with tab3:
    st.dataframe(filtered_df)
