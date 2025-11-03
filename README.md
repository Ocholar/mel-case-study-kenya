# MEL Quantitative Case Study - Kenya MSME Manufacturing Analysis

## Overview

This repository contains a comprehensive Monitoring, Evaluation, and Learning (MEL) analysis of 5,016 Micro, Small, and Medium Enterprises (MSMEs) in Kenya's manufacturing sector. The analysis focuses on employment creation, business growth, and the impact of training interventions on firm productivity and gender equity.

**Project Status:** ✅ Complete
**Analysis Date:** November 2025
**Data Source:** Kenya MSME Manufacturing Survey
**Sample Size:** 5,016 firms across multiple counties

---

## Key Findings

### Employment Metrics

- **Total Employment Generated:** 11,277 jobs

- **Average Firm Size:** 2.25 employees

- **Micro Firm Contribution:** 70% of total employment

- **Female-Owned Firm Share:** 39.8% of employment (45% of firms)

### Training Impact

- **Revenue per Employee (Trained Firms):** Ksh 108,740

- **Revenue per Employee (Non-Trained Firms):** Ksh 100,560

- **Efficiency Gain from Training:** 8.1%

### Sector Distribution

| Sector | Firms | Share |
| --- | --- | --- |
| Food, Beverages & Tobacco | 1,358 | 27% |
| Textiles, Apparel & Leather | 960 | 19% |
| Wood, Paper & Printing | 802 | 16% |
| Chemicals, Plastics & Non-Metallic Minerals | 555 | 11% |
| Basic & Fabricated Metals | 498 | 10% |
| Machinery & Transport Equipment | 374 | 7% |
| Electronic & Electrical Equipment | 213 | 4% |
| Other Manufacturing & Repair | 256 | 5% |

---

## Repository Structure

```
mel-case-study-kenya/
├── README.md                                    # This file
├── data/
│   ├── Data-CaseStudySCKenya_Original.xlsx     # Original raw data (5,016 firms)
│   └── Cleaned_Data_CaseStudySCKenya.xlsx      # Cleaned and processed data
├── analysis/
│   ├── data_cleaning_analysis.py               # Python script for data cleaning and analysis
│   ├── chart_1_sector_distribution.png         # Sector distribution visualization
│   └── chart_2_avg_employees_by_training_gender.png  # Employment by training & gender
├── presentation/
│   └── MEL_CaseStudy_Presentation.pdf          # 8-slide professional presentation
└── documentation/
    ├── DATA_QUALITY_REPORT.md                  # Detailed data quality assessment
    └── METHODOLOGY.md                          # Analysis methodology and definitions
```

---

## Data Quality & Cleaning

### Issues Identified & Resolved

1. **Inconsistent County Names**
  - Issue: Spelling variations and extra characters (e.g., 'Nairobii', 'Kisu mu', 'Nakuru.')
  - Solution: Standardized all county names using string cleaning and mapping

2. **Duplicate IDs**
  - Issue: Multiple firms shared the same ID
  - Solution: Retained all rows as unique observations; flagged for investigation

3. **Missing Values**
  - Issue: Gaps in Revenue and Employees columns
  - Solution: Imputed with median values (robust to outliers)

4. **Outliers in Employee Counts**
  - Issue: Extreme values (max: 1,000 employees for a 'Micro' firm)
  - Solution: Capped at 50 employees (upper bound for 'Small' firm definition)

5. **Unstructured Production Text**
  - Issue: ISIC codes embedded in long text strings
  - Solution: Extracted 4-digit ISIC codes and created structured Sector variable

### Cleaning Steps Applied

✓ Standardized county names (25 unique values)✓ Imputed missing data with medians✓ Capped outliers at 50 employees✓ Extracted ISIC codes for classification✓ Created 8-sector manufacturing classification✓ Validated data integrity and consistency

---

## Methodology

### Descriptive Indicators

**1. Total Employment**

- Definition: Sum of all employees across firms

- Calculation: `SUM(Employees_Capped)`

- Result: 11,277 jobs

**2. Average Employment per Firm**

- Definition: Mean employees per firm

- Calculation: `MEAN(Employees_Capped)`

- Result: 2.25 employees

**3. Employment by Firm Size**

- Definition: Employment distribution across Micro, Small, and Medium firms

- Result: Micro (70%), Small (27%), Medium (3%)

### Policy-Relevant Metrics

**Metric 1: Employment Creation Efficiency (Revenue per Employee)**

- **Definition:** Total revenue generated per employee, indicating firm productivity

- **Numerator:** Total Revenue (Ksh)

- **Denominator:** Total Employees (Capped)

- **Calculation:** `Revenue / Employees_Capped`

- **Result by Training Status:**
  - Trained Firms: Ksh 108,740 per employee
  - Non-Trained Firms: Ksh 100,560 per employee
  - **Efficiency Gain: 8.1%**

- **Interpretation:** Training significantly improves firm productivity and economic output per job

- **Limitation:** Cross-sectional analysis; cannot establish causality without RCT

**Metric 2: Gender Equity in Employment**

- **Definition:** Female-owned firms' contribution to total employment

- **Numerator:** Total employees in female-owned firms

- **Denominator:** Total employees across all firms

- **Calculation:** `(Female Employment / Total Employment) × 100`

- **Result:** 39.8% of employment from female-owned firms

- **Interpretation:** Female-owned firms represent 45% of firms but only 39.8% of employment, indicating they are smaller employers on average

- **Limitation:** Gender of owner is a proxy; data doesn't capture employee gender breakdown

---

## Sector Classification

The analysis uses a simplified ISIC Rev. 4 classification system:

