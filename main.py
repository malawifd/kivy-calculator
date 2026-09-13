from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Set window size
Window.size = (400, 600)


class CalculatorApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display
        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=40,
            size_hint_y=0.2,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1)
        )
        main_layout.add_widget(self.display)
        
        # Buttons layout
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint_y=0.8)
        
        # Button definitions: (label, color, function)
        buttons = [
            ('7', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('7')),
            ('8', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('8')),
            ('9', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('9')),
            ('/', (1, 0.5, 0, 1), lambda: self.on_button_press('/')),
            
            ('4', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('4')),
            ('5', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('5')),
            ('6', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('6')),
            ('*', (1, 0.5, 0, 1), lambda: self.on_button_press('*')),
            
            ('1', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('1')),
            ('2', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('2')),
            ('3', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('3')),
            ('-', (1, 0.5, 0, 1), lambda: self.on_button_press('-')),
            
            ('0', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('0')),
            ('.', (0.2, 0.2, 0.2, 1), lambda: self.on_button_press('.')),
            ('=', (0, 1, 0, 1), lambda: self.on_equals()),
            ('+', (1, 0.5, 0, 1), lambda: self.on_button_press('+')),
            
            ('C', (1, 0, 0, 1), lambda: self.on_clear()),
            ('DEL', (1, 0.2, 0.2, 1), lambda: self.on_delete()),
        ]
        
        # Add buttons to layout
        for label, color, callback in buttons:
            btn = Button(
                text=label,
                font_size=24,
                background_color=color,
                bold=True
            )
            btn.bind(on_press=callback)
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_button_press(self, value):
        """Handle number and operator button presses"""
        self.display.text += str(value)
    
    def on_equals(self):
        """Calculate the result"""
        try:
            if self.display.text:
                result = eval(self.display.text)
                self.display.text = str(result)
        except ZeroDivisionError:
            self.display.text = 'Cannot divide by zero'
        except Exception:
            self.display.text = 'Error'
    
    def on_clear(self):
        """Clear the display"""
        self.display.text = ''
    
    def on_delete(self):
        """Delete last character"""
        self.display.text = self.display.text[:-1]


if __name__ == '__main__':
    app = CalculatorApp()
    app.title = 'Kivy Calculator'
    app.run()
