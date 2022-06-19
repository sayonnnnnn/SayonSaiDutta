import streamlit as st
from PIL import Image
import streamlit.components.v1 as components 

def app():
	st.balloons()
	st.title("These are some of my projects")
	st.image(Image.open('github-profile.png'), caption='My Github Profile')
	
	st.subheader("Cryptocurrency Charting Application with Tradingview and Bitquery GraphQL API ")
	st.write("Tradingview which is one of the most popular charting applications used by Stock Market analysts does not support Cryptocurrency data. In order to place cryptocurrency data in Tradingview, the data has to processed in OHLC format and then the charting is shown. The Chart rendered by Tradingview's widget along with the data passed on by Bitquery GraphQL API shows the data for the Binance Smart Chain Mainnet's latest prices in the Ethereum blockchain. The data is represented in the Candlestick format.")
	st.image(Image.open('projects1.png'))
	st.write("Github Repository: [https://github.com/sayonnnnnn/CryptoCurrency_Charts_With_Tradingview](https://github.com/sayonnnnnn/CryptoCurrency_Charts_With_Tradingview)")
	
	st.subheader("Open Source Intrusion Detection System")
	st.write("CIDS is an open source Intrusion Detection system which makes use RandomForestClassifier in differenciating between different types of intrusion attacks based upon a real world dataset. It has an accuracy of 98%.")
	co1, co2 = st.columns(2)
	with co1:
		st.image(Image.open('projects2-1.png'))
	with co2:
		st.image(Image.open('projects2-2.png'))
	co3, co4 = st.columns(2)
	with co3:
		st.image(Image.open('projects2-3.png'))
	with co4:
		st.image(Image.open('projects2-5.png'))
	st.write("Github Repository: [https://github.com/sayonnnnnn/C-IDS-OPEN-SOURCE](https://github.com/sayonnnnnn/C-IDS-OPEN-SOURCE)")
	
	st.subheader("SocketChat")
	st.write("SocketChat is chat application made using NodeJS and Socket.io keeping vanilla JS as the frontend.")
	co5, co6 = st.columns(2)
	with co5:
		st.image(Image.open('projects3-1.png'))
	with co6:
		st.image(Image.open('projects3-2.png'))
	st.write("Github Repository: [https://github.com/sayonnnnnn/SocketChat](https://github.com/sayonnnnnn/SocketChat)")

	st.subheader("Gift Recommendation System")
	st.write("Gift Recommendation System has a set of gifts meant for people above the age of 18 and some for people below the age of 18 in it's SQLite database. The Flask microservice operates a CRUD application along with specifying the type of gifts based upon the user's age.")
	co7, co8, co9 = st.columns(3)
	with co7:
		st.image(Image.open('projects4-1.png'))
	with co8:
		st.image(Image.open('projects4-2.png'))
	with co9:
		st.image(Image.open('projects4-3.png'))
	st.write("Github Repository: [https://github.com/sayonnnnnn/RDBMS_PROJECT](https://github.com/sayonnnnnn/RDBMS_PROJECT)")

	st.subheader("GiftShop Maker JavaFX")
	st.write("GiftShop Maker is a desktop application made using Java and JavaFX to generate the UI.")
	st.image(Image.open('projects5.png'))
	st.write("Github Repository: [https://github.com/sayonnnnnn/JavaFX-Giftshop-Maker](https://github.com/sayonnnnnn/JavaFX-Giftshop-Maker)")

	st.subheader("Flutter Hostel Management App")
	st.write("This is an Android Application made for Hostlers of MUJ so that they can avail benefits of applying Online request for Out Pass and Guest Room Booking Approvals. Students can also get information about Mess Menu from the app itself. In Similar Fashion Hostel Authority can also manage student requests on this app and take decision accordingly which help them reduce paper work and enable to maintain proper records as well.")
	st.write("Github Repository: [https://github.com/sayonnnnnn/Flutter-Hostel-Management-App](https://github.com/sayonnnnnn/Flutter-Hostel-Management-App)")

# 	components.iframe("https://github.com/sayonnnnnn")
	st.image(Image.open('icons8-github-48.png'))
	st.write("Check out my [Github Repository](https://github.com/sayonnnnnn) for other projects")
