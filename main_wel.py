import streamlit as st

# Define the pages and their corresponding modules
PAGES = {
    "Government Account": "gov",
    "Trade Account": "trade"
}


# Page selection using radio buttons
selected_page = st.radio("Select a page:", list(PAGES.keys()))

# Store the selected page in session state
if 'page' not in st.session_state or st.session_state.page != selected_page:
    st.session_state.page = selected_page

# Dynamically import the selected page module
page_module = __import__(PAGES[st.session_state.page])
page_module.main()
