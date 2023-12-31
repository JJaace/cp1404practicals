"""Estimate: 30 minutes
    Actual: 30-35 minutes
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a simple Kivy app that greets the user"""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handles the greeting"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handles clearing the input box"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
