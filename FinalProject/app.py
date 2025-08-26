import streamlit as st

page_main = st.Page("main.py", title="Main Page", icon="🎈")
page_4 = st.Page("p4.py", title="Page 4", icon="❄️")


page = st.navigation([page_main, page_4])

page.run()