import pandas as pd
import streamlit as st
st.title("Student Dashboard")
df=pd.DataFrame({"name":["Alice","Bob","Charlie"],
                 "sales":[1000,3000,3500]})
st.subheader("Data Set")
st.dataframe(df)
min_sales=st.slider(
    "select sales range",
    1000,
    5000,
    0
)
filtered_df=df[df["sales"]>min_sales]

st.dataframe(filtered_df)   
chart_type=st.selectbox(
    "select chart type",
    ["line","bar"]
)

if chart_type=="line":
    st.line_chart(filtered_df.set_index("name"))
else:
    st.bar_chart(filtered_df.set_index("name"))