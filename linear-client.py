import streamlit as st
import requests
import numpy as np
import tensorflow as tf

url = 'https://tensorflow-linear-model-fvap.onrender.com/v1/models/linear-model:predict'

def predict():
  x = np.array([
    [1.0],
    [2.0],
    [3.0],
    [4.0]
  ], dtype=np.float32)
  
  data = {'instances': x.tolist()}
  response = requests.post(url, json=data)
  
  print(response.text)
  return response


st.title('Linear model client')
st.write('y = 2.0x + 1')


data = st.text_input('0, 1, 2')
btnPredict = st.button('Predict')

if (btnPredict):
   prediction = predict()
   st.write(prediction)
   st.write(prediction.text)


hello = tf.constant("hello  tensorflow world")
print(hello)

# to acces a Tensor value, call numpy()
st.write(hello.numpy())

