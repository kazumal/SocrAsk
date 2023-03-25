import codecs
import streamlit as st

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = ""
CONTACT_EMAIL = ""
PRODUCT_NAME = "SocrAsk"
PRODUCT_TAGLINE = "Unlock Your Learning Potential"
PRODUCT_DESCRIPTION = """
SocraticStudy is an innovative educational app that empowers students to delve deeper into their studies in an interactive and engaging manner, similar to the Socratic Method. By utilizing the advanced ChatGPT API, students can choose from a wide range of subjects such as math, science, and social studies to begin their self-paced learning journey. The app is designed to encourage critical thinking, problem-solving, and a true understanding of the subject matter.
"""

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- CSS ---
def load_css(file):
    with codecs.open(file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("./styles/Home.css")

# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
st.text("")
st.write(PRODUCT_DESCRIPTION)

# --- FEATURES ---
st.write("")
st.write("---")
st.subheader(":rocket: Features")
features = {
}
for image, description in features.items():
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo")


# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1": "Some text goes here to answer question 1",
    "Question 2": "Some text goes here to answer question 2",
    "Question 3": "Some text goes here to answer question 3",
    "Question 4": "Some text goes here to answer question 4",
    "Question 5": "Some text goes here to answer question 5",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


# --- CONTACT FORM ---
# video tutorial: https://youtu.be/FOULV9Xij_8
st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)