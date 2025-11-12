import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search For Happiness")

xaxis = st.selectbox("Select data for x-axis",
                      ("gdp","happiness","generosity"))

yaxis = st.selectbox("Select data for y-axis",
                      ("gdp","happiness","generosity"))


st.title(f"{xaxis} and {yaxis}")

df = pd.read_csv("happy.csv")

def getdata():
    first_pick = df[xaxis]
    second_pick = df[yaxis]
    return first_pick, second_pick

first_pick, second_pick = getdata()

graph = px.scatter(x=first_pick,y=second_pick,labels={'x':xaxis,'y':yaxis})
st.plotly_chart(graph)




