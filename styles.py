class Styles:
    THEMES = {
        "light": {"bg": (255, 255, 255), "btn": (0, 0, 0), "text": (50, 50, 50)},
        "dark": {"bg": (30, 30, 30), "btn": (200, 200, 200), "text": (255, 255, 255)},
        "funky": {"bg": (255, 0, 255), "btn": (0, 255, 255), "text": (255, 255, 0)},
        "ocean": {"bg": (0, 102, 204), "btn": (255, 255, 255), "text": (0, 255, 128)}
    }
    
    FONT = "Arial"
    BUTTON_RADIUS = 10
    BUTTON_PADDING = 15
    ICON_SIZE = (80, 80)
    RECORD_BUTTON_SIZE = 50
    RECORD_BUTTON_COLOR = (255, 0, 0)
    
    @staticmethod
    def get_theme(name):
        return Styles.THEMES.get(name, Styles.THEMES["light"])
