import streamlit as st 
st.title("Widgets")

#button 
if st.button("say hello"):
    st.write("hello world")
    
#textbox
name=st.text_input("Name") 
st.write(name)       

#textarea
address=st.text_area("Enter your address: ")
st.write(address)

#date and time
st.date_input("Enter a date")
st.time_input("time")


#checkbox
if st.checkbox("you accept",value=False):
    st.write("thankyou")
    

#radio button 
st.radio("Colours",["red","green","BLUE"],index=1)

#select box
st.selectbox("Colours",["red","green","BLUE"],index=1)


#multiselect
st.multiselect("Colours",["red","green","BLUE"])

#slider
st.slider("age",min_value=18,max_value=60,step=2)

#Number
st.number_input("numbers",min_value=10.0,max_value=20.0,value=15.0,step=1.0)

#file uplaoder

file_upload=st.file_uploader("upload a file")
st.write(file_upload)