import json
from pathlib import Path
import random
import streamlit as st
from models.High_and_Low_function import load_game_data

data = load_game_data()

st.title("High and Low Game2")

st.write("Welcome to the High and Low card game!")

if "chips" not in st.session_state:
    st.session_state.chips = data["initial_chips"]
if "deck" not in st.session_state:
    st.session_state.deck = data["deck"].copy()
if "round" not in st.session_state:
    st.session_state.round = 0

chips = st.session_state.chips
deck = st.session_state.deck
round_num = st.session_state.round

st.write(f"Round: {round_num + 1}")
st.write(f"Current Chips: {chips}")
st.write(f"Remaining Deck: {deck}")

if round_num < len(data["rounds"]):
    current_round = data["rounds"][round_num]
    base_card = random.choice(deck)
    st.write(f"Base Card: {base_card}")

    player_choice = st.radio("Will the next card be Higher or Lower?", ("High", "Drew", "Low"))
    bet = st.number_input("Place your bet:", min_value=1, max_value=chips, step=1, value=10)

    if st.button("Guess"):
        if bet > chips:
            st.error("You cannot bet more chips than you have!")
        else:
            result_card = current_round["result_card"]
            st.write(f"The next card is: {result_card}")

            if (player_choice == "High" and result_card > base_card) or (player_choice == "Low" and result_card < base_card) or (player_choice == "Drew" and result_card == base_card):
                st.success("You guessed correctly!")
                chips += bet
                outcome = "win"
            else:
                st.error("Sorry, you guessed wrong.")
                chips -= bet
                outcome = "lose"
            deck.remove(result_card)
            round_num += 1
            st.session_state.chips = chips
            st.session_state.deck = deck
            st.session_state.round = round_num
            st.write(f"Chips after round: {chips}")
            st.write(f"Remaining Deck: {deck}")
        if st.button("Next Round"):
            st.experimental_rerun()

else:
    st.write("Game over! You've completed all rounds.")
    st.write(f"Final Chips: {chips}")
    st.write("Thank you for playing!")
    st.button("Restart Game", on_click=lambda: st.session_state.update({"chips": data["initial_chips"], "deck": data["deck"].copy(), "round": 0}))