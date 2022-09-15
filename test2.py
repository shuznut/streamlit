import streamlit as st
import pandas as pd
import numpy as np

Name = "Streamlit"

st.write("**Welcome**to ",Name)
# st.write(Name)

st.markdown('Streamlit is **_really_ cool**.')
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a string that explains something above.')

code ='''
def hello():
    print("Hello, Streamlit!")    
'''
st.code(code, language='python')

st.text('This is some text.')

#latex
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

# syntax: st.dataframe(data=None, width=None, height=None)
st.dataframe(df)
# same as : st.write(df)

#highlighting the maximum number within the column
# st.dataframe(df.style.highlight_max(axis=0))

# desired width and height in pixels
# st.dataframe(df, 200, 100)

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

st.balloons()
st.error('This is an error', icon="🧐")