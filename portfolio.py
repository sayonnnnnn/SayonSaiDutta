import streamlit as st
import awards
import about
import experience
import education
import projects
import base64

st.set_page_config (
    page_title="Sayon Sai Dutta",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed"
)

PAGES = {
	"About Me": about,
	"Education": education,	
	"Experience": experience,
	"Projects": projects,
	"Awards & Certification": awards
}

col_one, col_two, col_three = st.columns(3)
with col_one:
	st.write("")
with col_two:	
	st.title("SAYON SAI DUTTA")
with col_three:
	st.write("")
st.sidebar.title('SAYON SAI DUTTA')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()