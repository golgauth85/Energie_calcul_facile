import streamlit as st






pg = st.navigation([
    st.Page("Home.py", title="Home", icon="🏠"),  # Page d'accueil
    # st.Page("page1.py", title="Page 1", icon="🔥"),
    # st.Page("page2.py", title="Page 2", icon=":material/favorite:"),
])

pg.run()



