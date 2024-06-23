import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Load the dataset
file_path = 'Dataset salary 2024.csv'  # Ensure this is the correct path to your CSV file
df = pd.read_csv(file_path)

# Set up the Streamlit app
st.title('Salary Analysis 2024')
st.write('This app analyzes the salary data for the year 2024.')

# Display the dataset
st.subheader('Dataset')
st.dataframe(df)

# Basic statistics
st.subheader('Basic Statistics')
st.write(df.describe())

# Data information
st.subheader('Data Information')
buffer = df.info(buf=None)
st.text(buffer)

# Employment counts
employment_counts = df['employment_type'].value_counts().sort_index()
df['employment_type_with_count'] = df['employment_type'].map(lambda x: f"{x}\n(N={employment_counts[x]})")

# Salary Distribution by Employment Type
st.subheader('Salary Distribution by Employment Type')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='employment_type_with_count', y='salary_in_usd', data=df, ax=ax)
ax.set_title('Salary Distribution by Employment Type')
ax.set_xlabel('Employment Type')
ax.set_ylabel('Salary in USD')
st.pyplot(fig)

# Average Salary by Company Location
st.subheader('Average Salary by Company Location')
average_salary_by_country = df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)
top_10_countries = average_salary_by_country.head(10).reset_index()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='salary_in_usd', y='company_location', data=top_10_countries, palette='viridis', ax=ax)
ax.set_title('Top 10 Company Locations by Average Salary')
ax.set_xlabel('Average Salary in USD')
ax.set_ylabel('Locations')
st.pyplot(fig)

# Average Salary by Job Title
st.subheader('Average Salary by Job Title')
average_salary_by_job_title = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
top_10_job_title = average_salary_by_job_title.head(15).reset_index()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='salary_in_usd', y='job_title', data=top_10_job_title, palette='viridis', ax=ax)
ax.set_title('Top 15 Job Titles by Average Salary')
ax.set_xlabel('Average Salary')
ax.set_ylabel('Job Title')
st.pyplot(fig)

# Average Salary by Experience Level
st.subheader('Average Salary by Experience Level')
average_salary_by_experience_level = df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
experience_level = average_salary_by_experience_level.reset_index()
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='salary_in_usd', y='experience_level', data=experience_level, palette='viridis', ax=ax)
ax.set_title('Experience Level and Average Salary')
ax.set_xlabel('Average Salary')
ax.set_ylabel('Experience Level')
st.pyplot(fig)

# Average Salary by Company Size
st.subheader('Average Salary by Company Size')
average_salary_by_company_size = df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)
company_size = average_salary_by_company_size.reset_index()
fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(x='salary_in_usd', y='company_size', data=company_size, palette='viridis', ax=ax)
ax.set_title('Company Size vs Average Salary')
ax.set_xlabel('Average Salary')
ax.set_ylabel('Company Size')
st.pyplot(fig)

