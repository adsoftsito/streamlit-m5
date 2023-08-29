import streamlit as st
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


st.title('DSA05 - Análisis de deserción de empleados')


@st.cache
def filter_data_by_(column: str, value:any)-> pd.DataFrame:
    """Function to filter data."""
    if isinstance(value,np.int64) :
        filtered_data = data[data[column]==value]
        return filtered_data

    filtered_data = data[data[column].str.upper().str.contains(value)]
    return filtered_data


@st.cache
def load_data(nrows: int) -> pd.DataFrame:
    """Function to load data."""
    employees = pd.read_csv('Employees.csv', nrows=nrows)
    return employees


data_load_state = st.text('Loading Employees data...')
data = load_data(500)
data_load_state.text("Done!")

if st.sidebar.checkbox('Show all employees'):
    st.subheader('All Employees')
    st.write(data)

st.markdown("___")

employee_ID = st.sidebar.text_input('Search for Employee ID:')
btnEmployeeID = st.sidebar.button('Search ID')

if (btnEmployeeID):
    data_by_employee_ID = filter_data_by_('Employee_ID', employee_ID.upper())
    count_row = data_by_employee_ID.shape[0]  # Gives number of rows
    st.subheader('Employees by ID')
    st.write(f"Total Employees: {count_row}")
    st.write(data_by_employee_ID)

hometown = st.sidebar.text_input('Search for Hometown:')
btnHometown = st.sidebar.button('Search Hometown')

if (btnHometown):
    data_by_hometown = filter_data_by_('Hometown', hometown.upper())
    count_row = data_by_hometown.shape[0]  # Gives number of rows
    st.subheader('Employees by Hometown')
    st.write(f"Total Employees: {count_row}")
    st.write(data_by_hometown)

unit = st.sidebar.text_input('Search for Unit:')
btnUnit = st.sidebar.button('Search Unit')

if (btnUnit):
    data_by_unit = filter_data_by_('Unit', unit.upper())
    count_row = data_by_unit.shape[0]  # Gives number of rows
    st.subheader('Employees by Unit')
    st.write(f"Total Employees: {count_row}")
    st.write(data_by_unit)

st.markdown("___")

selected_edulvl = st.sidebar.selectbox(
    "Select Educational Level", data['Education_Level'].unique())

if selected_edulvl:
    data_by_edu_level = filter_data_by_('Education_Level', selected_edulvl)
    count_row = data_by_edu_level.shape[0]  # Gives number of rows
    st.subheader('Employees by Educational Level')
    st.write(f"Total Employees : {count_row}")
    st.write(data_by_edu_level)

st.markdown("___")


selected_hometown = st.sidebar.selectbox(
    "Select City", data['Hometown'].unique())

if selected_hometown:
    data_by_hometown = filter_data_by_('Hometown', selected_hometown.upper())
    count_row = data_by_hometown.shape[0]  # Gives number of rows
    st.subheader('Employees by City')
    st.write(f"Total Employees: {count_row}")
    st.write(data_by_hometown)

st.markdown("___")

selected_unit = st.sidebar.selectbox(
    "Select Unit", data['Unit'].unique())

if selected_unit:
    data_by_unit = filter_data_by_('Unit', selected_unit.upper())
    count_row = data_by_unit.shape[0]  # Gives number of rows
    st.subheader('Employees by Unit')
    st.write(f"Total Employees: {count_row}")
    st.write(data_by_unit)

st.markdown("___")

sns.set_theme(style="whitegrid", palette="husl")
sns.axes_style("whitegrid")


st.subheader('Histogram of Employee\'s Age')
fig, ax = plt.subplots()
hist_age = sns.histplot(x=data["Age"], ax=ax)
st.pyplot(fig)

st.subheader('Frequency of Employee\'s Unit')
fig, ax = plt.subplots()
employees_by_unit = data[['Employee_ID', 'Unit']].groupby('Unit').count()
employees_by_unit.rename(columns={'Employee_ID':'Count'}, inplace=True)
employees_frequency = employees_by_unit.plot.bar(ax=ax)
st.pyplot(fig)


st.subheader('Hometown\'s Desertion index')
fig, ax = plt.subplots()
employees_by_hometown = data.groupby('Hometown').mean(numeric_only=True)
employees_by_hometown["Attrition_rate"].plot(ax=ax)
st.pyplot(fig)


st.subheader('Age vs Attrition Rate  and Time of service vs Attrition rate')
fig, axs = plt.subplots(1,2, figsize=(10,10), sharex='col')
data[['Age', 'Attrition_rate']].plot.scatter(
    'Age',
    'Attrition_rate',
    ax = axs[0],
)

data[['Time_of_service', 'Attrition_rate']].plot.scatter(
    'Time_of_service',
    'Attrition_rate',
    ax = axs[1],
)
st.pyplot(fig)