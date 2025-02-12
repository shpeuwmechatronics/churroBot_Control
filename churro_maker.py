from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton

class ChurroControlScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        # Title Label
        self.add_widget(Label(text='Churro Maker Control', font_size=30))
        
        # Shape Selection
        self.add_widget(Label(text='Select Churro Shape:'))
        self.shape_spinner = Spinner(
            text='Round',
            values=('Round', 'Star', 'Square')
        )
        self.add_widget(self.shape_spinner)
        
        # Size Selection
        self.add_widget(Label(text='Churro Size:'))
        self.size_slider = Slider(min=1, max=10, value=5)
        self.add_widget(self.size_slider)
        
        # Start Button
        self.start_button = Button(text='Start', font_size=20, size_hint=(1, 0.3))
        self.start_button.bind(on_press=self.start_churro_making)
        self.add_widget(self.start_button)
        
        # Status Label
        self.status_label = Label(text='Status: Idle', font_size=20)
        self.add_widget(self.status_label)
    
    def start_churro_making(self, instance):
        shape = self.shape_spinner.text
        size = int(self.size_slider.value)
        self.status_label.text = f'Starting {shape} churro, size {size}...'
        # Here you would add GPIO or serial communication to start the robot

class ChurroMakerApp(App):
    def build(self):
        return ChurroControlScreen()

if __name__ == '__main__':
    ChurroMakerApp().run()
