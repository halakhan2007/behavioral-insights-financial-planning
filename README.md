# 💰 Behavioral Insights into Financial Planning Among College Students

A Python-based data analysis and interactive dashboard project exploring financial planning habits, spending behaviour, saving practices, budgeting and financial awareness among college students.

## 🚀 Live Dashboard

**Explore the deployed application here:**

[Open the Financial Planning Dashboard](https://behavioral-insights-financial-planning-ghwjuc3xqodfindbuc5v3e.streamlit.app/)

Built with Python and Streamlit, the dashboard allows users to explore survey findings, student financial behaviour and interactive data visualisations.

## 📌 Project Overview

This project investigates how college students plan, spend, save and manage their money.

Primary data was collected through a Google Forms questionnaire containing 25 questions, with 72 student responses.

The collected data was processed and analysed using Python. The project includes data inspection, cleaning, transformation, exploratory data analysis, relationship-based analysis and visualisation.

An interactive Streamlit dashboard presents the findings through different sections, allowing users to explore financial behaviour and selected relationships between survey variables.

## 🎯 Project Objectives

- Understand financial planning habits among college students.
- Examine spending patterns, saving practices and budgeting behaviour.
- Explore relationships between different financial behaviour variables.
- Identify patterns in financial awareness and financial education.
- Present survey findings through statistical analysis and visualisations.
- Develop an interactive dashboard for exploring the results.

## ✨ Key Features

### 1. Data Processing and Cleaning
- Dataset inspection and preview.
- Examination of rows, columns and data types.
- Missing-value analysis.
- Duplicate response identification and removal.
- Removal of completely empty rows.
- Export of the cleaned dataset.

### 2. Exploratory Data Analysis
- Descriptive statistical summaries.
- Category-wise response analysis.
- Cross-tabulation of selected survey variables.
- Row-wise percentage analysis.
- Relationship-based exploration of student financial behaviour.

### 3. Relationship-Based Analysis

The project explores seven relationships:

1. Spending planning vs unplanned purchases.
2. Budgeting behaviour vs financial confidence.
3. Formal financial education vs desire to learn.
4. Unplanned purchases vs running out of money.
5. Expense tracking vs financial confidence.
6. Saving importance vs financial confidence.
7. Spending planning vs saving behaviour.

### 4. Survey Response Analysis
- Analysis of multiple-selection responses.
- Exploration of financial knowledge sources.
- Likert-scale analysis of student opinions.
- Examination of open-ended responses.

### 5. Interactive Streamlit Dashboard

The dashboard contains six sections:

- **Overview:** Respondent count, key indicators, project objectives and headline findings.
- **Spending Behaviour:** Spending categories, unplanned purchases and running out of money.
- **Saving & Budgeting:** Saving habits, budgeting practices and financial confidence.
- **Financial Awareness:** Financial education, learning interests and sources of financial knowledge.
- **Student Opinions:** Likert-scale responses and themes from open-ended answers.
- **Data Preview:** Dataset preview, dimensions, data types and missing-value information.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Microsoft Excel

## 📁 Project Structure

```text
Financial-Planning-Analysis/
│
├── data/
│   ├── original_dataset.csv
│   └── financial_planning_cleaned.csv
│
├── charts/
│   └── generated charts
│
├── app.py
├── money_matters_analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

The dataset filenames shown above are examples. Replace them with the actual filenames in your repository.

## 📂 Project Files

| File or Folder | Description |
|---|---|
| `app.py` | Runs the interactive Streamlit dashboard. |
| `money_matters_analysis.py` | Performs data inspection, cleaning, exploratory analysis and relationship-based analysis. |
| `data/` | Stores the original and cleaned survey datasets. |
| `charts/` | Contains visualisations prepared for the project. |
| `requirements.txt` | Lists the Python libraries required to run the project. |

## 📝 Survey Questionnaire

Primary data was collected through a Google Forms questionnaire containing 25 questions related to financial planning, budgeting, spending habits, saving behaviour and financial awareness.

- **Data Collection Method:** Google Forms
- **Total Responses:** 72
- **Questionnaire:** [View the Google Form](https://forms.gle/22P8jJYMFC8nfphdA)

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Financial-Planning-Analysis
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the data analysis script

```bash
python money_matters_analysis.py
```

This script processes the original dataset, saves the cleaned dataset and performs the analysis.

### 6. Launch the Streamlit dashboard

```bash
streamlit run app.py
```

Streamlit will provide a local URL to access the interactive dashboard.

## 👥 Project Details

This project was completed as an academic field research project by a team of two members. It combines survey-based research, data preparation, statistical exploration and interactive visualisation to understand financial planning behaviour among college students.
