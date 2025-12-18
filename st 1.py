import streamlit  as st
from textblob import TextBlob
st.sidebar.title("About us")
st.sidebar.text("""We Are Student At Ducat & Learning Machine Learning""")
st.sidebar.title("Contact Us")
st.sidebar.text("""hussainrao7599@gmail.com
aadilrao8445@gmail.com
asadrao9058@gmail.com""")

st.title("Sentiment Analysis Project")

text=st.text_input("**Enter Text**")
btn=st.button("predict")

if btn:
       blob=TextBlob (text)
       sent=blob.sentiment[0]
       if sent<0:
              st.error("Negative Sentiment")
              st.image("C:\\stream_programs\\neg_senti.png")
       elif sent>0:
              st.success("Positive Sentiment")
              st.image("C:\\stream_programs\\pos_senti.png")
       else:
              st.warning("Neutral Sentiment")
              st.image("C:\\stream_programs\\neut_senti.png")


