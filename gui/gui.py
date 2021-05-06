from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton


KV = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: numeratore
        hint_text: "inserisci il numeratore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .8}
'''

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Vaffanculo",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        ),
        username = Builder.load_string(KV)
        screen.add_widget(username)
        return screen

MainApp().run()
