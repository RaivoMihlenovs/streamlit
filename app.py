import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Analytics Dashboard")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Preview of Data")
    st.dataframe(df.head())
    
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if numerical_cols and categorical_cols:
        x_axis = st.selectbox("Select X-axis category:", categorical_cols)
        y_axis = st.selectbox("Select Y-axis numerical data:", numerical_cols)
        chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
        
        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} Trend by {x_axis}")
        else:
            fig = px.pie(df, names=x_axis, values=y_axis, title=f"{y_axis} Distribution by {x_axis}")
        
        st.plotly_chart(fig)
    else:
        st.warning("Ensure your dataset has both categorical and numerical columns for visualization.")
