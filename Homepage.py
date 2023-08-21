import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title="Medical AI Interviewer", layout="centered", page_icon=im)

lan = st.selectbox("#### Language", ["English", "中文"])

if lan == "English":
    home_title = "Medical AI Interviewer"
    home_introduction = "Welcome to the Medical AI Interviewer, empowering your medical history assessment with generative AI."
    
    # ... [rest of the code remains the same] ...

    st.markdown("Welcome to the Medical AI Interviewer! 👏 This AI tool is designed to ask you medical-related questions to gather a comprehensive medical history.")
    
    # ... [rest of the code remains the same] ...

    st.markdown("#### Get started!")
    st.markdown("Select one of the following categories to start your medical assessment!")
    
    selected = option_menu(
        menu_title=None,
        options=["General Health", "Uro-Genital", "Cardiovascular", "Customize!"],
        icons=["heartbeat", "user-md", "stethoscope"],
        default_index=0,
        orientation="horizontal",
    )
    
    # ... [rest of the code remains the same] ...

    if selected == 'General Health':
        st.info("""
            📚In this session, the Medical AI Interviewer will assess your general health.
            Note: The maximum length of your answer is 4097 tokens!
            - Each assessment will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your preferred interaction style (chat/voice)
            - Start by introducing yourself and enjoy！ """)
        if st.button("Start Assessment!"):
            switch_page("General Health Screen")
    
    # ... [rest of the code remains the same] ...

    st.markdown("#### Wiki")
    st.write('[Click here to view common FAQs, future updates, and more!](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')

# ... [rest of the code remains the same for the '中文' section, but translated to fit the medical context] ...
