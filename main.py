import streamlit as st
import langchain_helper

st.title("Learning Helper for CBSE Class XI")

subject = st.sidebar.selectbox("Pick your subject", ("maths", "physics","chemistry"))
#st.sidebar.t

if subject:
    response = langchain_helper.generate_subject_help_links(subject)
    st.header(f'Helpful Links for {subject}')
    helpful_links = response['helpful_links'].strip().split(",")
    for link in helpful_links:
        st.write(link)

