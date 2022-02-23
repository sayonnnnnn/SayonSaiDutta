import streamlit as st
from PIL import Image

def app():
	st.balloons()
	st.title("My Education")
	col1, col2 = st.columns(2)
	with col1:
		st.header("Manipal University Jaipur")
		st.image(Image.open('muj_pic.jpeg'), caption='Manipal University, Jaipur')
	with col2:
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("Course: Bachelors of Technology")
		st.write("Branch: Computer & Communication Engineering")
		st.write("CGPA: 8.45")
		st.write("Year of passing out: 2023")
		# st.table(data={"Course": "Bachelors of Technology", "Branch": "Computer and Communication Engineering", "CGPA": "8.45"})
	# with col3:
	# 	st.write("")
	# with st.container():
	# 	st.image(Image.open('muj_pic.jpeg'), caption='Manipal University, Jaipur')
	col11, col22 = st.columns(2)
	with col11:
		st.header("Apeejay School, Pitampura")
		st.image(Image.open('apeejay.png'), caption='Apeejay School, Pitampura')
	with col22:
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("")
		st.write("Board: Central Board of Secondary Education")
		st.write("Branch: PCM with Computer Science")
		st.write("CGPA in class 10: 9.4")
		st.write("Percentage in class 12: 89.25%")
		st.write("Year of passing out: 2019")
		# st.table(data={"Board": "Central Board of Secondary Education CBSE", "Branch": "PCM with Computer Science", "Percentage": "89.25"})
	# with col33:
	# 	st.write("")


	