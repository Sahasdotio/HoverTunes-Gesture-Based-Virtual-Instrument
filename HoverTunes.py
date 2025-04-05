import cv2
import mediapipe as mp
import numpy as np
import pygame
import time
import sounddevice as sd
import wave
from threading import Thread

# Initialize pygame for sound playback
pygame.init()

# Load instrument sounds
sounds = {
    "guitar": pygame.mixer.Sound("guitar.wav"),
    "piano": pygame.mixer.Sound("piano.wav"),
    "drum": pygame.mixer.Sound("drum.wav"),
    "flute": pygame.mixer.Sound("flute.wav")
}

# Load instrument images
images = {
    "guitar": cv2.imread("guitar.png"),
    "piano": cv2.imread("piano.png"),
    "drum": cv2.imread("drum.png"),
    "flute": cv2.imread("flute.png")
}

# Resize images for display
for key in images:
    images[key] = cv2.resize(images[key], (120, 120))

# Theme settings
themes = {
    "default": ((200, 200, 200), (50, 50, 50)),
    "dark": ((50, 50, 50), (200, 200, 200)),
    "neon": ((0, 255, 255), (255, 0, 255))
}
current_theme = "default"
last_theme_switch = time.time()

# Mediapipe hands setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Define button positions and sizes
button_positions = {
    "guitar": (50, 20),
    "piano": (200, 20),
    "drum": (350, 20),
    "flute": (500, 20)
}

# Recording variables
is_recording = False
recording_frames = []
fs = 44100  # Sample rate
hovered_button = None  # To track hovered button

# Function to start/stop recording
def toggle_recording():
    global is_recording, recording_frames
    if not is_recording:
        print("Recording started...")
        recording_frames = []
        is_recording = True
        Thread(target=record_audio).start()
    else:
        print("Recording stopped.")
        is_recording = False
        save_recording()

# Function to record audio
def record_audio():
    global recording_frames
    while is_recording:
        recording_frames.append(sd.rec(int(0.1 * fs), samplerate=fs, channels=2, dtype=np.int16))
        sd.wait()

# Function to save recording
def save_recording():
    if recording_frames:
        print("Saving recording...")
        audio_data = np.concatenate(recording_frames, axis=0)
        with wave.open("recording.wav", "wb") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(audio_data.tobytes())
        print("Recording saved as 'recording.wav'")

# Function to switch themes
def switch_theme():
    global current_theme, last_theme_switch
    if time.time() - last_theme_switch > 1:  # 1-second delay to prevent rapid switching
        themes_list = list(themes.keys())
        current_index = themes_list.index(current_theme)
        current_theme = themes_list[(current_index + 1) % len(themes_list)]
        last_theme_switch = time.time()
        print(f"Switched to {current_theme} theme")

# Open camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Convert image to RGB for mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    # Get current theme colors
    bg_color, border_color = themes[current_theme]
    
    # Draw instrument buttons
    for key, (x, y) in button_positions.items():
        if hovered_button == key:
            cv2.rectangle(frame, (x - 10, y - 10), (x + 130, y + 130), (255, 255, 0), -1)  # Glow effect
        else:
            cv2.rectangle(frame, (x - 5, y - 5), (x + 125, y + 125), bg_color, -1)
        
        frame[y:y+120, x:x+120] = images[key]
        cv2.rectangle(frame, (x - 5, y - 5), (x + 125, y + 125), border_color, 3)
        cv2.putText(frame, key.capitalize(), (x + 20, y + 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6, border_color, 2)

    # Draw recording button (animated pulse effect)
    rec_x, rec_y, rec_radius = 50, h - 50, 35 + (3 if not is_recording else 0)
    color = (0, 255, 0) if is_recording else (0, 0, 255)
    cv2.circle(frame, (rec_x, rec_y), rec_radius, color, -1)
    cv2.putText(frame, "Rec", (rec_x - 20, rec_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                                   mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3), 
                                   mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2))
            index_x, index_y = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
            
            hovered_button = None
            for key, (x, y) in button_positions.items():
                if x < index_x < x + 120 and y < index_y < y + 120:
                    hovered_button = key
                    sounds[key].play()
                    time.sleep(0.2)
            
            if (index_x - rec_x) ** 2 + (index_y - rec_y) ** 2 < rec_radius ** 2:
                toggle_recording()
                time.sleep(0.5)
            
            if index_y > h - 50:
                switch_theme()

    cv2.imshow("Virtual Instrument", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
