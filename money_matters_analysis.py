import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD DATA
# ==========================================

df = pd.read_csv("data/Money Matters- How College Students Plan, Spend & Save .csv")

print("===== DATASET PREVIEW =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==========================================
# STEP 2: TRANSFORM
# ==========================================

print("\n===== 2.1 DATASET DIMENSIONS =====")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


print("\n===== 2.2 COLUMN NAMES =====")
print(df.columns.tolist())


print("\n===== 2.3 DATA TYPES =====")
print(df.dtypes)


print("\n===== 2.4 DATASET INFORMATION =====")
df.info()


print("\n===== 2.5 MISSING VALUES =====")

missing_values = df.isnull().sum()

print("Columns with missing values:")
print(missing_values[missing_values > 0])

print("\nMissing value percentage:")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage[missing_percentage > 0])


print("\n===== 2.6 DUPLICATE RESPONSES =====")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

if duplicate_count > 0:
    print("\nDuplicate rows:")
    print(df[df.duplicated(keep=False)])


print("\n===== 2.7 CATEGORY VALUE CHECK =====")

for column in df.columns:
    print("\n---", column, "---")
    print(df[column].value_counts(dropna=False))


# ==========================================
# STEP 2.8: CLEAN DATA
# ==========================================

print("\n===== 2.8 CLEANING DATASET =====")

# Remove completely empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

print("Empty rows removed and duplicate rows removed.")


# ==========================================
# STEP 2.9: VERIFY CLEANED DATASET
# ==========================================

print("\n===== 2.9 VERIFY CLEANED DATASET =====")

print("Final rows:", df.shape[0])
print("Final columns:", df.shape[1])

print("Total missing values:", df.isnull().sum().sum())
print("Total duplicate rows:", df.duplicated().sum())

print("\nFirst 5 rows:")
print(df.head())

print("Statistical summary :",df.describe())


# ==========================================
# STEP 3: LOAD CLEAN DATA
# ==========================================

clean_df = df.copy()

print("\n===== CLEAN DATASET =====")
print("Clean dataset shape:", clean_df.shape)

clean_df.to_csv("data/financial_planning_cleaned.csv", index=False)

print("Cleaned dataset saved successfully.")


# ==========================================
# STEP 4: EXPLORATORY DATA ANALYSIS
# RELATIONSHIP-BASED EDA
# ==========================================

print("\n\n==========================================")
print("STEP 4: EXPLORATORY DATA ANALYSIS")
print("RELATIONSHIP-BASED EDA")
print("==========================================")


# ==========================================
# RELATIONSHIP 1
# Q5 PLANNING × Q8 UNPLANNED PURCHASES
# ==========================================

print("\n\n===== RELATIONSHIP 1 =====")
print("Spending Planning vs Unplanned Purchases")

# Group spending planning behaviour
clean_df["Planning_Group"] = clean_df[
    "Q5. Do you usually plan how you will spend your money?"
].replace({
    "Always": "Frequent Planning",
    "Often": "Frequent Planning",
    "Sometimes": "Sometimes",
    "Rarely": "Infrequent Planning",
    "Never": "Infrequent Planning"
})

# Group unplanned purchase behaviour
clean_df["Unplanned_Group"] = clean_df[
    "Q8. How often do you make unplanned purchases?"
].replace({
    "Never": "Low",
    "Rarely": "Low",
    "Sometimes": "Moderate",
    "Often": "High",
    "Very often": "High"
})

# Crosstab
planning_unplanned = pd.crosstab(
    clean_df["Planning_Group"],
    clean_df["Unplanned_Group"]
)

print("\nNumber of students:")
print(planning_unplanned)

# Row percentages
planning_unplanned_pct = pd.crosstab(
    clean_df["Planning_Group"],
    clean_df["Unplanned_Group"],
    normalize="index"
) * 100

print("\nRow percentages:")
print(planning_unplanned_pct.round(2))

# Chart
planning_unplanned_pct.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Spending Planning vs Unplanned Purchases")
plt.xlabel("Spending Planning Behaviour")
plt.ylabel("Percentage of Students")
plt.legend(title="Unplanned Purchases")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==========================================
# RELATIONSHIP 2
# Q14 BUDGET × Q15 FINANCIAL CONFIDENCE
# ==========================================

print("\n\n===== RELATIONSHIP 2 =====")
print("Budgeting Behaviour vs Financial Confidence")

