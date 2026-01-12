# ÙÙØ¯ Ø§ÙÙÙØ§Ø© Ø§ÙØ¹Ø§ÙÙÙØ© ÙÙÙØ´Ø±ÙØ¹ Ø±ÙÙ 1
import os
import cryptography
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

# Ø¥Ø¹Ø¯Ø§Ø¯Ø§Øª Ø§ÙÙØ§Ø¬ÙØ© ÙØ¯Ø¹Ù Ø¬ÙÙØ¹ Ø§ÙØ´Ø§Ø´Ø§Øª ÙØ§ÙÙØ§Ø±ÙØ§Øª
Window.clearcolor = (0.05, 0.05, 0.1, 1) # ÙÙÙ ÙÙÙÙ Ø§Ø­ØªØ±Ø§ÙÙ

class MainShieldScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Ø¹ÙÙØ§Ù Ø§ÙØªØ·Ø¨ÙÙ Ø¨Ø§ÙÙØºØ© Ø§ÙØ¹Ø±Ø¨ÙØ©
        self.label = Label(
            text="ð¡ï¸ ÙØ¸Ø§Ù Ø§ÙØ­ÙØ§ÙØ© Ø§ÙØ¹Ø§ÙÙÙ\nØªØ´ÙÙØ± Ø¹Ø³ÙØ±Ù ÙØ´Ø·",
            font_size='30sp',
            halign='center',
            color=(0, 1, 0.8, 1) # ÙÙÙ Ø§ÙØªÙÙÙÙÙØ¬ÙØ§ Ø§ÙÙØ³ØªÙØ¨ÙÙ
        )
        
        layout.add_widget(self.label)
        self.add_widget(layout)

class GlobalAIApp(App):
    def build(self):
        # ØªÙØ¹ÙÙ ÙØ­Ø±Ù Ø§ÙØ°ÙØ§Ø¡ Ø§ÙØ§ØµØ·ÙØ§Ø¹Ù Ø§ÙØ¹Ø§ÙÙÙ Ø¹ÙØ¯ Ø§ÙØ§ÙØ·ÙØ§Ù
        self.title = "Globa
