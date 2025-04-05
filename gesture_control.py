import cv2
import mediapipe as mp
import time

class GestureController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.last_theme_switch = time.time()

    def get_frame(self):
        cap = cv2.VideoCapture(0)
        success, frame = cap.read()
        if not success:
            return None, None
        frame = cv2.flip(frame, 1)
        return success, frame

    def detect_gesture(self, frame):
        hand_positions = []
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand_positions.append((cx, cy))
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return hand_positions

    def is_hovering(self, x, y, hand_positions, threshold=50):
        for hx, hy in hand_positions:
            if abs(hx - x) < threshold and abs(hy - y) < threshold:
                return True
        return False

    def theme_switch_gesture(self):
        current_time = time.time()
        if current_time - self.last_theme_switch > 2:  # Adding delay
            self.last_theme_switch = current_time
            return True
        return False