budget_confidence = clean_df.groupby(
    "Q14. Do you currently follow a personal budget?"
)["Q15. How confident are you in managing your personal finances?"].agg(
    ["count", "mean", "median"]
)

print("\nFinancial confidence by budgeting behaviour:")
print(budget_confidence.round(2))

# Chart
budget_confidence["mean"].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Budgeting Behaviour vs Financial Confidence")
plt.xlabel("Budgeting Behaviour")
plt.ylabel("Average Financial Confidence")
plt.ylim(0, 5)
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ==========================================
# RELATIONSHIP 3
# Q17 FINANCIAL EDUCATION × Q18 DESIRE TO LEARN
# ==========================================

print("\n\n===== RELATIONSHIP 3 =====")
print("Formal Financial Education vs Desire to Learn")

# Group desire to learn
clean_df["Learning_Group"] = clean_df[
    "Q18. Would you like to learn more about budgeting, saving, and financial planning?"
].replace({
    "Definitely yes": "Wants to Learn",
    "Probably yes": "Wants to Learn",
    "Not sure": "Not Sure",
    "Probably no": "Does Not Want to Learn",
    "Definitely no": "Does Not Want to Learn"
})

education_learning = pd.crosstab(
    clean_df[
        "Q17. Have you received any formal education or training about financial planning?"
    ],
    clean_df["Learning_Group"]
)

print("\nNumber of students:")
print(education_learning)

# Row percentages
education_learning_pct = pd.crosstab(
    clean_df[
        "Q17. Have you received any formal education or training about financial planning?"
    ],
    clean_df["Learning_Group"],
    normalize="index"
) * 100

print("\nRow percentages:")
print(education_learning_pct.round(2))

# Chart
education_learning_pct.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Formal Financial Education vs Desire to Learn")
plt.xlabel("Formal Financial Education")
plt.ylabel("Percentage of Students")
plt.legend(title="Desire to Learn")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==========================================
# RELATIONSHIP 4
# Q8 UNPLANNED PURCHASES × Q21 RUNNING OUT OF MONEY
# ==========================================

print("\n\n===== RELATIONSHIP 4 =====")
print("Unplanned Purchases vs Running Out of Money")


# Create unplanned purchase groups
clean_df["Unplanned_Group"] = clean_df[
    "Q8. How often do you make unplanned purchases?"
].replace({
    "Never": "Low",
    "Rarely": "Low",
    "Sometimes": "Moderate",
    "Often": "High",
    "Very often": "High"
})


# Create crosstab
unplanned_money = pd.crosstab(
    clean_df["Unplanned_Group"],
    clean_df[
        "Q21. Have you ever faced a situation where you ran out of money because of unplanned spending?"
    ]
)

print("\nNumber of students:")
print(unplanned_money)


# Calculate row percentages
unplanned_money_pct = pd.crosstab(
    clean_df["Unplanned_Group"],
    clean_df[
        "Q21. Have you ever faced a situation where you ran out of money because of unplanned spending?"
    ],
    normalize="index"
) * 100

print("\nRow percentages:")
print(unplanned_money_pct.round(2))


# Plot
unplanned_money_pct.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Unplanned Purchases vs Running Out of Money")
plt.xlabel("Frequency of Unplanned Purchases")
plt.ylabel("Percentage of Students")
plt.legend(title="Ran Out of Money")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==========================================
# RELATIONSHIP 5
# Q6 EXPENSE TRACKING × Q15 FINANCIAL CONFIDENCE
# ==========================================

print("\n\n===== RELATIONSHIP 5 =====")
print("Expense Tracking vs Financial Confidence")


tracking_confidence = clean_df.groupby(
    "Q6. How often do you track your expenses?"
)["Q15. How confident are you in managing your personal finances?"].agg(
    ["count", "mean", "median"]
)

print("\nFinancial confidence by expense tracking frequency:")
print(tracking_confidence.round(2))


tracking_confidence["mean"].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Expense Tracking vs Financial Confidence")
plt.xlabel("Expense Tracking Frequency")
plt.ylabel("Average Financial Confidence")
plt.ylim(0, 5)
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ==========================================
# RELATIONSHIP 6
# Q13 SAVING IMPORTANCE × Q15 FINANCIAL CONFIDENCE
# ==========================================

print("\n\n===== RELATIONSHIP 6 =====")
print("Saving Importance vs Financial Confidence")


