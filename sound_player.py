import pygame
import sounddevice as sd
import numpy as np
import wave
import threading

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.recording = False
        self.frames = []
        self.samplerate = 44100
        self.channels = 2
        self.recording_thread = None

        self.sounds = {
            "guitar": "sounds/guitar.wav",
            "piano": "sounds/piano.wav",
            "drum": "sounds/drum.wav",
            "flute": "sounds/flute.wav"
        }
    
    def play_sound(self, instrument):
        if instrument in self.sounds:
            pygame.mixer.Sound(self.sounds[instrument]).play()

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.frames = []
            self.recording_thread = threading.Thread(target=self.record_audio)
            self.recording_thread.start()
    
    def record_audio(self):
        with sd.InputStream(samplerate=self.samplerate, channels=self.channels, callback=self.callback):
            while self.recording:
                sd.sleep(100)
    
    def callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.frames.append(indata.copy())
    
    def stop_recording(self, filename="recorded_audio.wav"):
        if self.recording:
            self.recording = False
            self.recording_thread.join()
            self.save_audio(filename)
    
    def save_audio(self, filename):
        audio_data = np.concatenate(self.frames, axis=0)
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)
            wf.setframerate(self.samplerate)
            wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())
