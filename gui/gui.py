import kivy
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
        self.numerator = Builder.load_string(box_numeratore)
        self.denominator = Builder.load_string(box_denominatore)
        screen.add_widget(self.numerator)
        screen.add_widget(self.denominator)
        return screen

    def event(self,obj):
        # numerator = self.numeratore.text
        print(self.numerator.idstext)
        print("miao")

if __name__ == '__main__':
    MainApp().run()
