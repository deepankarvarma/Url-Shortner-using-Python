# Import the necessary libraries
import streamlit as st
import pyshorteners

# Create a streamlit app and add a text input for user
st.title("URL Shortener")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.pexels.com/photo/1103970/download/");
             background-attachment: fixed;
             background-color: transparent;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
     
url = st.text_input("Enter URL:")

# Add a button to submit the url and shorten it
if st.button("Shorten URL "):
    if not url:
        st.warning("Please enter a URL to shorten.")
    else:
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            st.success(f'Shortened URL: {short_url}')
        except pyshorteners.exceptions.BadURLException:
            st.error("Invalid URL. Please enter a valid URL.")
        except pyshorteners.exceptions.ShorteningErrorException:
            st.error("Error while shortening URL. Please try again later.")