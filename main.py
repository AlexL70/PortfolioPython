import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./images/AlexL_pro.jpg")

with col2:
    st.title("Alex Levinson")
    content = """Hello.

I am an experienced and creative software developer. Passion is solutions’ quality, particularly in terms of high performance, irredundant and easily maintainable code. I like learning and trying new programming languages and technologies from time to time. I am also quite well at choosing an optimal way of resolving non-trivial issues.

My primary speciality at the moment is web-app development with C# and .Net. I have a thorough understanding of RDBMS principles, vast experience in Oracle and MS/SQL programming, and a firm grip on Microsoft ASP.Net stuff. I have some front-end development skills as well but do not feel it like my dominant direction. I prefer developing the back-end (DB and business logic) part, though I do not mind doing some front-end development unless it is too sophisticated.

I developed software for different areas of activity, including banking, billing & CRM, contract management, content management, online trading and software development tools.
    """
    st.info(content)

content2 ="""Below you can find some of the apps I have built using different programming languages and frameworks.

Please feel free to contact me."""
st.write(content2)