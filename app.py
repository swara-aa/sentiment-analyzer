import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

st.title("🤖 AI-Powered Sentiment Analyzer")
st.write("Enter a sentence, and I'll tell you if it's Positive or Negative.")

text = st.text_area("Your Text")

if st.button("Analyze"):
    if text:
        result = sentiment_pipeline(text)[0]
        label = result['label']
        score = round(result['score'] * 100, 2)

        if label == "POSITIVE":
            st.success(f"🙂 Positive ({score}% confidence)")
        else:
            st.error(f"🙁 Negative ({score}% confidence)")
    else:
        st.warning("Please enter some text.")
