from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgets(App):
    status_text = StringProperty("")

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Jaace", "Steve", "Kate", "Jack", "Zach"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widget(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        name = instance.text
        self.status_text = f"Hello {name}"


DynamicWidgets().run()
