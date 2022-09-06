from calendar import c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

st.title("Welcome to the first ever penguin database app")
st.write("**Starting** the *build* of 'penguin' app :penguin: :mag:")
st.write("**Starting** the *build* of 'penguin' app :penguin: :mag:")
st.write("Data is taken from [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/")
st.header("Data")

df = pd.read_csv("penguins_extra.csv")
st.write("Display a sample of 20 data points", df.sample(20))

species = st.selectbox(f"Select species", df.species.unique())
st.write(f"Displaying a sub data from {species}", df[df["species"] == species])

#heading over to the plotting
fig, ax = plt.subplots()

ax = sns.scatterplot(
    data = df, 
    x = "bill_length_mm", 
    y = "flipper_length_mm", 
    hue = "species") 
    
st.pyplot(fig)

st.bar_chart(df.groupby("island")["species"].count())
st.map(df)

csv_variable= st.sidebar.file_uploader("Upload a csv file", type=["csv"])
if csv_variable is not None:
    df=pd.read(csv_variable)
    st.write(df)