| Sector Code | ISIC Range | Sector Name |
| --- | --- | --- |
| 1 | 10-12 | Food, Beverages & Tobacco |
| 2 | 13-15 | Textiles, Apparel & Leather |
| 3 | 16-18 | Wood, Paper & Printing |
| 4 | 19-23 | Chemicals, Plastics & Non-Metallic Minerals |
| 5 | 24-25 | Basic & Fabricated Metals |
| 6 | 26-27 | Electronic & Electrical Equipment |
| 7 | 28-30 | Machinery & Transport Equipment |
| 8 | 31-33 | Other Manufacturing & Repair |

---

## Key Recommendations

### For Donor Programme

1. **Targeted Growth Support for Female-Owned Firms**
  - Develop specific interventions to help female-owned firms scale beyond micro level
  - Provide access to finance, business mentoring, and growth coaching
  - Address structural barriers to employment expansion

2. **Deepen Training Impact**
  - Investigate why training has greater scaling effects on male-owned firms
  - Adapt training content and delivery to address female-owned firm constraints
  - Consider gender-specific training modules and support mechanisms

3. **Sector-Specific Strategy**
  - Tailor programme support to dominant sectors (Food, Textiles, Wood)
  - Engage sector associations for industry-specific technical assistance
  - Develop value chain interventions for high-concentration sectors

---

## Files & Deliverables

### Data Files

- **Data-CaseStudySCKenya_Original.xlsx** (310 KB)
  - Original raw data with 5,016 firms and 8 variables
  - Includes: ID, County, Size, Gender of Owner, Production Type, Training, Revenue, Employees

- **Cleaned_Data_CaseStudySCKenya.xlsx** (310 KB)
  - Cleaned and processed data with additional derived variables
  - Includes: All original variables + Employees_Capped, ISIC_Code, ISIC_2_Digit, Sector, Revenue_per_Employee

### Analysis Files

- **data_cleaning_analysis.py**
  - Reproducible Python script for data cleaning and analysis
  - Generates all descriptive statistics and policy metrics
  - Can be run independently to regenerate results

- **chart_1_sector_distribution.png**
  - Horizontal bar chart showing firm distribution by manufacturing sector
  - Highlights sector concentration in Food, Textiles, and Wood industries

- **chart_2_avg_employees_by_training_gender.png**
  - Grouped bar chart comparing average employees by training status and owner gender
  - Shows disparities in firm scaling between trained/non-trained and male/female-owned firms

### Presentation

- **MEL_CaseStudy_Presentation.pdf** (8 slides)
  - Professional presentation suitable for donor and programme audiences
  - Includes: Data quality summary, employment analysis, sector recoding, policy metrics, recommendations
  - Design: Data-driven editorial aesthetic with structured tables and clear visualizations

---

## How to Use This Repository

### 1. Review the Analysis

- Start with the **README.md** (this file) for an overview

- Review the **presentation PDF** for a visual summary

- Check **METHODOLOGY.md** for detailed definitions and calculations

### 2. Explore the Data

- Open **Cleaned_Data_CaseStudySCKenya.xlsx** in Excel or your preferred tool

- Use the cleaned data for further analysis or integration with other datasets

### 3. Reproduce the Analysis

```bash
# Navigate to the analysis directory
cd analysis/

# Run the Python script
python3 data_cleaning_analysis.py
```

### 4. Adapt for Your Context

- Modify the **data_cleaning_analysis.py** script for your own datasets

- Adjust sector definitions based on local ISIC classifications

- Customize policy metrics to align with programme objectives

---

## Technical Details

### Tools & Technologies

- **Data Processing:** Python (pandas, numpy)

- **Visualization:** Matplotlib, Chart.js

- **Presentation:** HTML/CSS (responsive design)

- **Data Format:** Excel (.xlsx), CSV

### Python Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
openpyxl>=3.6.0
```

### System Requirements

- Python 3.8 or higher

- Excel or compatible spreadsheet application

- Web browser for presentation viewing

---

## Contact & Support

**Analyst:** Reagan Ochola

**Email:** reaochola@gmail.com

**Organization:** XXX Consulting

**Analysis Date:** November 2025

For questions about the analysis, methodology, or data, please refer to the detailed documentation in the `/documentation` folder.

---

## License

This analysis is provided for educational and programme evaluation purposes. Please ensure appropriate attribution when using or referencing this work.

---

## Changelog

### Version 1.0 (November 2025)

- Initial analysis of 5,016 MSME firms

- Data cleaning and quality assessment

- Descriptive employment analysis

- Sector recoding using ISIC classification

- Policy-relevant metric calculations

- Professional presentation and documentation

---

## Appendix: Data Dictionary

| Variable | Type | Description | Values |
| --- | --- | --- | --- |
| ID | Integer | Firm identifier | 1-5016 |
| County | String | Administrative county | 47 Kenyan counties |
| Size | String | Firm size classification | Micro, Small, Medium |
| Gender of owner | String | Owner gender | Male, Female |
| Type of major production | String | ISIC classification with description | ISIC codes 10-33 |
| Training | String | Training participation | Received training, No training |
| Revenue | Float | Annual revenue (Ksh) | 300 - 1,200,000 |
| Employees | Float | Number of employees | 1 - 1,000 |
| Employees_Capped | Float | Capped employees (max 50) | 1 - 50 |
| ISIC_Code | Integer | 4-digit ISIC code | 1001 - 3290 |
| ISIC_2_Digit | String | 2-digit ISIC code | 10 - 33 |
| Sector | String | Aggregated sector classification | 8 sector categories |
| Revenue_per_Employee | Float | Revenue efficiency metric | 300 - 1,200,000 |

---

**Last Updated:** November 3, 2025**Repository:** [https://github.com/Ocholar/mel-case-study-kenya](https://github.com/Ocholar/mel-case-study-kenya)
