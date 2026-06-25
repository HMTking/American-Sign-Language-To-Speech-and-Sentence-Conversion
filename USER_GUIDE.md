# 🤟 ASL to Speech & Sentence — User Guide

A hands-free web app that watches your hand through the webcam, recognizes
American Sign Language (ASL) letters, builds words and sentences, and speaks
them aloud. Everything works with gestures — no buttons required.

---

## 1. Quick Start

1. Start the server:
   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```
2. Open **http://127.0.0.1:5000** in your browser.
3. Click **Start Camera** and allow camera access.
4. Make ASL signs in front of the camera. A green skeleton is drawn on your hand
   when it is detected.
5. Hold a sign steady — a **progress ring** fills around your hand, a **beep**
   confirms, and the letter is added to the current word.

> 💡 Needs an internet connection: hand detection (MediaPipe) loads from a CDN.

---

## 2. Letter Signs (A–Z)

The model recognizes the 26 static ASL alphabet handshapes. Sign a letter and
**hold it still** until the green ring completes and you hear the commit beep.

| Sign | Action | Sign | Action |
|------|--------|------|--------|
| 🤚 **A** | Type letter A | 🖐 **N** | Type letter N |
| ✋ **B** | Type letter B | 👌 **O** | Type letter O |
| 🤏 **C** | Type letter C | 👇 **P** | Type letter P |
| ☝️ **D** | Type letter D | **Q** | Type letter Q |
| ✊ **E** | Type letter E | **R** | Type letter R |
| 👌 **F** | Type letter F | ✊ **S** | Type letter S |
| 👉 **G** | Type letter G | **T** | Type letter T |
| ✌️ **H** | Type letter H | ✌️ **U** | Type letter U |
| 🤙 **I** | Type letter I | ✌️ **V** | Type letter V |
| **J** | Type letter J | 🤟 **W** | Type letter W |
| ☝️ **K** | Type letter K | ☝️ **X** | Type letter X |
| 🤟 **L** | Type letter L | 🤙 **Y** | Type letter Y |
| ✊ **M** | Type letter M | **Z** | Type letter Z |

*(Emojis are approximate visual hints — use standard ASL alphabet handshapes for
best accuracy.)*

**Tips for accurate letters**
- Keep the hand inside the frame, palm generally facing the camera.
- Hold each letter steady ~0.7 seconds (until the ring fills).
- To repeat the **same letter twice** (e.g. "LL"), drop your hand briefly or wait
  for the short cooldown, then sign it again.

---

## 3. Control Gestures (no buttons needed)

These are detected by finger position and take **priority over letters**. Hold
them steady; an **orange ring** shows progress.

| Gesture | Handshape | Action |
|---------|-----------|--------|
| ✋ **Open palm** | All 4 fingers extended + thumb out | **Space** — finishes the current word and adds it to the sentence |
| 👊 **Closed fist** | All fingers folded, thumb tucked | **Delete** — removes the last letter (or last word) |
| 👍 **Thumbs-up** | Fist with thumb pointing up | **Speak** — speaks the full sentence aloud, then clears it |

---

## 4. Suggestion Picker (autocomplete by gesture)

As you spell, up to **3 suggested words** appear as chips under the current word
(the first chip is the best match). Pick one hands-free with a **blue ring**:

| Gesture | Handshape | Action |
|---------|-----------|--------|
| ☝️ **1 finger** | Index only | Accept suggestion **#1** |
| ✌️ **2 fingers** | Index + middle | Accept suggestion **#2** |
| 🤟 **3 fingers** | Index + middle + ring | Accept suggestion **#3** |

You can also **click any chip** with the mouse to select it.

> ⚠️ While suggestion chips are visible, the 2- and 3-finger shapes overlap with
> the letters **V/U/K** and **W**. Holding them will pick a suggestion instead of
> typing that letter. To type those letters, pick your word first (or use the
> manual buttons).

---

## 5. Automatic Behavior (pause to act)

You don't have to gesture for everything — just **pause**:

| You do | The app does |
|--------|--------------|
| Hold still / drop hand for ~2 seconds | Finishes the current **word** |
| Hold still / drop hand for ~4 seconds | Finishes the word, then **speaks the sentence** and clears it |

When a word is finalized, if your spelling isn't a real word yet, the **top
suggestion is auto-accepted** (e.g. `HEL` → `HELLO`).

---

## 6. Manual Buttons (fallback)

If a gesture is hard to make, the on-screen buttons do the same thing:

| Button | Action |
|--------|--------|
| ➕ **Add Space** | Finish current word |
| ⌫ **Delete** | Remove last letter / word |
| 🔊 **Speak Text** | Speak the sentence |
| 🗑️ **Clear All** | Erase the word and sentence |

---

## 7. Feature Summary

- ✅ **Real-time hand tracking** — 21-point MediaPipe skeleton drawn live on the video.
- ✅ **26-letter ASL alphabet recognition** via an on-device TensorFlow Lite model.
- ✅ **Stabilization + confidence check** — letters only commit when held steady,
  preventing flicker and false detections.
- ✅ **Visual + audio feedback** — progress ring (green = letter, orange = control,
  blue = pick) and a confirmation beep on every commit.
- ✅ **Hands-free controls** — Space, Delete, and Speak via palm / fist / thumbs-up.
- ✅ **Gesture autocomplete** — pick word suggestions with 1/2/3 fingers.
- ✅ **Pause-to-act** — auto-finish words (2s) and auto-speak sentences (4s).
- ✅ **Spell correction** — sentences are auto-corrected before being spoken.
- ✅ **Text-to-speech** — natural speech via gTTS, played in the browser.
- ✅ **Deploy-ready** — runs on Render (see `RENDER_DEPLOYMENT.md`).

---

## 8. Troubleshooting

| Problem | Fix |
|---------|-----|
| No skeleton on hand | Check lighting; keep the whole hand in frame; allow camera permission. |
| "Detection library failed to load" | You need internet access (MediaPipe CDN). |
| A letter won't register | Hold it steadier/longer; ensure confidence is above the threshold (shown on screen). |
| Wrong letter for fists (A/E/S/M/N/T) | These closed-hand letters can be read as **Delete**. Use the suggestion chips or buttons for words containing them. |
| Speech doesn't play | Click once anywhere on the page first (browsers block audio until you interact). |

---

## 9. Limitations

- The model recognizes only the **26 static letters (A–Z)** — no digits, no
  dynamic motion letters beyond the trained set, and Space/Delete/Speak come from
  finger heuristics rather than the model.
- Closed-fist letters (**A, E, S, M, N, T**) conflict with the Delete gesture.
- Recognition accuracy depends on lighting, camera quality, and how closely your
  handshape matches the trained ASL alphabet.
