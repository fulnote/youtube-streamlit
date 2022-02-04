import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.expander('問い合わせ')
expander.write('問い合わせをかく')

# text = st.text_input('あなたが好きな趣味を教えて下さい')
# condition= st.slider('あなたの調子は？',1,100,50)

# 'あなたの趣味:', text
# 'コンディション:', condition


# if st.checkbox('show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='background',use_column_width=True)

