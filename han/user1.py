import streamlit as st
import pandas as pd

## 위도와 경도 값을 가진 샘플 DataFrame 생성
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060]
})

# 강조하려는 포인트를 포함하는 DataFrame 생성
highlight = pd.DataFrame({
    'latitude': [37.7749],
    'longitude': [-122.4194]
})

# 강조 포인트를 지도에 추가
st.map(data)