saving_confidence = clean_df.groupby(
    "Q13. How much importance do you give to saving money?"
)["Q15. How confident are you in managing your personal finances?"].agg(
    ["count", "mean", "median"]
)

print("\nFinancial confidence by saving importance:")
print(saving_confidence.round(2))


saving_confidence["mean"].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Saving Importance vs Financial Confidence")
plt.xlabel("Importance Given to Saving")
plt.ylabel("Average Financial Confidence")
plt.ylim(0, 5)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==========================================
# RELATIONSHIP 7
# Q5 PLANNING × Q11 SAVING BEHAVIOUR
# ==========================================

print("\n\n===== RELATIONSHIP 7 =====")
print("Spending Planning vs Saving Behaviour")


# ==========================================
# CREATE PLANNING GROUP
# ==========================================

clean_df["Planning_Group"] = clean_df[
    "Q5. Do you usually plan how you will spend your money?"
].replace({
    "Always": "Frequent Planning",
    "Often": "Frequent Planning",
    "Sometimes": "Sometimes",
    "Rarely": "Infrequent Planning",
    "Never": "Infrequent Planning"
})


# ==========================================
# CREATE CROSSTAB
# ==========================================

planning_saving = pd.crosstab(
    clean_df["Planning_Group"],
    clean_df[
        "Q11. Do you save a portion of the money you receive?"
    ]
)

print("\nNumber of students:")
print(planning_saving)


# ==========================================
# ROW PERCENTAGES
# ==========================================

planning_saving_pct = pd.crosstab(
    clean_df["Planning_Group"],
    clean_df[
        "Q11. Do you save a portion of the money you receive?"
    ],
    normalize="index"
) * 100

print("\nRow percentages:")
print(planning_saving_pct.round(2))


# ==========================================
# VISUALIZATION
# ==========================================

planning_saving_pct.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Spending Planning vs Saving Behaviour")
plt.xlabel("Spending Planning Behaviour")
plt.ylabel("Percentage of Students")
plt.legend(title="Saving Behaviour")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\n\n==========================================")
print("RELATIONSHIP ANALYSIS COMPLETED")
print("==========================================")


print("\n\n==========================================")
print("STEP 5: MULTI-SELECT ANALYSIS")
print("==========================================")


print("\n\n===== Q9: FACTORS INFLUENCING UNPLANNED SPENDING =====")


# Find the Q9 column automatically
q9_columns = [col for col in clean_df.columns if col.startswith("Q9.")]

print("\nQ9 column found:")
print(q9_columns)


# Check that exactly one Q9 column was found
if len(q9_columns) != 1:
    print("\nERROR: Expected exactly one Q9 column.")
else:

    q9_column = q9_columns[0]


    # Split multiple selections
    q9_split = (
        clean_df[q9_column]
        .dropna()
        .astype(str)
        .str.split(";")
        .explode()
        .str.strip()
    )


    # Count each selected factor
    q9_counts = q9_split.value_counts()


    print("\nNumber of selections:")
    print(q9_counts)


    # Percentage of all students
    q9_percentage = (q9_counts / len(clean_df)) * 100


    print("\nPercentage of students:")
    print(q9_percentage.round(2))


    # Chart
    q9_counts.sort_values().plot(
        kind="barh",
        figsize=(10, 6)
    )

    plt.title("Factors Influencing Unplanned Spending")
    plt.xlabel("Number of Students")
    plt.ylabel("Factor")
    plt.tight_layout()
    plt.show()


print("\n\n===== Q16: SOURCES OF FINANCIAL KNOWLEDGE =====")


# Find Q16 column automatically
q16_columns = [col for col in clean_df.columns if col.startswith("Q16.")]

print("\nQ16 column found:")
print(q16_columns)


if len(q16_columns) != 1:
    print("\nERROR: Expected exactly one Q16 column.")

else:

    q16_column = q16_columns[0]


    # Split multiple selections
    q16_split = (
        clean_df[q16_column]
        .dropna()
        .astype(str)
        .str.split(";")
        .explode()
        .str.strip()
    )


    # Count selections
    q16_counts = q16_split.value_counts()


    print("\nNumber of selections:")
    print(q16_counts)


    # Percentage of students
    q16_percentage = (q16_counts / len(clean_df)) * 100


    print("\nPercentage of students:")
    print(q16_percentage.round(2))


    # Chart
    q16_counts.sort_values().plot(
        kind="barh",
        figsize=(10, 6)
    )

    plt.title("Sources of Financial Knowledge")
    plt.xlabel("Number of Students")
    plt.ylabel("Source")
    plt.tight_layout()
    plt.show()

    
