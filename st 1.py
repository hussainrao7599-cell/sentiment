import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis App", page_icon="😊")

st.title("Sentiment Analysis App")
st.write("Enter any text and check its sentiment")

# Text input
user_text = st.text_area("Enter your text here")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity

        st.subheader("Result")
        st.write(f"Polarity Score: {polarity}")

        if polarity > 0:
            st.success("Positive Sentiment 😊")
            st.image("pos_senti.png")
        elif polarity < 0:
            st.error("Negative Sentiment 😠")
            st.image("neg_senti.png")
        else:
            st.info("Neutral Sentiment 😐")
            st.image("neut_senti.png")
st.markdown("---")
st.caption("Built with Streamlit & TextBlob")




