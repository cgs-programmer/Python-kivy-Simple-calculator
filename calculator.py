# This is for educational purpose,you can modify it as you wish
# This is just a simple calculator, it will have bugs

from kivy.app import App  
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget  
from kivy.core.window import Window 
from kivy.properties import ObjectProperty,BooleanProperty,StringProperty

# This is the main screen of the calculator software
class Ui(BoxLayout): 
    inputs = ObjectProperty() # reference of text display in kv file
    
    one = ObjectProperty()
    two = ObjectProperty()
    three = ObjectProperty()
    four = ObjectProperty()
    five = ObjectProperty()
    six = ObjectProperty()
    seven = ObjectProperty()
    eight = ObjectProperty()
    nine = ObjectProperty()
    zero = ObjectProperty()
    add = ObjectProperty()
    sub = ObjectProperty()
    mul = ObjectProperty()
    div = ObjectProperty()
    modulus = ObjectProperty()
    dels = ObjectProperty()     # clears the screen
    dot = ObjectProperty()
    is_equal = ObjectProperty()   # do calculation 
    
    first_pressed = BooleanProperty(False)  # becomes true it is pressed
    operator_pressed = BooleanProperty(False) # becomes true when operator is pressed
    is_opt_pressed = BooleanProperty(False) 
    
    displays = StringProperty('')   # the main display holder
    
    ops = '' # operator holder
    
    l_intakes = StringProperty('') # left operand
    r_intakes = StringProperty('') # right operand
    
    # makes sure that this runs as soon as this is called
    def __init__(self,**kwargs):
        super(Ui,self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = None,None
        self.size = 300,500         # window size

        Window.size = self.size     # size the window to window size


    def one_pressed(self,instance):
        if self.first_pressed == False:  # if there is no left operand then
            self.inputs.text = '1'   # do this
            self.l_intakes = '1'     # stores the input in left operand holder
            self.first_pressed = True # this becomes true
        else:
            if self.operator_pressed == False:   # self explanatory
                self.l_intakes += '1'
                self.inputs.text += self.l_intakes
            else:
                self.r_intakes += '1' # stores the input in the right operand holder
                self.displays += '1'
                self.inputs.text = self.displays # update the display
        
    def two_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '2'
            self.l_intakes = '2'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '2'
                self.inputs.text = self.l_intakes    
            else:
                self.r_intakes += '2'
                self.displays += '2'
                self.inputs.text = self.displays
        
        
    def three_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '3'
            self.l_intakes = '3'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '3'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '3'
                self.displays += '3'
                self.inputs.text = self.displays
  
        
    def four_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '4'
            self.l_intakes = '4'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '4'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '4'
                self.displays += '4'
                self.inputs.text = self.displays
  
        
    def five_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '5'
            self.l_intakes = '5'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '5'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '5'
                self.displays += '5'
                self.inputs.text = self.displays
  
        
    def six_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '6'
            self.l_intakes = '6'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '6'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '6'
                self.displays += '6'
                self.inputs.text = self.displays
  
        
    def seven_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '7'
            self.l_intakes = '7'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '7'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '7'
                self.displays += '7'
                self.inputs.text = self.displays
  
        
    def eight_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '8'
            self.l_intakes = '8'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '8'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '8'
                self.displays += '8'
                self.inputs.text = self.displays
  
        
    def nine_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '9'
            self.l_intakes = '9'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '9'
                self.inputs.text = self.l_intakes
            else:
                self.r_intakes += '9'
                self.displays += '9'
                self.inputs.text = self.displays
  
        
    def zero_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '0'
            self.l_intakes = '0'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '0'
                self.inputs.text = self.l_intakes
            else: 
                self.r_intakes += '0'
                self.displays += '0'
                self.inputs.text = self.displays
    
    def dot_pressed(self):
        if self.first_pressed == False:
            self.inputs.text = '.'
            self.l_intakes = '.'
            self.first_pressed = True
        else:
            if self.operator_pressed == False:
                self.l_intakes += '.'
                self.inputs.text = self.l_intakes
            else: 
                self.r_intakes += '.'
                self.displays += '.'
                self.inputs.text = self.displays
  
        
    def add_pressed(self):
        # if there is atleast one number in left operand also the 
        # operator is already pressed then 
        if self.first_pressed == True and self.is_opt_pressed == False:
            # do this
            self.ops = '+' # stores the operator input in ops holder
            self.displays = self.l_intakes + self.ops  # update the display
            self.inputs.text = self.displays
            self.operator_pressed = True  # operator pressed becomes true
            self.is_opt_pressed = True    
        
    def sub_pressed(self):
        if self.first_pressed == True and self.is_opt_pressed == False:
            self.ops = '-'
            self.displays = self.l_intakes + self.ops
            self.inputs.text = self.displays
            self.operator_pressed = True
            self.is_opt_pressed = True
        
    def mul_pressed(self):
        if self.first_pressed == True and self.is_opt_pressed == False:
            self.ops = '*'
            self.displays = self.l_intakes + self.ops
            self.inputs.text = self.displays
            self.operator_pressed = True
            self.is_opt_pressed = True
        
    def div_pressed(self):
        if self.first_pressed == True and self.is_opt_pressed == False:
            self.ops = '/'
            self.displays = self.l_intakes + self.ops
            self.inputs.text = self.displays
            self.operator_pressed = True
            self.is_opt_pressed = True
        
    def modulus_pressed(self):
        if self.first_pressed == True and self.is_opt_pressed == False:
            self.ops = '%'
            self.displays = self.l_intakes + self.ops
            self.inputs.text = self.displays
            self.operator_pressed = True
            self.is_opt_pressed = True
        
    def del_pressed(self):
        if self.first_pressed == True:
            self.inputs.text = '0'
            self.l_intakes = ''
            self.r_intakes = ''
        
    def is_equal_pressed(self):
        if self.r_intakes:  # if there is no input and equal is presed then do nothing
            if self.first_pressed == True and self.operator_pressed == True:
                if self.ops == '+':
                    # do the operation
                    self.result = float(self.l_intakes) + float(self.r_intakes)
                    self.inputs.text = str(self.result)
                    self.l_intakes = str(self.result)
                    self.r_intakes = ''
                    self.ops = ''
                    self.displays = self.l_intakes  # update the display
                    self.operator_pressed = False   # it is falsed again so that 
                    self.is_opt_pressed = False     # we can do more calculation
                    
                elif self.ops == '-':
                    self.result = float(self.l_intakes) - float(self.r_intakes)
                    self.inputs.text = str(self.result)
                    self.l_intakes = str(self.result)
                    self.r_intakes = ''
                    self.ops = ''
                    self.displays = self.l_intakes
                    self.operator_pressed = False
                    self.is_opt_pressed = False
                    
                elif self.ops == '*':
                    self.result = float(self.l_intakes) * float(self.r_intakes)
                    self.inputs.text = str(self.result)
                    self.l_intakes = str(self.result)
                    self.r_intakes = ''
                    self.ops = ''
                    self.displays = self.l_intakes
                    self.operator_pressed = False
                    self.is_opt_pressed = False
                    
                elif self.ops == '/':
                    self.result = float(self.l_intakes) / float(self.r_intakes)
                    self.inputs.text = str(self.result)
                    self.l_intakes = str(self.result)
                    self.r_intakes = ''
                    self.ops = ''
                    self.displays = self.l_intakes
                    self.operator_pressed = False
                    self.is_opt_pressed = False
               
                elif self.ops == '%':
                    self.result = float(self.l_intakes) % float(self.r_intakes)
                    self.inputs.text = str(self.result)
                    self.l_intakes = str(self.result)
                    self.r_intakes = ''
                    self.ops = ''
                    self.displays = self.l_intakes
                    self.operator_pressed = False
                    self.is_opt_pressed = False
        else:
            pass

class MainApp(App):
    def build(self):
        return Ui()
        
if __name__ == '__main__':
    MainApp().run()






