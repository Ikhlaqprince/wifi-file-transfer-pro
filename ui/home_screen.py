from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from server import WiFiServer
import socket

class HomeScreen(Screen):
    ip_address = StringProperty("Not Started")
    server = None

    def start_server(self):
        if not self.server:
            self.server = WiFiServer(port=8080)
            self.server.start_in_thread()
            ip = self.get_ip()
            self.ip_address = f"http://{ip}:8080"

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip
