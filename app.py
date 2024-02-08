import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

#importing data
data=pd.read_csv("Salary_Data.csv")
st.title("Salary Predictor")

nav=st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
x=np.array(data["YearsExperience"]).reshape(-1,1)

lr=LinearRegression()
lr.fit(x,np.array(data["Salary"]))

if nav=="Home":
    st.write("Home")
    st.image("https://cdn.pixabay.com/photo/2019/10/18/19/51/financial-4560047_640.jpg",width=800)
    if st.checkbox("Show Table"):
        st.table(data)
        
    graph=st.selectbox("Select the Type of Graph ",["Non Interactive","Interactive"])    
    val=st.slider("Years Filter",0,20)
    data=data.loc[data["YearsExperience"]>=val]
    
    if graph=="Non Interactive":
        # Create a figure and axes
        fig, ax = plt.subplots(figsize=(10,5))
        # Perform your plotting actions on the axes
        ax.scatter(data["YearsExperience"],data["Salary"])
        ax.set_ylim(0)
        ax.set_xlabel("Years Of Experience")
        ax.set_ylabel("Salary")
        # Pass the figure to st.pyplot()
        st.pyplot(fig)
        
    if graph=="Interactive":
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,210000])   
        )
        fig=go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"),layout=layout)
        st.plotly_chart(fig)
if nav=="Prediction":
    st.header("Know Your Salary")
    val=st.number_input("Enter Years of Experience",0.00,20.00,step = 0.25)
    val=np.array(val).reshape(1,-1)
    pred=lr.predict(val)[0]
    
    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")
    
    
    
if nav=="Contribute":
    st.header("Contribute to Our Dataset")
    ex=st.number_input("Enter Your Experience",0.00,20.00,step=0.25)
    sal=st.number_input("Enter Your Salary",0.00,10000000.00,step=1000.00)
    if st.button("SUBMIT"):
        to_add={"YearsExperience":[ex],"Salary":[sal]}  # Added brackets to make the values as lists
        to_add=pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a',header=False,index=False)  # Corrected here
        st.success("Submitted! Thankyou for the Contribution")











