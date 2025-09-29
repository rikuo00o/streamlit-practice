import json
from pathlib import Path
import random

def load_game_data():
    # ----Pathを指定して JSONファイルを読み込み ----
    json_path = Path(__file__).parent.parent / "sample_data" / "highlow_round3.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def jugde_guess(guess, base_card, result_card):
    if (guess == "High" and result_card > base_card) or (guess == "Low" and result_card < base_card) or (guess == "Drew" and result_card == base_card):
        return True
    else:
        return False