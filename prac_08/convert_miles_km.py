from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES = 1.60934


class ConvertMilesToKilometres(App):
    """ ConvertMilesToKilometres is a Kivy App for converting miles to kilometres """
    output_text = StringProperty

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 500)
        self.title = "Miles Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        """handles when up/down is pressed.
        If value is True, current value +1. If value is False, current value -1.
        """
        input_number = self.root.ids.input_number
        try:
            current_value = int(input_number.text)
        except ValueError:
            current_value = 0
        if value:
            current_value += 1
        else:
            current_value -= 1
        input_number.text = str(current_value)
        self.handle_conversion(current_value)

    def handle_conversion(self, value):
        """handles the calculation for converting miles to kilometres"""
        try:
            current_value = float(value)
        except ValueError:
            current_value = 0.0
        km = current_value * MILES
        self.root.ids.output_label.text = str(km)

    def handle_update(self):
        """handles updating the conversion result with error handling"""
        try:
            user_value = float(self.root.ids.input_number.text)
        except ValueError:
            user_value = 0.0
        self.handle_conversion(user_value)


ConvertMilesToKilometres().run()
