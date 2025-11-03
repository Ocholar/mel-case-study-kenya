"""
MEL Quantitative Case Study - Data Cleaning and Analysis Script
Kenya MSME Manufacturing Sector Analysis

This script performs:
1. Data quality assessment and cleaning
2. Descriptive employment analysis
3. Sector recoding using ISIC classification
4. Policy-relevant metric calculations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = '../data/Data-CaseStudySCKenya_Original.xlsx'
df = pd.read_excel(file_path)

print("=== DATA CLEANING AND QUALITY ASSESSMENT ===\n")

# 1. Identify data quality issues
print("1. IDENTIFIED DATA QUALITY ISSUES:")
print("-" * 50)

# Issue 1: Inconsistent County Names
print("\nIssue 1: Inconsistent County Names")
print(f"Unique counties (sample): {df['County'].unique()[:10]}")

# Issue 2: Duplicate IDs
duplicate_ids = df[df.duplicated(subset=['ID'], keep=False)].sort_values(by='ID')
print(f"\nIssue 2: Duplicate IDs")
print(f"Number of rows with duplicate IDs: {len(duplicate_ids)}")

# Issue 3: Missing Values
print(f"\nIssue 3: Missing Values")
print(df.isnull().sum())

# Issue 4: Outliers in Employees
print(f"\nIssue 4: Outliers in Employees")
print(f"Max employees: {df['Employees'].max()}")
print(f"Min employees: {df['Employees'].min()}")

# Issue 5: Unstructured Production Text
print(f"\nIssue 5: Unstructured Production Text")
print(f"Sample production values:\n{df['Type of major production: industrial classification (ISIC)'].head(3)}")

print("\n\n=== DATA CLEANING STEPS ===\n")

# Step 1: Standardize County Names
df['County'] = df['County'].str.replace(r'[\.\s]', '', regex=True).str.lower()
county_mapping = {
    'nairobii': 'nairobi', 'naiirobi': 'nairobi', 'narobi': 'nairobi',
    'kisu mu': 'kisumu', 'kiaambu': 'kiambu', 'nakuru.': 'nakuru',
    'mombas a': 'mombasa', 'merru': 'meru',
}
df['County'] = df['County'].replace(county_mapping, regex=False)
df['County'] = df['County'].str.title()

# Step 2: Impute Missing Values
median_employees = df['Employees'].median()
median_revenue = df['Revenue'].median()
df['Employees'].fillna(median_employees, inplace=True)
df['Revenue'].fillna(median_revenue, inplace=True)

# Step 3: Cap Outliers
df['Employees_Capped'] = df['Employees'].clip(upper=50)

# Step 4: Extract ISIC Code
df['ISIC_Code'] = df['Type of major production: industrial classification (ISIC)'].str.extract(r'(\d{4})').astype(float)
df['ISIC_Code'].fillna(9999, inplace=True)
df['ISIC_Code'] = df['ISIC_Code'].astype(int)

# Step 5: Create Sector Variable
df['ISIC_2_Digit'] = df['ISIC_Code'].astype(str).str[:2]

def map_isic_to_sector(isic_2_digit):
    sector_map = {
        ('10', '11', '12'): 'Food, Beverages & Tobacco',
        ('13', '14', '15'): 'Textiles, Apparel & Leather',
        ('16', '17', '18'): 'Wood, Paper & Printing',
        ('19', '20', '21', '22', '23'): 'Chemicals, Plastics & Non-Metallic Minerals',
        ('24', '25'): 'Basic & Fabricated Metals',
        ('26', '27'): 'Electronic & Electrical Equipment',
        ('28', '29', '30'): 'Machinery & Transport Equipment',
        ('31', '32', '33'): 'Other Manufacturing & Repair',
    }
    for codes, sector in sector_map.items():
        if isic_2_digit in codes:
            return sector
    return 'Unclassified'

df['Sector'] = df['ISIC_2_Digit'].apply(map_isic_to_sector)

print("✓ Standardized county names")
print("✓ Imputed missing values with medians")
print("✓ Capped outliers at 50 employees")
print("✓ Extracted ISIC codes")
print("✓ Created sector variable from ISIC classification")

print("\n\n=== DESCRIPTIVE EMPLOYMENT ANALYSIS ===\n")

total_employment = df['Employees_Capped'].sum()
avg_employment = df['Employees_Capped'].mean()
employment_by_size = df.groupby('Size')['Employees_Capped'].agg(['sum', 'mean', 'count']).reset_index()

print(f"Total Employment (Capped): {total_employment:,.0f}")
print(f"Average Employment per Firm: {avg_employment:.2f}")
print(f"\nEmployment by Firm Size:")
print(employment_by_size.to_string(index=False))

print("\n\n=== SECTOR DISTRIBUTION ===\n")

sector_distribution = df.groupby('Sector').size().reset_index(name='Firm_Count').sort_values(by='Firm_Count', ascending=False)
print(sector_distribution.to_string(index=False))

print("\n\n=== POLICY METRICS ===\n")

# Metric 1: Revenue per Employee
df['Revenue_per_Employee'] = df['Revenue'] / df['Employees_Capped']
df['Revenue_per_Employee'].replace([float('inf'), -float('inf')], 0, inplace=True)
rev_per_emp_by_training = df.groupby('Training')['Revenue_per_Employee'].mean().reset_index()

print("Metric 1: Revenue per Employee by Training Status")
print(rev_per_emp_by_training.to_string(index=False))

# Metric 2: Female-Owned Firms' Share of Employment
total_capped_employment = df['Employees_Capped'].sum()
female_owned_employment = df[df['Gender of owner'] == 'Female']['Employees_Capped'].sum()
female_share_of_employment = (female_owned_employment / total_capped_employment) * 100

print(f"\nMetric 2: Female-Owned Firms' Share of Total Employment")
print(f"Female-Owned Firms' Share: {female_share_of_employment:.2f}%")

# Save cleaned dataset
df.to_excel('../data/Cleaned_Data_CaseStudySCKenya.xlsx', index=False)
print("\n✓ Cleaned dataset saved to: ../data/Cleaned_Data_CaseStudySCKenya.xlsx")

