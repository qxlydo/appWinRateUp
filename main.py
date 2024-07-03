from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.core.window import Window 
from kivy.uix.label import Label 
from kivy.uix.image import Image 


class MyApp(App):
    def resize(self, window, width, height):
        if width < height:
            # портретная ориентация
            Window.size = (width * 0.8, height * 0.8)
        else:
            # альбомная ориентация
            Window.size = (width * 0.8, height * 0.6)

    def build(self): 
        Window.bind(size=self.resize)
        Window.bind(width=self.resize, height=self.resize)
        
        al = AnchorLayout(anchor_y='top', padding=[0, 100]) 
        bl = BoxLayout(orientation='vertical', size_hint=[None, None], size=[240, 350]) 
        fl = FloatLayout() 
 
        # Добавляем фоновое изображение 
 
        self.matches_played = TextInput(font_size=18) 
        self.current_win_rate = TextInput(font_size=18) 
        self.required_win_rate = TextInput(font_size=18) 
        self.wins_today = TextInput(font_size=18) 
        self.result_label = Label(text='', font_size=20) 
 
        bl.add_widget(Label(text='Сколько матчей сыграно')) 
        bl.add_widget(self.matches_played) 
        bl.add_widget(Label(text='Нынешний % побед')) 
        bl.add_widget(self.current_win_rate) 
        bl.add_widget(Label(text='Требуемый % побед')) 
        bl.add_widget(self.required_win_rate) 
        bl.add_widget(Label(text='Победы в течении дня')) 
        bl.add_widget(self.wins_today) 
        button = Button(text='click!', on_press=self.on_button_press) 
        bl.add_widget(button) 
        bl.add_widget(self.result_label) 
 
        al.add_widget(bl) 
        return al 
 
    def on_button_press(self, instance): 
        matches_played = int(self.matches_played.text) 
        current_win_rate = float(self.current_win_rate.text) 
        required_win_rate = float(self.required_win_rate.text) 
        wins_today = int(self.wins_today.text) 
 
        # Вычисляем необходимое количество побед для достижения требуемого процента побед 
        required_wins = int(matches_played * (required_win_rate / 100)) 
        current_wins = int(matches_played * (current_win_rate / 100)) 
        additional_wins_needed = required_wins - current_wins 
 
        # Выводим результат в Label 
        self.result_label.text = f"Необходимо {additional_wins_needed} побед" 
        
if __name__ == '__main__': 
    MyApp().run()