import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.title("21信管李樱")
st.header("2109120108")


#文件上传
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    string_data = stringio.read()
    st.write(string_data)

    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

#图像可视化
st.title('图像可视化')
x = np.linspace(0, 10, 30)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)


#算法选择
data = pd.DataFrame({
    '第一列': np.random.randn(10),
    '第二列': np.random.rand(10)
})
st.dataframe(data)
genre = st.radio(
    "算法选择",
    ('+', '-', '*', '/'))

