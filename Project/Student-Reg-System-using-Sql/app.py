import streamlit as st
import mysql.connector
import pandas as pd

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Employee Management System", page_icon="👨‍💼", layout="wide")

# ------------------- CUSTOM CSS -------------------
st.markdown("""
    <style>
    /* Global */
    body {
        font-family: 'Segoe UI', sans-serif;
        background: #f5f7fa;
        color: #2c3e50;
    }
    .stApp { background: #f5f7fa; }

    /* Title */
    .main-title {
        font-size: 32px;
        font-weight: 600;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 30px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;  /* white sidebar */
        border-right: 1px solid #e0e0e0;
        padding-top: 20px;
    }
    .sidebar-title {
        font-size: 20px;
        font-weight: 600;
        color: #2563eb; /* corporate blue */
        text-align: center;
        margin-bottom: 20px;
    }
    .sidebar-menu {
        font-size: 16px;
        font-weight: 500;
        color: #374151;
        padding: 10px 16px;
        border-radius: 6px;
        cursor: pointer;
        margin-bottom: 8px;
        transition: all 0.2s ease;
    }
    .sidebar-menu:hover {
        background-color: #f3f4f6;
        color: #2563eb;
    }
    .sidebar-selected {
        background-color: #2563eb !important;
        color: white !important;
    }

    /* Card */
    .card {
        background: white;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 15px;
        color: #2c3e50;
        border-left: 4px solid #2563eb;
        padding-left: 10px;
    }

    /* Inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        height: 38px;
        font-size: 15px;
        border-radius: 6px;
        border: 1px solid #ccc;
    }

    /* Buttons */
    .stButton > button {
        background: #2563eb;
        color: white;
        border-radius: 6px;
        padding: 8px 18px;
        font-size: 15px;
        font-weight: 500;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background: #1d4ed8;
    }

    /* Table */
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }
    th {
        background: #2563eb;
        color: white;
        padding: 10px;
        text-align: left;
    }
    td {
        padding: 10px;
        border-bottom: 1px solid #e0e0e0;
    }
    tr:nth-child(even) { background: #f9f9f9; }
    tr:hover { background: #eef4ff; }
    </style>
""", unsafe_allow_html=True)

# ------------------- DATABASE CONNECTION -------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Adnan@1521",
        database="webui"
    )

# ------------------- FETCH DATA -------------------
def fetch_data():
    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT emp_id, name, mobile, salary FROM employees")
    rows = cursor.fetchall()
    con.close()
    return pd.DataFrame(rows, columns=["Employee ID", "Name", "Mobile", "Salary"])

# ------------------- ADD EMPLOYEE -------------------
def add_employee(empid, name, mobile, salary):
    try:
        con = connect_db()
        cursor = con.cursor()
        query = "INSERT INTO employees (emp_id, name, mobile, salary) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (empid, name, mobile, salary))
        con.commit()
        con.close()
        st.success("✅ Employee added successfully!")
    except Exception as e:
        st.error(f"❌ Database Error: {e}")

# ------------------- UPDATE EMPLOYEE -------------------
def update_employee(old_empid, empid, name, mobile, salary):
    try:
        con = connect_db()
        cursor = con.cursor()
        query = "UPDATE employees SET emp_id=%s, name=%s, mobile=%s, salary=%s WHERE emp_id=%s"
        cursor.execute(query, (empid, name, mobile, salary, old_empid))
        con.commit()
        con.close()
        st.success("✅ Employee updated successfully!")
    except Exception as e:
        st.error(f"❌ Database Error: {e}")

# ------------------- DELETE EMPLOYEE -------------------
def delete_employee(empid):
    try:
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("DELETE FROM employees WHERE emp_id=%s", (empid,))
        con.commit()
        con.close()
        st.warning(f"🗑️ Employee {empid} deleted successfully!")
    except Exception as e:
        st.error(f"❌ Database Error: {e}")

# ------------------- STREAMLIT UI -------------------
st.markdown('<div class="main-title">👨‍💼 Employee Management System</div>', unsafe_allow_html=True)

# Sidebar menu
st.sidebar.markdown('<div class="sidebar-title">📂 Navigation</div>', unsafe_allow_html=True)
menu = st.sidebar.radio("", ["Add Employee", "View Employees"])

if menu == "Add Employee":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">➕ Register New Employee</div>', unsafe_allow_html=True)
    with st.form("emp_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            empid = st.text_input("Employee ID")
            name = st.text_input("Name")
        with col2:
            mobile = st.text_input("Mobile")
            salary = st.number_input("Salary", min_value=0.0, step=100.0)
        submitted = st.form_submit_button("Submit")

        if submitted:
            if empid and name and mobile and salary:
                add_employee(empid, name, mobile, salary)
            else:
                st.error("⚠️ Please fill all fields!")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "View Employees":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Employee Records</div>', unsafe_allow_html=True)
    df = fetch_data()

    if not df.empty:
        st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

        selected_emp = st.selectbox("Select Employee to Edit/Delete", df["Employee ID"])
        selected_row = df[df["Employee ID"] == selected_emp].iloc[0]

        st.markdown('<div class="section-title">✏️ Update Employee Info</div>', unsafe_allow_html=True)
        with st.form("update_form"):
            col1, col2 = st.columns(2)
            with col1:
                new_id = st.text_input("Employee ID", value=selected_row["Employee ID"])
                new_name = st.text_input("Name", value=selected_row["Name"])
            with col2:
                new_mobile = st.text_input("Mobile", value=selected_row["Mobile"])
                new_salary = st.number_input("Salary", value=float(selected_row["Salary"]))
            
            update_btn = st.form_submit_button("Update Employee")
            if update_btn:
                update_employee(selected_row["Employee ID"], new_id, new_name, new_mobile, new_salary)

        st.markdown('<div class="section-title">🗑️ Delete Employee</div>', unsafe_allow_html=True)
        if st.button(f"Delete {selected_row['Name']}"):
            delete_employee(selected_row["Employee ID"])
    else:
        st.info("No employees found. Please add some.")

    st.markdown('</div>', unsafe_allow_html=True)
