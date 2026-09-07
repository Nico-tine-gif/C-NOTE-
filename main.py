
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CryptoMasterX1App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text='C-NOTE-\nCryptoMasterX1', font_size='24sp', halign='center')
        status = Label(text='App is Working! No Crash!', font_size='18sp')
        
        btn = Button(text='CLICK ME', size_hint=(1, 0.3), background_color=(0,1,0,1))
        btn.bind(on_press=lambda x: setattr(status, 'text', 'SUCCESS! Your APK Works!'))
        
        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    CryptoMasterX1App().run()
