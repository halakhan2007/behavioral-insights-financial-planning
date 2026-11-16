import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Financial Planning Among College Students",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("data/financial_planning_cleaned.csv")

# =========================================================
# COLUMN HELPERS
# =========================================================

def get_col(prefix):
    return [col for col in df.columns if col.startswith(prefix)][0]


q5_col = get_col("Q5.")
q6_col = get_col("Q6.")
q7_col = get_col("Q7.")
q8_col = get_col("Q8.")
q9_col = get_col("Q9.")
q11_col = get_col("Q11.")
q13_col = get_col("Q13.")
q14_col = get_col("Q14.")
q15_col = get_col("Q15.")
q16_col = get_col("Q16.")
q17_col = get_col("Q17.")
q18_col = get_col("Q18.")
q21_col = get_col("Q21.")
q22_col = get_col("Q22.")

q19_columns = [
    col for col in df.columns
    if col.startswith("Q19.")
]

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💰 Financial Planning")

st.sidebar.markdown(
    """
    ### Field Project Dashboard

    **Topic:**  
    Behavioral Insights into Financial Planning among College Students

    **Responses:** 72

    ---
    """
)

page = st.sidebar.radio(
    "Navigate to",
    [
        "🏠 Overview",
        "💸 Spending Behaviour",
        "💰 Saving & Budgeting",
        "🧠 Financial Awareness",
        "📋 Student Opinions",
        "🔎 Data Preview"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Primary survey data | Field Project")

# =========================================================
# OVERVIEW
# =========================================================

if page == "🏠 Overview":

    st.title("💰 Financial Planning Among College Students")

    st.markdown(
        "### Behavioral insights into how college students plan, spend and save"
    )

    st.info(
        "This dashboard presents findings from a primary survey conducted "
        "among college students as part of a Data Science Field Project."
    )

    st.divider()

    # ---------------- KPI CARDS ----------------

    saving_importance = df[q13_col].mean()
    confidence = df[q15_col].mean()

    planning_important = (
        df[q19_columns[-1]]
        .isin(["Agree", "Strongly Agree"])
        .mean() * 100
    )

    regular_savers = (
        df[q11_col]
        .eq("Yes regularly")
        .mean() * 100
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Respondents",
        len(df)
    )

    col2.metric(
        "💰 Saving Importance",
        f"{saving_importance:.2f} / 5"
    )

    col3.metric(
        "📊 Financial Confidence",
        f"{confidence:.2f} / 5"
    )

    col4.metric(
        "📚 Planning Is Important",
        f"{planning_important:.1f}%"
    )

    st.divider()

    # ---------------- PROJECT OBJECTIVE ----------------

    st.header("🎯 Project Objective")

    st.write(
        "To understand how college students plan their spending, manage "
        "their money, save for future needs, and perceive their own "
        "financial planning abilities."
    )

    st.divider()

    # ---------------- HEADLINE FINDINGS ----------------

    st.header("🔎 Headline Findings")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "💰 Students place high importance on saving and financial security."
        )

        st.write(
            "79.17% agreed or strongly agreed that they feel more "
            "financially secure when they have savings."
        )

        st.warning(
            "🛒 Unplanned spending remains common."
        )

        st.write(
            "59.72% agreed or strongly agreed that they sometimes spend "
            "money even when they had not planned to."
        )

    with col2:

        st.info(
            "📚 There is strong interest in financial education."
        )

        st.write(
            "A large proportion of students who had not received formal "
            "financial education still wanted to learn more."
        )

        st.success(
            "🎓 Students recognize the importance of financial planning."
        )

        st.write(
            f"{planning_important:.1f}% agreed or strongly agreed that "
            "financial planning is important for college students."
        )

    st.divider()

    st.caption(
        "Source: Primary survey data collected through a questionnaire. "
        "Total responses: 72."
    )

# =========================================================
# SPENDING BEHAVIOUR
# =========================================================

elif page == "💸 Spending Behaviour":

    st.title("💸 Spending Behaviour")

    st.write(
        "This section examines how students plan their spending, "
        "make unplanned purchases and manage unexpected spending."
    )

    st.divider()

    # ---------------- SPENDING CATEGORY ----------------

    st.subheader("Where do students spend the most?")

    spending_counts = df[q7_col].value_counts()

    fig, ax = plt.subplots(figsize=(10, 5))

    spending_counts.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Number of Students")
    ax.set_ylabel("")
    ax.set_title("Largest Spending Categories")

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------- UNPLANNED PURCHASES ----------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Frequency of Unplanned Purchases")

        counts = df[q8_col].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Number of Students")
        ax.set_xlabel("")
        ax.set_title("Unplanned Purchase Frequency")

        plt.xticks(rotation=25)

        st.pyplot(fig)

    with col2:

        st.subheader("Running Out of Money")

        counts = df[q21_col].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Number of Students")
        ax.set_xlabel("")
        ax.set_title("Running Out of Money Due to Unplanned Spending")

        plt.xticks(rotation=25)

        st.pyplot(fig)

    st.divider()

    # ---------------- INSIGHT ----------------

    st.subheader("💡 Key Insight")

    st.write(
        "Students reporting more frequent unplanned purchases also tended "
        "to report more frequent experiences of running out of money due "
        "to unplanned spending."
    )

    st.caption(
        "This describes an observed relationship in the survey and does "
        "not establish causation."
    )

# =========================================================
# SAVING & BUDGETING
# =========================================================

elif page == "💰 Saving & Budgeting":

    st.title("💰 Saving & Budgeting")

    st.write(
        "This section explores saving behaviour, budgeting practices "
        "and reported financial confidence."
    )

    st.divider()

    # ---------------- SAVING IMPORTANCE ----------------

    st.subheader("Saving Importance vs Financial Confidence")

    saving_confidence = (
        df.groupby(q13_col)[q15_col]
        .mean()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        saving_confidence.index,
        saving_confidence.values,
        marker="o"
    )

    ax.set_xlabel("Importance Given to Saving (1–5)")
    ax.set_ylabel("Average Financial Confidence (1–5)")
    ax.set_title("Saving Importance and Financial Confidence")

    ax.set_xticks([1, 2, 3, 4, 5])

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------- BUDGETING ----------------

    st.subheader("Personal Budget vs Financial Confidence")

    budget_confidence = (
        df.groupby(q14_col)[q15_col]
        .mean()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    budget_confidence.plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Average Financial Confidence")
    ax.set_ylabel("")
    ax.set_title("Budgeting and Financial Confidence")

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------- SAVING HABIT ----------------

    st.subheader("Saving Behaviour")

    saving_counts = df[q11_col].value_counts()

    fig, ax = plt.subplots(figsize=(9, 5))

    saving_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_ylabel("Number of Students")
    ax.set_xlabel("")
    ax.set_title("How Frequently Students Save Money")

    plt.xticks(rotation=20)

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    st.info(
        "Students who placed greater importance on saving generally "
        "reported higher average financial confidence."
    )

# =========================================================
# FINANCIAL AWARENESS
# =========================================================

elif page == "🧠 Financial Awareness":

    st.title("🧠 Financial Awareness")

    st.write(
        "This section examines where students learn about personal "
        "finance, whether they have received formal education, and "
        "whether they want to learn more."
    )

    st.divider()

    # ---------------- EDUCATION ----------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Formal Financial Education")

        education_counts = df[q17_col].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        education_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Number of Students")
        ax.set_xlabel("")
        ax.set_title("Formal Education or Training")

        plt.xticks(rotation=20)

        st.pyplot(fig)

    with col2:

        st.subheader("Desire to Learn More")

        learn_counts = df[q18_col].value_counts()

        fig, ax = plt.subplots(figsize=(7, 5))

        learn_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel("Number of Students")
        ax.set_xlabel("")
        ax.set_title("Interest in Learning Financial Planning")

        plt.xticks(rotation=25)

        st.pyplot(fig)

    st.divider()

    # ---------------- SOURCES OF KNOWLEDGE ----------------

    st.subheader("Where do students learn about personal finance?")

    q16_counts = {}

    for response in df[q16_col].dropna():

        for item in response.split(","):

            item = item.strip()

            q16_counts[item] = q16_counts.get(item, 0) + 1

    q16_series = pd.Series(q16_counts).sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))

    q16_series.plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Number of Students")
    ax.set_ylabel("")
    ax.set_title("Sources of Financial Knowledge")

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------- IMPROVEMENT ----------------

    st.subheader("What could improve financial planning?")

    q22_counts = {}

    for response in df[q22_col].dropna():

        for item in response.split(","):

            item = item.strip()

            q22_counts[item] = q22_counts.get(item, 0) + 1

    q22_series = pd.Series(q22_counts).sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))

    q22_series.plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Number of Students")
    ax.set_ylabel("")
    ax.set_title("Suggested Ways to Improve Financial Planning")

    plt.tight_layout()

    st.pyplot(fig)

