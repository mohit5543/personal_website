import streamlit as st
from streamlit_option_menu import option_menu
import requests

# page setup
st.set_page_config(page_title="My Portfolio", page_icon="⭐", layout="wide")

# Navigator
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Portfolio", "Contact"],
    icons=["house", "person", "code-slash", "envelop"],
    orientation="horizontal",
)

# Sections
if selected == "Home":
    st.title("Welcome to my digital space")
    st.write("I am a developer focused on python and creative coding.")
    #Add a call to action
    if st.button("Check my GitHub"):
        st.info("Navigate to the Portfolio section above!")

elif selected == "About":
    st.title("About me")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Techinical Skills")
        st.write("- Python & Streamlit")
        st.write("- PC Hardware & Customization")
    with col2:
        st.write("### Current goals")
        st.write("- Current Typing speed goal: 100+ WPM")

elif selected == "Portfolio":
    st.title("GitHub Projects")
    username = "mohit5543"
    try:
        response = requests.get(f"https://api.github.com/users/{username}/repos")
        repos = response.jason()
        for repo in reposp[:5]:
            with st.container():
                st.subheader(repo["name"])
                st.write(repo["description"])
                st.markdown(f"[View on GitHub]({repo['html_url']})")
    except:
        st.error("Failed to load github data.")

elif selected == "Contact":
    st.title("Get in touch")
    with st.form("contact"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        if st.form_submit_button("Submit"):
            st.success("Thank you for reaching out! I'll get back to you soon.")

