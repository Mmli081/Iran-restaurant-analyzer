from streamlit_SQLinterface import *
from scipy.stats import chisquare

from sklearn.preprocessing import OrdinalEncoder
from scipy.stats import chisquare,chi2_contingency,chi2
import numpy as np
st.title('Realation between city and rate')
st.subheader('The null hypothesis (H0) :')
st.text('states that there is no relation between the variables.')
st.text('''we seperate our data and encode our categorial data using ordinal encoding and join it with the other data.
then we run a `chi2_contigency()` test on our new data and get the p-value to check our null hypothesis.
you can read more about this test in this [link](https://towardsdatascience.com/chi-square-test-with-python-d8ba98117626)
''')
city = read_to_df('cafe').city
city = np.array(city).reshape(-1,1)
rate = read_to_df('cafe_rating').iloc[:,1:6].mean(axis=1)
oh = OrdinalEncoder()
city = oh.fit_transform(city)[:,0]
# defining the table
data = [city, rate]
chi2, p, dof, ex = chi2_contingency(data)  
# interpret p-value
alpha = 0.05
st.subheader("p value is " + str(p))
st.title('Resault:')
if p <= alpha:
    st.text('Dependent (reject H0)')
else:
    st.text('Independent (H0 holds true)')