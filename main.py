from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
import os

# Load UI
Builder.load_file("ui/main.kv")

from ui.home_screen import HomeScreen
from ui.transfer_screen import TransferScreen
from ui.about_screen import AboutScreen

# Set window size for mobile view testing
Window.size = (360, 640)

class WiFiFileTransferApp(App):
    def build(self):
        self.title = "WiFi File Transfer Pro"
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(TransferScreen(name='transfer'))
        self.sm.add_widget(AboutScreen(name='about'))
        return self.sm

if __name__ == '__main__':
    WiFiFileTransferApp().run()
