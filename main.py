import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
import content
from content import Content
import search


x=Window.size[0]
y=Window.size[1]

Window.clearcolor=(1,1,240/255,0)

class computer_terms(GridLayout):
    def __init__(self,**kwargs):
        super(computer_terms,self).__init__(**kwargs)
        self.cols=1
        self.size_hint_x=None
        self.size_hint_y=None
        self.height=y
        self.width=x
        
        
        self.top_bar=GridLayout(cols=4,size_hint_y=None,height=10*y/100)
        self.add_widget(self.top_bar)
        
        self.top_bar.add_widget(Label(size_hint_x=None,width=5))
        
        self.top_bar.add_widget(Label(size_hint_y=None,height=3*y/100,size_hint_x=None,width=3*x/4))
        self.top_bar.add_widget(Label())
        self.top_bar.add_widget(Label(size_hint_x=None,width=5))
        self.top_bar.add_widget(Label(size_hint_x=None,width=5))
        
        self.menu_bar=Spinner(text='Choose a topic', values=content.list,size_hint_y=None,height=7*y/100,size_hint_x=None,width=3*x/4,font_size=x/25)
        self.top_bar.add_widget(self.menu_bar)
        
        self.go=Button(text='GO',font_size=x/25,bold=True)
        self.go.bind(on_press=self.view_content)
        
        
        
        self.top_bar.add_widget(self.go)
        
        self.top_bar.add_widget(Label(size_hint_x=None,width=5))
        
        
        
        self.mid_grid=GridLayout(cols=3,size_hint_y=None,height=y/1.5)
        
        self.mid_grid.add_widget(Label(size_hint_x=None,width=10,size_hint_y=None,height=y/20))
        self.mid_grid.add_widget(Label(size_hint_y=None,height=y/20))
        self.mid_grid.add_widget(Label(size_hint_x=None,width=10,size_hint_y=None,height=y/20))
        
        self.mid_grid.add_widget(Label(size_hint_x=None,width=10))
        
        
        
        
        
        
        self.content_box=Label(markup=True,color=(0,0,0,1),text_size=(x-20,37*y/60),size=(0,0),font_size=30)
        self.mid_grid.add_widget(self.content_box)
        
        
        
        
        
        self.mid_grid.add_widget(Label(size_hint_x=None,width=10))
        
        self.add_widget(self.mid_grid)
        
        
        self.bottom_part=GridLayout(cols=3)
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/2))
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
        
        self.go_google=Button(text='Get more information',font_size=x/25)
        self.bottom_part.add_widget(self.go_google)
        self.go_google.bind(on_press=lambda *args:search.search(self.content_box.text))
        
        
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
        
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/2))
        
        self.bottom_part.add_widget(Label(size_hint_x=None,width=x/4))
      
            
            
 
    
    def view_content(self,instance):
        
        if self.menu_bar.text!='Choose a topic':
            try:
                self.add_widget(self.bottom_part)
            except :
                pass
        
        if self.menu_bar.text=='Computer':
            self.content_box.text=Content.computer
            
        elif self.menu_bar.text=='Input Device':
            self.content_box.text=Content.input_device
            
            
        elif self.menu_bar.text=='Output Device':
            self.content_box.text=Content.output_device
            
        elif self.menu_bar.text=='Memory Device':
            self.content_box.text=Content.memory_device
            
        elif self.menu_bar.text=='Cache Memory':
            self.content_box.text=Content.cache_memory
            
            
            
        elif self.menu_bar.text=='Registers':
            self.content_box.text=Content.registers
            
            
        elif self.menu_bar.text=='Random Access Memory (RAM)':
            self.content_box.text=Content.ram
            
        elif self.menu_bar.text=='Read Only Memory (ROM)':
            self.content_box.text=Content.rom
            
        elif self.menu_bar.text=='Hard Disk':
            self.content_box.text=Content.hard_disk
            
            
            
            
            
            
            
            
            
            
            
        elif self.menu_bar.text=='Pen Drive':
            self.content_box.text=Content.pen_drive
            
            
        elif self.menu_bar.text=='Compact Disc (CD)':
            self.content_box.text=Content.cd
            
        elif self.menu_bar.text=='Floppy Disk':
            self.content_box.text=Content.floppy_disk
            
        elif self.menu_bar.text=='Bit':
            self.content_box.text=Content.bit
            
            
            
        elif self.menu_bar.text=='Byte':
            self.content_box.text=Content.byte
            
            
        elif self.menu_bar.text=='Kilobyte (kB)':
            self.content_box.text=Content.kb
            
        elif self.menu_bar.text=='Megabyte (MB)':
            self.content_box.text=Content.mb
            
        elif self.menu_bar.text=='Gigabyte (GB)':
            self.content_box.text=Content.gb
            
            
            
            
            
            
        elif self.menu_bar.text=='Terabyte (TB)':
            self.content_box.text=Content.tb
            
            
        elif self.menu_bar.text=='Operating System (OS)':
            self.content_box.text=Content.os
            
        elif self.menu_bar.text=='Programming Language':
            self.content_box.text=Content.programming_language
            
        elif self.menu_bar.text=='Application Programs':
            self.content_box.text=Content.application_programs
            
            
            
        elif self.menu_bar.text=='ASCII value':
            self.content_box.text=Content.ascii
            
            
        elif self.menu_bar.text=='utf format':
            self.content_box.text=Content.utf
            
        elif self.menu_bar.text=='Compiler':
            self.content_box.text=Content.compiler
            
        elif self.menu_bar.text=='Assembler':
            self.content_box.text=Content.assembler
            
     
     
     
     
     
     
     
     
        elif self.menu_bar.text=='POST operation':
            self.content_box.text=Content.post
            
            
        elif self.menu_bar.text=='second':
            self.content_box.text=Content.second
            
        elif self.menu_bar.text=='millisecond':
            self.content_box.text=Content.milli_second
            
        elif self.menu_bar.text=='microsecond':
            self.content_box.text=Content.micro_second
            
            
            
        elif self.menu_bar.text=='nanosecond':
            self.content_box.text=Content.nano_second
            
            
        elif self.menu_bar.text=='Read Operation':
            self.content_box.text=Content.read_operation
            
        elif self.menu_bar.text=='Write Operation':
            self.content_box.text=Content.write_operation
            
        elif self.menu_bar.text=='Append Operation':
            self.content_box.text=Content.append_operation
            
        elif self.menu_bar.text=='Number System':
            self.content_box.text=Content.number_system
            
            
        elif self.menu_bar.text=='Binary Number System':
            self.content_box.text=Content.binary
            
        elif self.menu_bar.text=='Octal Number System':
            self.content_box.text=Content.octal
            
        elif self.menu_bar.text=='Decimal Number System':
            self.content_box.text=Content.decimal
      
            
            
            
        elif self.menu_bar.text=='HexaDecimal Number System':
            self.content_box.text=Content.hexadecimal
            
            
        elif self.menu_bar.text=='IP Address':
            self.content_box.text=Content.ip_address
            
        elif self.menu_bar.text=='MAC Address':
            self.content_box.text=Content.mac_address
            
            
            
            
            

class app_class(App):
    def build(self):
        return computer_terms()
        
if __name__=='__main__':
    app_class().run()