import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("Displaying & Plotting")

################################################################################

n = 100
x = np.linspace(-10, 10, n)
f = 5 #hz
noise = np.random.random(n) * 10

func_sin = 220 * np.sin(2 * np.pi * f * x) + noise
func_cos = 220 * np.cos(2 * np.pi * f * x) + noise
signals = pd.DataFrame({
    "t": x,
    "func_sin": func_sin,
    "func_cos": func_cos
}).set_index("t")

################################################################################

st.subheader("`st.line_chart`")
"""
+ interactive
+ easy & fast to use
"""
st.line_chart(
    data=signals,
    use_container_width=True
)

################################################################################

st.subheader("`st.area_chart`")
st.area_chart(
    data=signals,
    use_container_width=True
)

################################################################################

st.subheader("`st.bar_chart`")
sales_info = pd.DataFrame({
    "Product 1": np.random.randint(10, 100, 5),
    "Product 2": np.random.randint(10, 100, 5),
    "Product 3": np.random.randint(10, 100, 5),
}).set_index(pd.Index(["Jan", "Feb", "March", "April", "May"], name="Month"))
st.bar_chart(sales_info)

################################################################################

st.subheader("`st.pyplot`")
fig, axs = plt.subplots(1, 2, figsize=(15, 8), dpi=300)
axs[0].plot(x, func_sin)
axs[0].set_title(f"$f(t) = 220sin(2\pi{f}t)$")
axs[0].grid()

axs[1].plot(x, func_cos)
axs[1].set_title(f"$f(t) = 220cos(2\pi{f}t)$")
axs[1].grid()

st.pyplot(fig)

################################################################################

st.subheader("`st.map`")
df = pd.read_csv("datas/housing_data.csv", encoding="gbk")
df = df[["Lat", "Lng"]]
df.columns = ["lat", "lon"]
st.map(df)