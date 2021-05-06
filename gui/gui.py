from styled_components import *
from kivymd.app import MDApp
from kivy.lang import Builder
from styled_components import *
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        screen.add_widget (
            MDRectangleFlatButton (
                text="Press me!",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                on_release=self.event )
        )
        self.numeratore = Builder.load_string(box_numeratore)
        self.denominatore = Builder.load_string(box_denominatore)
        screen.add_widget(self.numeratore)
        screen.add_widget(self.denominatore)
        return screen

    def event(self,obj):
        # self.numeratore.text = str(self.numeratore)
        # print(self.numeratore.text)
        print("miao")


MainApp().run()
