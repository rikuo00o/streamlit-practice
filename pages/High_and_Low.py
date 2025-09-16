import streamlit as st
import random

st.title("High and Low Game")

st.write("Welcome to the High and Low card game!")

if "win" not in st.session_state:
    st.session_state.win = 0

win = st.session_state.win

st.write(f"連勝数: {win}")

st.session_state.curent_player_card = st.session_state.get("curent_player_card", random.randint(1, 13))
curent_player_card = st.session_state.curent_player_card
st.write(f"Your current card is: {curent_player_card}")

guess = st.radio("Will the next card be Higher or Lower?", ("Higher", "Drew", "Lower"))
if st.button("Guess"):
    challenge_card = random.randint(1, 13)
    next_card = random.randint(1, 13)
    st.write(f"The next card is: {challenge_card}")

    if (guess == "Higher" and challenge_card > curent_player_card) or (guess == "Lower" and challenge_card < curent_player_card) or (guess == "Drew" and challenge_card == curent_player_card):
        st.success("You guessed correctly!")
        st.session_state.win += 1
        st.session_state.curent_player_card = next_card

    elif (challenge_card == curent_player_card) and (guess == "Higher" or guess == "Lower"):
        st.info("It's a tie!")
        st.session_state.win = 0
        st.session_state.curent_player_card = next_card

    else:
        st.error("Sorry, you guessed wrong.")
        st.session_state.win = 0 
        st.session_state.curent_player_card = next_card