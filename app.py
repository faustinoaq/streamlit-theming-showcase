import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import time

# Global settings

title = "Streamlit Theme showcase"

st.set_page_config(page_title=title, initial_sidebar_state="collapsed")

st.title(title)

# Custom CSS

st.markdown("""<style>
header {visibility: hidden;}
</style>""", unsafe_allow_html=True)

# Widgets

st.write("""
Hello *world!* :sunglasses: See source in [Github](https://github.com/faustinoaq/streamlit-theming-showcase).
""")

with st.popover("More info"):
    st.write("This is a popover")
    st.link_button("🎈 Streamlit", "https://www.streamlit.io/")
    st.toast("You opened more info!", icon="😁")
    st.toast("Check the [link](https://www.streamlit.io/)!", icon="🎈")

x, y = st.tabs(["📈 Chart", "🧾 Data"])

data = np.cumsum(np.random.randn(100, 10), 0).round(2)

pets = ["Cat", "Dog", "Bird", "Fish", "Rabbit", "Turtle", "Jiraffe", "Lion", "Elephant", "Monkey"]

df = pd.DataFrame(data, columns=pets)

x.subheader("A tab with a chart",divider='rainbow')
x.bar_chart(df)

y.subheader("A tab with a dataframe")
y.dataframe(df)

d, e = st.columns((4,3))

file = d.file_uploader("Pick a file")

options = ["1 balloon 🎈", "2 balloons 🎈🎈", "3 balloons 🎈🎈🎈"]
e.radio("How many balloons?",options)

a, b, c = st.columns((3,1, 3))

number = a.slider("Pick a number", 0, 100, 37)

color = b.color_picker("Pick a color", value="#478AFF")

date = c.date_input("Pick a date", value=pd.to_datetime("1970-01-01"))


st.write(
"""
### Example Widgets

These widgets don't do anything. But look at all the these cool things! 👀 

```python
# First some code.
streamlit = "cool"
theming = "fantastic"
both = "😊"
```
"""
)

with st.form(key='my_form'):
    st.checkbox("Is this cool or what?")
    
    j, k = st.columns(2)

    with j:
        st.text_input("Username", placeholder="User name here")

    with k:
        st.text_input("Password", placeholder="Type something...", type="password")
    
    f, g = st.columns(2)

    with f:
        st.number_input("So many numbers", 0, 100, 37)

    with g:
        st.selectbox(
            "My favorite thing in the world is...",
            ["Streamlit", "Theming", "Baloooons 🎈 "]
        )

    submit_button = st.form_submit_button(label='Submit')

p, q, r = st.columns(3)
p.metric("Temperature", "70 °F", "1.2 °F")
q.metric("Wind", "9 mph", "-8%")
r.metric("Humidity", "86%", "4%")

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.text_area("A little writing space for you :)", placeholder="Write something...")

m, n, o  = st.columns(3)

m.button("😊 Click me", )

n.button("🤔 Click me", disabled=True, help="This is disabled")

o.button("😁 Another", type="primary", help="This is primary")

st.write("""### A bit of illustrated text content

[Streamlit](https://streamlit.io/) is an open-source [Python](https://www.python.org/) framework that makes it easy to create beautiful,
interactive data apps. With [Streamlit](https://streamlit.io/), you can turn your data analysis scripts into
shareable web applications with just a _few lines of code_.""")

h, i = st.columns((4,2))

h.write("""[Streamlit](https://streamlit.io/) provides a simple and intuitive API that allows you to quickly build and
customize your data apps. You can easily add interactive widgets, charts, tables,
and text to create a rich and engaging user interface.

One of the key features of [Streamlit](https://streamlit.io/) is its ability to automatically update the app
whenever the underlying code or data changes. This makes it incredibly efficient for
iterative development and real-time data exploration. [Streamlit](https://streamlit.io/) also supports seamless integration
with popular data libraries like `pandas`, `altair`, and `numpy`, allowing you to leverage their power and
flexibility in your apps. You can easily load and manipulate data, create interactive visualizations,
and perform complex calculations with just a few lines of code.""")

i.image("python.png", caption="Python logo")

st.write("""Whether you're a **data scientist**, **machine learning engineer**, or **data enthusiast**,
[Streamlit](https://streamlit.io/) empowers you to quickly prototype and deploy data apps without the need for extensive web development knowledge.
Its simplicity and ease of use make it a favorite tool among data professionals.

So, if you're looking to create stunning and interactive data apps with [Python](https://www.python.org/), give [Streamlit](https://streamlit.io/) a try.
You'll be amazed at how quickly you can bring your ideas to life and share them with others.
""")

s = st.expander("Help!!!")
s.help()

st.sidebar.title("Settings")

# Sidebar widgets

st.sidebar.warning("This is a warning")

with st.sidebar.status("Checking test..."):
    st.write("Searching for test...")
    time.sleep(2)
    st.write("Found test.")
    time.sleep(1)
    st.write("Downloading test...")
    time.sleep(1)

on = st.sidebar.toggle('Activate feature')

if on:
    st.sidebar.write('Feature activated!')
else:
    st.sidebar.write('Feature deactivated!')
