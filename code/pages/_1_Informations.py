from Home_Page import *
from streamlit_SQLinterface import *

st.subheader("Special Cafes Information")

"""
**Cafes with the most features**
"""
st.table(most_features())

"""
**Cafes with highest mean rate (10 random sample)**
"""

st.table(highest_rate())

"\n\n"

col1, col2, col3 = st.columns(3)
col1.markdown("<p ><br><br><br>\
    Almost 18 percent of cafes start working from 9<br> \
    and 16 percent of them start at 8<br> \
    and so on...</p>", unsafe_allow_html=True)

col2.dataframe(work_start_p()[0])
col3.bar_chart(work_start_p()[1])


"\n\n"

col1, col2, col3 = st.columns(3)
col1.markdown("<p ><br><br><br>\
    Almost half of the cafes close at midnight<br> \
    and 26 percent of them close at 11:00 pm<br> \
    and so on...</p>", unsafe_allow_html=True)

col2.dataframe(work_end_p()[0])
col3.bar_chart(work_end_p()[1])

