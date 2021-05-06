from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.behaviors import ButtonBehavior

box_numeratore = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: numeratore
        hint_text: "inserisci il numeratore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .8}
'''

box_denominatore = '''
BoxLayout:
    padding: "10dp"
    MDTextField:
        id: numeratore
        hint_text: "inserisci il denominatore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .7}
'''

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Press me!",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_press=self.event
            )
        ),
        numeratore = Builder.load_string(box_numeratore)
        denominatore = Builder.load_string(box_denominatore)
        screen.add_widget(numeratore)
        screen.add_widget(denominatore)
        return screen
    def event(self, obj):
        print("added event!")
MainApp().run()
