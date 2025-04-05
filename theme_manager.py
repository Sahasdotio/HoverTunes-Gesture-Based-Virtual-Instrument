class ThemeManager:
    def __init__(self):
        self.themes = {
            "light": {"bg": (255, 255, 255), "btn": (0, 0, 0), "text": (50, 50, 50)},
            "dark": {"bg": (30, 30, 30), "btn": (200, 200, 200), "text": (255, 255, 255)},
            "funky": {"bg": (255, 0, 255), "btn": (0, 255, 255), "text": (255, 255, 0)},
            "ocean": {"bg": (0, 102, 204), "btn": (255, 255, 255), "text": (0, 255, 128)}
        }
        self.current_theme = "light"

    def switch_theme(self):
        theme_keys = list(self.themes.keys())
        current_index = theme_keys.index(self.current_theme)
        self.current_theme = theme_keys[(current_index + 1) % len(theme_keys)]
        return self.themes[self.current_theme]
    
    def get_current_theme(self):
        return self.themes[self.current_theme]
