import streamlit as st


st.title("Introduction")


"""
Welcome to our project
click on [link](https://github.com/Mmli081/Iran-restaurant-analyzer) to see our project on github
"""

st.title("Title with `st.title`")
st.header("Header with `st.header`")
st.subheader("Subheader with `st.subheader`")
st.caption('Caption (Usually for images or extra infos) with `st.caption`')
st.code("""
        print("Python Code with `st.code`")
        """)

st.code(
"""
#include <iostream>
int main(int argc, char **argv) {
    std:: cout << "QUERAA" << std::endl;
}
""", language="c++")

st.text("Normal text with `st.text`")

st.latex("f(x) = x ^ 2 + 2x + 1 = (x + 1) ^ 2")

"""
    in the background `st.write` or *magic* uses these methods to render your data 
    therefore we strongly suggest you to use **MAGIC**
    $$
    f(x) = x ^ 2 + 2x + 1 = (x + 1) ^ 2
    $$
"""
