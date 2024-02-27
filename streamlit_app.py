import streamlit as st
import calendar

# 获取当前年份和月份
year = st.sidebar.number_input("Year", min_value=1900, max_value=2100, value=2024)
month = st.sidebar.number_input("Month", min_value=1, max_value=12, value=1)

# 生成日历
cal = calendar.month(year, month)

# 在 Streamlit 中显示日历
st.write(f"## Calendar for {calendar.month_name[month]} {year}")
st.write(cal)

