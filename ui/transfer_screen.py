from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from file_manager import FileManager

class TransferScreen(Screen):
    files = ListProperty([])

    def on_enter(self):
        self.load_files()

    def load_files(self):
        fm = FileManager()
        self.files = fm.list_files()
