'''
# kivymd version 1.1.1
# Home-page: https://github.com/kivymd/KivyMD  
# kivy version 2.2.1
# Home-page: http://kivy.org

Main file of your application
'''
from kivymd.uix.screen import MDScreen
from utils.demo import Demo


class TestClass(MDScreen):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.add_widget(Demo())
