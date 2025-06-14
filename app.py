import streamlit as st
import pandas as pd
import random
import string
from faker import Faker
from io import BytesIO

st.set_page_config(page_title="FakeCSV Generator", layout="wide")
st.title("🧪 FakeCSV Generator")
st.markdown("Create realistic fake datasets for testing, AI training, or analytics!")

# --- Locale and Faker ---
available_locales = {
    "🇺🇸 US (English)": "en_US",
    "🇮🇳 India (Hindi)": "hi_IN",
    "🇫🇷 France (French)": "fr_FR",
    "🇩🇪 Germany (German)": "de_DE",
    "🇯🇵 Japan (Japanese)": "ja_JP"
}
locale = st.selectbox("🌐 Select Locale", list(available_locales.keys()), index=0)
fake = Faker(available_locales[locale])

# --- Built-in Field Generators ---
def get_builtin_fields():
    return {
        "Full Name": fake.name,
        "First Name": fake.first_name,
        "Last Name": fake.last_name,
        "Email": fake.email,
        "Phone Number": fake.phone_number,
        "Address": fake.address,
        "City": fake.city,
        "State": fake.state,
        "Country": fake.country,
        "Postal Code": fake.postcode,
        "Company": fake.company,
        "Job Title": fake.job,
        "Date": fake.date,
        "Time": fake.time,
        "Text": fake.text,
        "Username": fake.user_name,
        "Password": fake.password,
        "Credit Card Number": fake.credit_card_number,
        "IPv4": fake.ipv4,
        "URL": fake.url
    }

builtin_fields = get_builtin_fields()

# --- Category Presets ---
category_presets = {
    "E-commerce": ["Full Name", "Email", "Phone Number", "Address", "City", "Country", "Postal Code"],
    "Healthcare": ["Full Name", "Date", "Job Title", "City", "State", "Email"],
    "Finance": ["Full Name", "Email", "Credit Card Number", "Address", "Company"],
    "Education": ["Full Name", "Email", "Date", "Address", "Job Title"]
}

selected_category = st.selectbox("📂 Choose a Category (auto-selects fields)", ["None"] + list(category_presets.keys()))
if selected_category != "None":
    default_fields = category_presets[selected_category]
else:
    default_fields = []

# --- Column Selection ---
st.markdown("### 🏗️ Column Selection")
selected_fields = st.multiselect("✅ Select Built-in Fields", list(builtin_fields.keys()), default=default_fields)

# --- Custom Fields ---
st.markdown("### ➕ Add Custom Fields")
num_custom = st.number_input("Number of custom fields", 0, 10, 0)
custom_fields = []

for i in range(num_custom):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(f"Field {i+1} Name", key=f"name_{i}")
    with col2:
        datatype = st.selectbox(f"Data Type", ["Integer", "Float", "String"], key=f"type_{i}")
    if name:
        if datatype == "Integer":
            func = lambda: random.randint(1, 100)
        elif datatype == "Float":
            func = lambda: round(random.uniform(1.0, 100.0), 2)
        else:
            func = lambda: ''.join(random.choices(string.ascii_letters, k=8))
        custom_fields.append((name, func))

# --- Data Noise ---
st.markdown("### 🧬 Data Noise Configuration")
num_rows = st.slider("Number of Rows", 10, 10000, 1000, step=100)
add_duplicates = st.checkbox("Add Duplicate Rows", value=False)
duplicate_fraction = st.slider("Duplicate row fraction", 0.0, 1.0, 0.1, step=0.1) if add_duplicates else 0.0
null_percent = st.slider("Percentage of values to randomly nullify", 0, 50, 0, step=5)

# --- Generate Data ---
if st.button("🚀 Generate Fake Data"):
    if not selected_fields and not custom_fields:
        st.error("❌ Please select at least one built-in or custom column.")
    else:
        data = {}

        # Built-in
        for col in selected_fields:
            data[col] = [builtin_fields[col]() for _ in range(num_rows)]

        # Custom
        for name, func in custom_fields:
            data[name] = [func() for _ in range(num_rows)]

        df = pd.DataFrame(data)

        # Inject Nulls
        if null_percent > 0:
            for col in df.columns:
                df.loc[df.sample(frac=null_percent / 100).index, col] = None

        # Add Duplicates
        if add_duplicates and duplicate_fraction > 0:
            dup_count = int(len(df) * duplicate_fraction)
            duplicates = df.sample(n=dup_count, replace=True)
            df = pd.concat([df, duplicates], ignore_index=True)

        st.session_state["df"] = df
        st.success("✅ Fake data generated!")

# --- Display Section ---
if "df" in st.session_state:
    df = st.session_state["df"]

    st.dataframe(df, use_container_width=True)

    st.markdown("### 📥 Download")
    csv = df.to_csv(index=False)
    st.download_button("⬇️ CSV", csv, "fake_data.csv", "text/csv")

    excel = BytesIO()
    with pd.ExcelWriter(excel, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    excel.seek(0)
    st.download_button("⬇️ Excel", excel, "fake_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    json_data = df.to_json(orient="records", indent=2)
    st.download_button("⬇️ JSON", json_data, "fake_data.json", mime="application/json")

    st.markdown("### 📈 Summary")
    st.write(df.describe(include="all"))

    st.markdown("### 📊 Charts")
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include='object').columns

    if len(num_cols):
        col = st.selectbox("Numeric Chart", num_cols)
        st.bar_chart(df[col].value_counts().sort_index())

    if len(cat_cols):
        col = st.selectbox("Categorical Chart", cat_cols)
        st.bar_chart(df[col].value_counts())

    st.markdown("### 🔍 Search")
    q = st.text_input("Search text")
    if q:
        st.write(df[df.astype(str).apply(lambda x: x.str.contains(q, case=False)).any(axis=1)])

    st.markdown("### 🧠 Unique Values")
    for col in df.columns:
        st.markdown(f"**{col}** ({df[col].nunique()} unique)")
        st.code(df[col].dropna().astype(str).unique()[:10])

    st.markdown("### 💾 SQL Preview")
    tablename = st.text_input("Table Name", "fake_table")
    if tablename:
        sql_preview = "\n".join([
            f"INSERT INTO {tablename} ({', '.join(df.columns)}) VALUES ({', '.join(repr(x) for x in row)});"
            for row in df.head(10).values.tolist()
        ])
        st.code(sql_preview)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ by Vaibhav Rawat | Locale: `" + available_locales[locale] + "`")
