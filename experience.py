import streamlit as st
from PIL import Image
import base64

# video_file_bitquery = open('Bitquery-video.mp4', 'rb')
# video_bytes_bitquery = video_file_bitquery.read()

video_file_edumee = open('edumee-video.mp4', 'rb')
video_bytes_edumee = video_file_edumee.read()

def app():
	st.balloons()
	st.title("Some of my work experience")
	st.header("Deloitte")
	st.success('Incoming SFDC Engineer at Deloitte.')
	st.image(Image.open('DeloitteLogo.png')
# 	st.success('Currently working as a full-time Technical Support Engineer in Bitquery')
	st.header("Bitquery")
	st.write("Role: Technical Support Engineer")
# 	c1, c2, c3 = st.columns(3) 
# 	with c1:
# 		st.write("")
# 	with c2:
	st.image(Image.open('bitqueryLogo.jpg')
# 	with c3:
# 		st.write("")
	st.header("Bitquery")
	st.write("Role: Software Development Intern")
	colone, coltwo = st.columns(2)
	with colone:
# 		st.video(video_bytes_bitquery)
		st.image(Image.open('bitqueryLogo.jpg')
	# st.write("Role: Software Development Intern")
	with coltwo:
		st.image(Image.open('Internship Completion Certificate Bitquery Sayon Sai Dutta FINAL-signed-1.png'), caption='Bitquery Internship Completion Certificate')
	# displayPDF('Internship Completion Certificate Bitquery Sayon Sai Dutta FINAL-signed.pdf')
	st.header("Edumee")
	st.write("Role: Technical Content Writer Intern")
	col, coll = st.columns(2)
	with col:
		st.video(video_bytes_edumee)
	with coll:
		st.image(Image.open('edumee.jpg'), caption='Edumee Internship Completion Certificate')
	st.header("Deloitte")
	st.write("Role: Technical Consultancy Virtual Internship Experience")
	st.image(Image.open('Deloitte Virtual Internship Certificate-1.png'), caption='Deloitte Technical Consultancy Virtual Internship Experience Certificate')
	# displayPDF('Deloitte Virtual Internship Certificate.pdf')
