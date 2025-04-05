import time
import math

class Animations:
    def __init__(self):
        self.start_time = time.time()
        
    def pulse_effect(self, base_size, speed=1.5, range_factor=0.2):
        """Creates a pulsing animation effect."""
        scale = 1 + range_factor * math.sin(speed * (time.time() - self.start_time))
        return int(base_size * scale)
    
    def fade_effect(self, alpha_range=(100, 255), speed=2):
        """Creates a fading effect for elements."""
        min_alpha, max_alpha = alpha_range
        alpha = min_alpha + (max_alpha - min_alpha) * (0.5 + 0.5 * math.sin(speed * (time.time() - self.start_time)))
        return int(alpha)
    
    def bounce_effect(self, base_position, amplitude=10, speed=3):
        """Creates a bouncing effect for UI elements."""
        y_offset = amplitude * math.sin(speed * (time.time() - self.start_time))
        return base_position + int(y_offset)
    
    def rotate_effect(self, angle_speed=5):
        """Creates a smooth rotating effect."""
        return (time.time() - self.start_time) * angle_speed % 360
