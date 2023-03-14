import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer


# To add more files/content in dairy.
st.title("Analyze the emotion of your days")
date_of_content = st.date_input(label="Select the date you want to add content on your dairy")
content = st.text_input("Enter Your daily musings...")

if len(content) > 10:
    with open(f"dairy/{date_of_content}.txt", "w") as file:
        file.write(content)

# Create a list of filepath using glob
filepaths = sorted(glob.glob("dairy/*.txt"))

analyzer = SentimentIntensityAnalyzer()

pos_list = []
neg_list = []

for filepath in filepathse:
    with open(filepath, "r") as file:
        content_local = file.read()
    result = analyzer.polarity_scores(content_local)
    pos_list.append(result["pos"])
    neg_list.append(result["neg"])

date_list = [name.strip(".txt").strip("dairy/") for name in filepaths]

fig1 = px.line(y=pos_list, x=date_list, labels={"y":"Positive Score", "x":"Date"})
st.plotly_chart(fig1)

fig2 = px.line(x=date_list, y=neg_list, labels={"x":"Date", "y":"Negative Score"})
st.plotly_chart(fig2)