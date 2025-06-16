# 🧪 FakeCSV Generator

A powerful and easy-to-use web tool to generate **realistic fake datasets** for testing, AI model training, analytics, and education — with support for **locale**, **categories**, **custom fields**, and **data export**.

![FakeCSV Banner](https://img.shields.io/badge/Built%20with-Streamlit-red?style=for-the-badge)  
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🔧 Features

- ✅ **Locale Support**: Generate data for different regions (India 🇮🇳, US 🇺🇸, France 🇫🇷, etc.)
- 🗃️ **Category Presets**: Auto-select relevant columns for E-commerce, Finance, Healthcare, etc.
- ✨ **Custom Fields**: Add your own fields with Integer, Float, or Random Strings
- 💫 **Data Noise**: Add duplicates and null values for real-world simulation
- 📊 **Built-in Charts**: Visualize numerical and categorical column distributions
- 🔍 **Search**: Quickly search values across the dataset
- 📁 **Export Options**: Download in CSV, Excel, and JSON formats
- 💾 **SQL Preview**: Generate SQL `INSERT` statements from your fake data

---

## 🚀 Getting Started

### 🖥️ Requirements

- Python 3.8+
- `pip install -r requirements.txt`

### 📦 Installation

```bash
git clone https://github.com/yourusername/fakecsv-generator.git
cd fakecsv-generator
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔍 Available Locales

- `en_US` – United States 🇺🇸  
- `hi_IN` – India 🇮🇳  
- `fr_FR` – France 🇫🇷  
- `de_DE` – Germany 🇩🇪  
- `ja_JP` – Japan 🇯🇵  

Powered by [`Faker`](https://faker.readthedocs.io).

---

## 📂 Built-in Field Types

| Category       | Fields Included |
|----------------|-----------------|
| Identity       | Full Name, First/Last Name, Email, Phone Number |
| Location       | Address, City, State, Country, Postal Code |
| Business       | Company, Job Title |
| Web & Tech     | Username, Password, URL, IPv4 |
| Date & Time    | Date, Time |
| Financial      | Credit Card Number |

---

## 🧪 Sample Use Cases

- Generate test data for **AI/ML Models**
- Create fake **user data** for front-end/backend testing
- Populate mock dashboards and databases
- Teach **data analysis and visualization**

---

## 📤 Exports & Integration

You can export your data to:
- ✅ CSV
- ✅ Excel (.xlsx)
- ✅ JSON
- ✅ SQL INSERT preview

---

## 🧠 Powered By

- [Streamlit](https://streamlit.io)
- [Faker](https://faker.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io)

---

## ✍️ Author

**Vaibhav Rawat**  
Access website here: https://fakecsvgenerator.streamlit.app/

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
