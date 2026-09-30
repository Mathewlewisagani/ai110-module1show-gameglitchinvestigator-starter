# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? I read the game instructions and without opening the developer debug info I guessed a number. I kept picking higher numbers with wider ranges between each choice and the hint kept nudging me to go higher. I kept going up and my last 2 attempt flagged something unusual. I entered 99, hint said go higher, but when I entered 100 it said go lower, only to realize at the end of the game that the answer was 21. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - New game button was not restarting a new game. The attemps left would update but I couldn't play another consecutive round after losing the previous game
  - I also noticed the hint was backwards, from my explanation in the first part.
  - On the developer debug info, I noticed that the game started with 1 attempt instead of 0
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location
|-------|-------------------|-----------------|------------------------|
| Guess = 50| Go lower | Go higher | none | check_guess() in app.py
| secret = 34| 
| Attempts left = 1 | 1 more round | game ends | Out of attempts! |attemps initalization in app.py 
| Click on new game button | new round | game hangs | Game over. Start a new game to try again  | a session rerun bug, previous session never dies

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude Code inside VS Code. I attached app.py, logic_utils.py and reflection.md and pasted in the phase instructions so it could see how the UI and logic files connect.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude explained why my 99 and 100 guesses gave opposite hints when the secret was 21. On every even attempt app.py turned the secret into a string, so the comparison was done like words instead of numbers. "99" comes after "21" so it said too high, but "100" starts with a "1" so it came before "21" and said too low. On top of that the hint messages themselves were swapped, so "Too High" told me to go HIGHER. It suggested removing the string conversion and fixing the messages in check_guess. This matched exactly what happened in my first game, and I verified it with a pytest case that checks 99 and 100 against a secret of "21" both come back as "Too High".
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - Claude skipped the step where I was supposed to add a # FIXME comment where the logic breaks. It went straight to fixing the bugs, and when I asked about it, it said I could just skip it and mention it in my reflection. I didn't want to skip a required step, so I had it go back and add a FIXME marker above each bug, right next to its FIX comment. It also gave me the wrong line numbers for its fixes. When I highlighted lines 95-104 they turned out to be the st.stop() check and not the New Game fix it described. I verified by searching app.py and logic_utils.py for FIXME and checking that each marker sits right above the line where the bug was, and I ran pytest again to make sure the comments didn't break anything.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I considered a bug fixed when there was a test for it that passed, and when the game actually behaved differently when I played it. For the hints that meant a pytest case. For the New Game button that meant losing a game on purpose and seeing if I could start another round.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran pytest and all 6 tests passed, the 3 starter tests and 3 new ones. The new ones check that a guess of 60 against 50 is "Too High" and the hint says go LOWER, that 40 against 50 says go HIGHER, and that a string secret like "21" is still compared as a number. The starter tests expected check_guess to return just "Win"/"Too High"/"Too Low", so that is what it returns now, and the app looks up the hint message separately.
  
- Did AI help you design or understand any tests? How? Yes, Claude wrote the tests and picked the exact inputs from my own bug (99 and 100 vs 21). That made it clear the test was targeting the bug I saw and not just some general case. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Every time you click a button or type something, Streamlit runs the whole script again from top to bottom. That means normal variables get wiped out every time. st.session_state is the place where you keep things that need to survive between reruns, like the secret number, attempts and score. The New Game bug is a good example: the button reset some of the values in session state but not the status, so after every rerun the game still thought it was over.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - Writing a test that uses the exact input from the bug I saw. Having 99 and 100 vs 21 as a test means if the bug ever comes back I'll know right away.
- What is one thing you would do differently next time you work with AI on a coding task? I would go one step at a time and check each step before moving on. Giving the AI all the instructions at once made it skip a step and give me line numbers I had to double check.
- In one or two sentences, describe how this project changed the way you think about AI generated code. The starter code "looked" fine and claimed to be production-ready but had bugs that only showed up while playing. Now I know AI code, including the fixes, has to be checked with tests and by actually running it.
