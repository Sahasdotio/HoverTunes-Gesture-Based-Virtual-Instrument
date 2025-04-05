# 🎵 HoverTunes - Gesture-Based Virtual Instrument 🎶

HoverTunes is an AI-powered virtual instrument that allows users to play different musical instruments using just hand gestures. The system utilizes computer vision, hand tracking, and sound processing to create an immersive, touch-free music experience! 🎸🎹🥁

---

## 🚀 Features

✅ **Hand Gesture Detection** – Uses AI-based hand tracking to recognize interactions.\
✅ **Multiple Instruments** – Play Guitar, Piano, Drums, and Flute.\
✅ **Hover-Based Sound Playback** – Just hover over an instrument to play its sound.\
✅ **Live Recording** – Record and save your compositions.\
✅ **Customizable Themes** – Switch between different UI themes using hand gestures.\
✅ **Animated UI Elements** – Smooth animations for a visually appealing experience.\
✅ **Real-time Processing** – Ensures a lag-free musical experience.

---

## 📂 Project Structure

```
📦 HoverTunes
 ┣ 📂 assets                # Image & sound assets for instruments
 ┣ 📜 HoverTunes.py         # Main application file (UI & gesture control)
 ┣ 📜 LICENSE               # License file (MIT License)
 ┣ 📜 README.md             # Documentation file (This file)
 ┣ 📜 gesture_control.py    # Handles gesture recognition logic
 ┣ 📜 sound_player.py       # Manages sound playback & recording
 ┣ 📜 theme_manager.py      # Controls UI theme switching
 ┣ 📜 animations.py         # Adds smooth animations to UI elements
 ┣ 📜 styles.py             # Defines color themes & UI styles
 ┣ 📜 requirements.txt      # Dependencies list for easy setup 
```

---

## 🔧 Prerequisites

Before running HoverTunes, make sure you have the following installed:

- Python 3.8+
- OpenCV
- MediaPipe
- PyGame
- NumPy
- Soundfile & PyAudio (for recording & playback)

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎮 How It Works

1. **Launch the Application:** Run `main.py` to start HoverTunes.
2. **Hand Detection:** Move your hand over an instrument icon to play it.
3. **Recording Feature:** Click the circular button (bottom left) to start/stop recording.
4. **Theme Switching:** Change the UI theme by making a specific hand gesture.
5. **Enjoy!** Create music effortlessly using just your hands.

---

## ⚠️ Precautions

🔹 Ensure proper lighting for accurate hand tracking.\
🔹 Avoid excessive movement for smoother sound transitions.\
🔹 Place your hand at an optimal distance from the camera.\
🔹 Keep background noise minimal for better audio quality.

---

## 📸 Screenshots & Demo

![HoverTunes](output)


---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

We welcome contributions! Feel free to fork the repo and submit pull requests.

---

## 📬 Contact

For any questions, reach out via [your email or GitHub profile link].

🎵 **HoverTunes – Play music in the air!** ✨