# =========================================================
# STUDENT OPINIONS
# =========================================================

elif page == "📋 Student Opinions":

    st.title("📋 Student Opinions")

    st.write(
        "This section summarizes students' attitudes toward spending, "
        "saving and financial planning."
    )

    st.divider()

    # ---------------- Q19 LIKERT ----------------

    st.subheader("Attitudes Toward Spending, Saving and Planning")

    likert_order = [
        "Strongly Disagree",
        "Disagree",
        "Neutral",
        "Agree",
        "Strongly Agree"
    ]

    likert_results = []

    for column in q19_columns:

        counts = df[column].value_counts()

        statement = column.split("[")[-1].replace("]", "")

        result = {
            "Statement": statement
        }

        for response in likert_order:
            result[response] = (
                counts.get(response, 0) / len(df) * 100
            )

        likert_results.append(result)

    likert_df = pd.DataFrame(likert_results)

    fig, ax = plt.subplots(figsize=(12, 7))

    left = [0] * len(likert_df)

    for response in likert_order:

        values = likert_df[response].values

        ax.barh(
            likert_df["Statement"],
            values,
            left=left,
            label=response
        )

        left = [
            left[i] + values[i]
            for i in range(len(values))
        ]

    ax.set_xlabel("Percentage of Respondents")
    ax.set_title("Likert-Scale Responses")

    ax.legend(
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------- Q25 ----------------

    st.subheader("💬 What students suggested")

    st.write(
        "Recurring themes from the open-ended responses included:"
    )

    themes = [
        "🎓 Financial literacy workshops and seminars",
        "📊 Practical budgeting and expense-management education",
        "💰 Saving for emergencies and future needs",
        "📚 Greater financial education in colleges",
        "🔐 Financial-safety and scam awareness",
        "🧠 Development of practical money-management habits"
    ]

    for theme in themes:
        st.markdown(f"• {theme}")

    st.info(
        "These themes were identified manually from the 41 completed "
        "open-ended responses."
    )

# =========================================================
# DATA PREVIEW
# =========================================================

elif page == "🔎 Data Preview":

    st.title("🔎 Data Preview")

    st.write(
        "This section provides a quick view of the cleaned dataset "
        "used for analysis."
    )

    st.divider()

    # ---------------- DATASET INFO ----------------

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Duplicate Rows", df.duplicated().sum())

    st.divider()

    # ---------------- FIRST 5 ----------------

    st.subheader("📌 First 5 Rows")

    st.dataframe(
        df.head(5),
        use_container_width=True
    )

    st.divider()

    # ---------------- LAST 5 ----------------

    st.subheader("📌 Last 5 Rows")

    st.dataframe(
        df.tail(5),
        use_container_width=True
    )

    st.divider()

    # ---------------- DATA TYPES ----------------

    st.subheader("📋 Column Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values
    })

    st.dataframe(
        dtype_df,
        use_container_width=True
    )

    st.divider()

    # ---------------- MISSING VALUES ----------------

    st.subheader("⚠️ Missing Values")

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:
        st.success("No missing values found.")
    else:
        missing_df = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })

        st.dataframe(
            missing_df,
            use_container_width=True
        )

    st.divider()

    st.caption(
        "The cleaned dataset was used for the dashboard and exploratory analysis."
    )