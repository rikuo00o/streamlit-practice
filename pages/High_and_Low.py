import json
from pathlib import Path
import random
import streamlit as st
from models.High_and_Low_function import load_game_data

data = load_game_data()

st.title("High and Low Game!!")

if "chips" not in st.session_state:
    st.session_state.chips = data["initial_chips"]
if "deck" not in st.session_state:
    st.session_state.deck = data["deck"].copy()
if "round" not in st.session_state:
    st.session_state.round = 0

chips = st.session_state.chips
deck = st.session_state.deck
round_num = st.session_state.round

if round_num < len(data["rounds"]) and chips > 0:
    st.write(f"Round: {round_num + 1}")
    st.write(f"現在の所持金: {chips}")
    st.write(f"選ばれる数字の候補: {deck}")
    current_round = data["rounds"][round_num]
    base_card = random.choice(deck)
    st.write(f"ゲームマスターが引いたカード: {base_card}")

    player_choice = st.radio("次のカードの予想は?", ("High", "Drew", "Low"))
    bet = st.number_input("掛け金:", min_value=1, max_value=chips, step=1, value=10)

    if st.button("ファイナルアンサー"):
        if bet > chips:
            st.error("どうやってその掛け金を払うのだ？ 身の程を知れ！")
        else:
            result_card = current_round["result_card"]
            st.write(f"引かれたカード: {result_card}")

            if (player_choice == "High" and result_card > base_card) or (player_choice == "Low" and result_card < base_card) or (player_choice == "Drew" and result_card == base_card):
                st.success("おめでとう！ 掛け金は君のものだ！")
                chips += bet
                outcome = "win"
            else:
                st.error("残念！ 掛け金は私がもらうぞ！")
                chips -= bet
                outcome = "lose"
            deck.remove(result_card)
            round_num += 1
            st.session_state.chips = chips
            st.session_state.deck = deck
            st.session_state.round = round_num
            st.write(f"現在の所持金: {chips}")
            st.write(f"選ばれる数字の候補: {deck}")
        if st.button("Next Round"):
            st.experimental_rerun()

elif chips <= 0:
    st.write("所持金をすべて失いました、、、1050年地下行き!!!!!")
    st.button("Restart Game", on_click=lambda: st.session_state.update({"chips": data["initial_chips"], "deck": data["deck"].copy(), "round": 0}))

else:
    st.write("すべてのラウンドが終了しました！")
    st.write(f"Final Chips: {chips}")
    st.write("Thank you for playing!")
    st.button("Restart Game", on_click=lambda: st.session_state.update({"chips": data["initial_chips"], "deck": data["deck"].copy(), "round": 0}))