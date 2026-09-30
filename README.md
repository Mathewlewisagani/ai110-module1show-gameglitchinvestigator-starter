# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.** It's a number guessing game built with Streamlit. The game picks a secret number in a range based on difficulty (Easy 1–20, Normal 1–100, Hard 1–50), and you get a limited number of attempts to guess it. After each guess it tells you to go higher or lower and updates your score.
- [x] **Detail which bugs you found.**
  - The hints were backwards. A guess that was too high told me to go HIGHER.
  - On every even attempt the secret was turned into a string, so the game compared text instead of numbers. With a secret of 21, a guess of 99 said "go higher" but 100 said "go lower", because "100" comes before "21" as text.
  - The New Game button didn't work after a loss. It reset the attempts and the secret but not the game status, so the game stayed "over".
  - Attempts started at 1 instead of 0, so you lost a turn before guessing.
- [x] **Explain what fixes you applied.**
  - Moved `get_range_for_difficulty`, `parse_guess`, `check_guess` and `update_score` from `app.py` into `logic_utils.py` so they can be tested.
  - `check_guess` now compares both values as ints and returns only the outcome. The hint text comes from a `HINT_MESSAGES` table where "Too High" says go LOWER.
  - Removed the code in `app.py` that turned the secret into a string.
  - New Game now resets status, score, history and attempts, and picks the new secret from the current difficulty's range.
  - Attempts now start at 0.
  - Added 3 regression tests, and each fix has a `# FIXME` / `# FIX` comment in the code.

## 📸 Demo Walkthrough

A sample game on Normal difficulty (1–100) where the secret is 63:

1. The game starts with 0 attempts, a score of 0 and 8 attempts allowed.
2. User enters a guess of 40. The game shows "📈 Go HIGHER!" and the score goes to -5.
3. User enters a guess of 70. The game shows "📉 Go LOWER!" and the score goes to 0.
4. User types "abc". The game shows "That is not a number." and gives no hint.
5. User enters a guess of 63. The game shows "🎉 Correct!", balloons, and "You won! The secret was 63. Final score: 50".
6. User clicks "New Game 🔁". Attempts, score and history reset to 0/empty, a new secret is picked, and the user can guess again.

Known quirks still left: the "Attempts left" line updates one guess late, invalid input still uses up an attempt, and a "Too High" guess adds 5 points on even attempts instead of subtracting them. The hint also always says "between 1 and 100", even on Easy and Hard.

## 🧪 Test Results

```
$ python -m pytest
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0
collected 6 items

tests/test_game_logic.py ......                                          [100%]

============================== 6 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
