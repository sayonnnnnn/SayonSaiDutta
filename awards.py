import streamlit as st
from PIL import Image
def app():
	st.balloons()
	st.title("Awards and Certifications")
	st.subheader("Microsoft Azure AI Fundamentals AI-900")
	# st.image(Image.open('Microsoft_Certified_Professional_Certificate_0-1.png'), caption='Microsoft Azure AI Fundamentals AI-900')
	# st.markdown("<object data='/Microsoft_Certified_Professional_Certificate_0.pdf/' type='application/pdf' width='100%'></object>", unsafe_allow_html=True)
	st.image(Image.open('Microsoft_Certified_Professional_Certificate_0-1.png'), caption='Microsoft Azure AI Fundamentals AI-900')
	st.subheader("Google Digital Marketing Certification")
	st.image(Image.open('c3.jpeg'), caption='Google Digital Unlocked Digital Marketing Certification')
	st.subheader("Coursera Accolades")
	column1, column2 = st.columns(2)
	with column1: 
		st.image(Image.open('c1.jpeg'), caption='Python Basics University of Michigan')
	with column2:
		st.image(Image.open('c2.jpeg'), caption='How Google Does Machine Learning') 
		# st.markdown("![](https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~LSCD7ENV8B7F/CERTIFICATE_LANDING_PAGE~LSCD7ENV8B7F.jpeg)", unsafe_allow_html=True)
	column3, column4 = st.columns(2)
	with column3:
		st.image(Image.open('c4.jpeg'), caption='Relational Database Management System')
	with column4:
		st.image(Image.open('c5.jpeg'), caption='IBM Data Analysis with by Python')
	st.image(Image.open('coursera-1.png'))
	# st.markdown(!['My Github Repository']('https://github.com/sayonnnnnn'))
	st.write("Check out my Coursera accomplishments to find my other certifications [Click here](https://www.coursera.org/user/19266227ef7632bf42f81f3d1d208d8a)")