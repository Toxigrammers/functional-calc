from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder


KV = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: numeratore
        hint_text: "inserisci il numeratore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()