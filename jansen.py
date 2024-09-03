import streamlit as st
import base64

st.title("My Autobiography and Portfolio")

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to", ["Home", "About Me", "Portfolio", "Contact"])

if option == "Home":
    st.header("Welcome to My Personal Space!")
    st.write("""
    Hello! I'm glad you're here. In this space, I share a bit about myself and my educational background. Feel free to explore!
    """)

elif option == "About Me":
    st.header("About Me")
    st.subheader("A Little Background")
    st.write("""
    Hi, I'm Jansen Paul S. Amper, a 4th-year BS-IT student at CIT-U with a passion for software development. I started my journey in Information Technology 5 years ago, and since then, I've been dedicated to learning and growing in this field.
    """)

    st.subheader("My Journey")
    st.write("""
    - **Born and raised** in Cebu City, I have always been curious about computers.
    - **Education**:  I pursued my Bachelor of Science in Information Technology (BS-IT) at CIT-U
    - **Personal Life**: In my free time, I enjoy playing computer games.
    """)

    st.subheader("Skills")
    st.write("""
    - **Programming**: C/C++, Python, JavaScript, HTML/CSS
    - **Frameworks**: Django, Streamlit, React
    - **Tools**: Git, SQL
    """)

elif option == "Portfolio":
    st.header("My Portfolio")
    st.subheader("Resume")
    with open("Amper, Jansen Paul S..pdf", "rb") as file:

        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
        
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        
        st.markdown(pdf_display, unsafe_allow_html=True)

    st.write("You can also download my resume by clicking the button below:")
    with open("Amper, Jansen Paul S..pdf", "rb") as file:
        btn = st.download_button(label="Download Resume", data=file, file_name="Jansen_Paul_Amper_Resume.pdf", mime="application/pdf")

elif option == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Thank you {name}! I'll get back to you at {email} soon.")
    
    st.subheader("Social Media")
    st.write("""
    - **Facebook**: [Jansen Seno](https://www.facebook.com/Jansensensensen)
    """)
