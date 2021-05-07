box_numeratore = '''
BoxLayout:
    id: porcodio
    padding: "10dp"
    MDTextField:
        id: numerator
        hint_text: "inserisci il numeratore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .8}
'''

box_denominatore = '''
BoxLayout:
    padding: "10dp"
    MDTextField:
        id: denominator
        hint_text: "inserisci il denominatore"
        helper_text: "There will always be a mistake"
        pos_hint: {"center_x": .5, "center_y": .7}
'''