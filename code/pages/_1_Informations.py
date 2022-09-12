from Home_Page import *
from streamlit_SQLinterface import *

st.subheader("Special cafes information")

"""
**Cafes with the most features**
"""
st.table(most_features())

"""
**Cafes with highest mean rate**
"""

st.dataframe(highest_rate())

