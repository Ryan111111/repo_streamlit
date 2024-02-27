import streamlit as st
import calendar

def generate_month_calendar(year, month):
    # 使用 calendar 模块生成指定年份和月份的日历
    cal = calendar.monthcalendar(year, month)
    
    # 创建一个空的二维列表来存储日历表格
    month_calendar = [[]]
    
    # 添加表头，即星期几的缩写
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    month_calendar[0].extend(week_days)
    
    # 将日历数据添加到表格中
    for week in cal:
        month_calendar.append(week)
    
    return month_calendar

# 指定年份和月份
year = 2024
month = 2

# 生成日历表格
month_calendar = generate_month_calendar(year, month)

# 在 Streamlit 应用中显示日历表格
st.write("## Monthly Calendar")
for week in month_calendar:
    st.write(week)
