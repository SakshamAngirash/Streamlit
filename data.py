import streamlit as st
import pandas as pd
import numpy as np 
import time

a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape((2,4))
dic={
    "name":"saksham",
    "age":"21",
    "city":"solan"
}
data=pd.read_csv("Salary_Data.csv")
#print(data)

#st.dataframe(nd)
#st.dataframe(dic)
#st.dataframe(data,width=10000,height=20000)
st.dataframe(data)


#table: but it displays all the data
st.table(data)

#JSON
st.json(dic)

#write : can also be used to display data
st.write(data)


@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))    