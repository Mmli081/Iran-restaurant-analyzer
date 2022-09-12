from Home_Page import *
from streamlit_SQLinterface import *

st.table(most_features())

st.write("\n\n")

st.markdown(
    """<style>
        .dataframe {text-align: right !important}
    </style>
    """, unsafe_allow_html=True)
st.dataframe(highest_rate())