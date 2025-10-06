import streamlit as st

st.title("カードゲームappへようこそ!!")

st.write("遊びたいゲームを選択してください(ゲームをクリックするとそのページに移動します)")
st.write("ゲーム一覧")
st.page_link("pages/High_and_Low.py", label="🎮 High and Low", icon="🃏")
st.write("現在High and Lowのみ実装。気が向いたら他のゲームも順次追加予定です。")

st.markdown('[遊び方(外部ページ)](https://rikuo00o.github.io/streamlit-practice/latest/)', unsafe_allow_html=True)