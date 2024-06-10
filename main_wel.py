# import streamlit as st

# # Define the pages and their corresponding modules
# PAGES = {
#     "Government Account": "gov",
#     "Trade Account": "trade"
# }


# # Page selection using radio buttons
# selected_page = st.radio("Select a page:", list(PAGES.keys()))

# # Store the selected page in session state
# if 'page' not in st.session_state or st.session_state.page != selected_page:
#     st.session_state.page = selected_page

# # Dynamically import the selected page module
# page_module = __import__(PAGES[st.session_state.page])
# page_module.main()

import streamlit as st

# Define the pages and their corresponding modules
PAGES = {
    "Government Account": "gov",
    "Trade Account": "trade"
}

# Define the new pages
NEW_PAGES = {
    "I-Open": "new1",
    "Total Package Cost": "package_dashboard",
    "Cumulative Comparison of Costs": "cuyear_costs"
}

# Create three columns
col1, col2, col3 = st.columns([1,1,1])

# Page selection using radio buttons in the left column
selected_account = col1.radio("Type of Account:-", list(PAGES.keys()))

# New page selection using radio buttons in the right column
selected_dashboard = col3.radio("Dashboard:-", list(NEW_PAGES.keys()))

# Store the selected page in session state
if 'page' not in st.session_state or st.session_state.page != selected_account:
    st.session_state.page = selected_account

# Store the selected new page in session state
if 'new_page' not in st.session_state or st.session_state.new_page != selected_dashboard:
    st.session_state.new_page = selected_dashboard


if selected_dashboard=="I-Open":
    # Dynamically import the selected page module
    page_module = __import__(PAGES[st.session_state.page])
    page_module.main()

elif selected_dashboard=="Total Package Cost":
    new_page_module = __import__(NEW_PAGES[st.session_state.new_page])
    new_page_module.main()

else:
    new_page_module = __import__(NEW_PAGES[st.session_state.new_page])
    new_page_module.main()




# Dynamically import the selected new page module





# import streamlit as st

# # Define the pages and their corresponding modules
# PAGES = {
#     "Government Account": "gov",
#     "Trade Account": "trade"
# }

# # Page selection dropdown
# selected_page = st.selectbox("Select a page:", list(PAGES.keys()))

# # Store the selected page in session state
# if 'page' not in st.session_state or st.session_state.page != selected_page:
#     st.session_state.page = selected_page

# # Dynamically import the selected page module
# page_module = __import__(PAGES[st.session_state.page])
# page_module.main()


