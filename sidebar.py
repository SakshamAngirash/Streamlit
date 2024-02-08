import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import time

data={
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
#navigation bar
rad=st.sidebar.radio("Navigation",["home","about us"])

if rad=="home":
    df=pd.DataFrame(data=data)
    call=st.sidebar.selectbox("Number",[1,2,3,4,5])
    #actual use case 
    col=st.sidebar.selectbox("Column",df.columns)
    plt.plot(df["num"],df[col])
    st.pyplot()

if rad=="about us":
    
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
        
    st.balloons()
        
    st.write("about us is nothing special")
    st.error("error")
    st.success("yaayy")
    st.info("Information")
    st.exception(RuntimeError("this is a runtime error"))
    st.warning("this is a warning")



