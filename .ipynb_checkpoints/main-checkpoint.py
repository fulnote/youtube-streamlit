import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

Image.open('sample.jpg')

img = Image.open('sample.jpg')
st.image(img, caption='background',use_column_width=True)


    # df  = pd.DataFrame(
    #     np.random.rand(100,2)/[50,50]+[35.69,139.70],
    #     columns=['lat','lon']
    # )

    # st.map(df)

