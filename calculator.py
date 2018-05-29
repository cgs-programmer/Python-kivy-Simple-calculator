# This is a simple calculator in python GUI version in kivy

import __future__

import kivy
kivy.config.Config.set('graphics','resizable',0) # makes the window not resizable
from kivy.app import App  
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget  
from kivy.core.window import Window
from kivy.properties import ObjectProperty,BooleanProperty,StringProperty

Window.show_cursor = True

# This is the main screen of the calculator software
class Ui(BoxLayout): 
    inputs = ObjectProperty() # reference of text display in kv file
    
    # makes sure that this runs as soon as this is called
    def __init__(self,**kwargs):
        super(Ui,self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = None,None
        self.size = 300,400         # window size

        Window.size = self.size     # size the window to window size


    def one_pressed(self):
    	self.inputs.text += str(1)
        
    def two_pressed(self):
    	self.inputs.text += str(2)

    def three_pressed(self):
    	self.inputs.text += str(3)

    def four_pressed(self):
        self.inputs.text += str(4)

    def five_pressed(self):
        self.inputs.text += str(5)

    def six_pressed(self):
        self.inputs.text += str(6)

    def seven_pressed(self):
        self.inputs.text += str(7)

    def eight_pressed(self):
        self.inputs.text += str(8)

    def nine_pressed(self):
        self.inputs.text += str(9)

    def zero_pressed(self):
        self.inputs.text += str(0)
        
    def add_pressed(self):
        self.inputs.text += "+"

    def subtract_pressed(self):
        self.inputs.text += "-"

    def division_pressed(self):
        self.inputs.text += "/"

    def multiply_pressed(self):
        self.inputs.text += "*"

    def modulus_pressed(self):
   		self.inputs.text += "%"

    def delete_pressed(self):
        self.inputs.text = ""

    def dot_pressed(self):
        self.inputs.text += "."

    def equal_to_pressed(self):
    	try:
    		self.result = eval(compile((self.inputs.text),"<string>","eval",__future__.division.compiler_flag))
    		self.output = str(self.result)
    		self.inputs.text = str(self.output)
    	except:
    		self.inputs.text = str("!Error ! ! !")

class MainApp(App):
    def build(self):
        return Ui()
        
if __name__ == '__main__':
    MainApp().run()