print("\n\n===== Q22: WAYS TO IMPROVE FINANCIAL PLANNING =====")


# Find Q22 column automatically
q22_columns = [col for col in clean_df.columns if col.startswith("Q22.")]

print("\nQ22 column found:")
print(q22_columns)


if len(q22_columns) != 1:
    print("\nERROR: Expected exactly one Q22 column.")

else:

    q22_column = q22_columns[0]


    # Split multiple selections
    q22_split = (
        clean_df[q22_column]
        .dropna()
        .astype(str)
        .str.split(";")
        .explode()
        .str.strip()
    )


    # Count selections
    q22_counts = q22_split.value_counts()


    print("\nNumber of selections:")
    print(q22_counts)


    # Percentage of students
    q22_percentage = (q22_counts / len(clean_df)) * 100


    print("\nPercentage of students:")
    print(q22_percentage.round(2))


    # Chart
    q22_counts.sort_values().plot(
        kind="barh",
        figsize=(10, 6)
    )

    plt.title("Ways to Improve Financial Planning")
    plt.xlabel("Number of Students")
    plt.ylabel("Method")
    plt.tight_layout()
    plt.show()

print("\n\n==========================================")
print("STEP 6: LIKERT SCALE ANALYSIS")
print("==========================================")


# ==========================================
# FIND ALL Q19 COLUMNS
# ==========================================

q19_columns = [
    col for col in clean_df.columns
    if col.startswith("Q19.")
]

print("\nQ19 columns found:")
for col in q19_columns:
    print("-", col)


print("\nNumber of Q19 statements:", len(q19_columns))

print("\n\n===== Q19: LIKERT SCALE ANALYSIS =====")


# ==========================================
# LIKERT RESPONSE ORDER
# ==========================================

likert_order = [
    "Strongly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly Agree"
]


# ==========================================
# CREATE SUMMARY TABLE
# ==========================================

likert_results = []


for column in q19_columns:

    counts = clean_df[column].value_counts()

    total = len(clean_df)

    percentages = (counts / total) * 100


    # Short statement name for easier reading
    statement = column.split("[")[-1].replace("]", "")


    result = {
        "Statement": statement
    }


    for response in likert_order:
        result[response] = round(
            percentages.get(response, 0),
            2
        )


    likert_results.append(result)


likert_summary = pd.DataFrame(likert_results)


print("\n===== LIKERT PERCENTAGE SUMMARY =====")
print(likert_summary.to_string(index=False))

# ==========================================
# Q19: GROUPED LIKERT ANALYSIS
# ==========================================

likert_grouped = likert_summary[["Statement"]].copy()

likert_grouped["Agreement"] = (
    likert_summary["Agree"] +
    likert_summary["Strongly Agree"]
)

likert_grouped["Neutral"] = likert_summary["Neutral"]

likert_grouped["Disagreement"] = (
    likert_summary["Disagree"] +
    likert_summary["Strongly Disagree"]
)

print("\n===== GROUPED LIKERT SUMMARY =====")
print(likert_grouped.to_string(index=False))

# ==========================================
# Q19: LIKERT STACKED BAR CHART
# ==========================================

plot_data = likert_grouped.set_index("Statement")

plot_data[["Disagreement", "Neutral", "Agreement"]].plot(
    kind="barh",
    stacked=True,
    figsize=(12, 7)
)

plt.xlabel("Percentage of Respondents")
plt.ylabel("")
plt.title("College Students' Attitudes Toward Spending, Saving and Financial Planning")

plt.legend(
    title="Response",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()

# ==========================================
# Q25: OPEN-ENDED RESPONSES
# ==========================================

q25_column = [col for col in clean_df.columns if col.startswith("Q25.")][0]

print("\n===== Q25: OPEN-ENDED RESPONSES =====")

q25_responses = clean_df[q25_column].dropna()

print("Total responses:", len(q25_responses))
print("\nResponses:\n")

for i, response in enumerate(q25_responses, start=1):
    print(f"{i}. {response}")

# ==========================================
# STEP 6: KEY FINDINGS
# ==========================================

# All Key findings are available on the dashboard.


# ==========================================
# STEP 7: FINAL ANALYSIS OUTPUT
# ==========================================

# Findings, interpretations and recommendations
# is given on the dashboard.