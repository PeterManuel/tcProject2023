import kivy

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse,Line
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse,Line   
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen



class MainScreen(Screen):
    pass


class ExecutingScreen(Screen):
    pass

class MyGridLayout(GridLayout):
    pass


class TapeWidget(Widget):
    def __init__(self, **kwargs):
        super(TapeWidget, self).__init__(**kwargs)
        with self.canvas:
            print("linhas turing app")
            print(self.pos_hint)
            l=Line(rectangle=[100,400,100,100])
    



class StateWidget(Button):
    def __init__(self, **kwargs):
        super(StateWidget, self).__init__(**kwargs)
        self.line_list=[]

class MyWidget(Widget):

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.btn_list=[]
        self.bt=None
        self.state=0
        self.link=[]
        self.linked=[]
        self.touched=None

    def say(instance):
        print("you touch me---")
    
    def collide_button(self,touch):
        for btn in self.btn_list:
            if btn.collide_point(touch.x, touch.y):
                self.link.append([(btn.pos[0]+12),(btn.pos[1]+12)])
                self.linked.append(btn)
                self.touched=btn
                print("without",btn.pos[0])
                print(btn.pos[0]+5)
      
                return True
        return False

    def on_touch_down(self, touch):
        
        if len(self.btn_list) > 0 :
            if self.collide_point(touch.x, touch.y) and not self.collide_button(touch):
                with self.canvas:
                    Color(1,1,0)
                    d = 30.
                    self.btn_list.append(StateWidget(text="q"+str(self.state), pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                    )
                    self.btn_list[-1].bind(on_press=self.say)
                    print("botao criado")
                    self.state+=1
                self.link=[]
                self.linked=[]
                self.touched=None
        else:
            if self.collide_point(touch.x, touch.y):
                with self.canvas:
                    Color(1,1,0)
                    d = 30.
                    self.btn_list.append(StateWidget(text="q"+str(self.state), pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                    )
                    self.btn_list[-1].bind(on_press=self.say)
                    print('botão criado')
                    self.state+=1
                    self.link=[]
                    self.linked=[]
                    self.touched=None
        if len(self.link)==2:
            with self.canvas.before:
                print("linhas",self.link)
                l=Line(points=self.link,width=2)
                self.linked[0].line_list.append((l,0))
                self.linked[1].line_list.append((l,2))
                self.link=[]
                self.linked=[]
                self.touched=None

    def on_touch_move(self, touch):
        print("toquei",touch)
        self.link=[]
        self.linked=[]
        if(self.touched):
            self.touched.pos=[touch.x,touch.y]
            
            for linha in self.touched.line_list:
                print("linhs",linha[0].points)
                newLines=linha[0].points

                newLines[linha[1]]=self.touched.pos[0]+12
                newLines[linha[1]+1]=self.touched.pos[1]+12
                linha[0].points=newLines
           



class TuringApp(App):
    def  build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(ExecutingScreen(name='executing'))
        return sm
       
        #return Label(text='Hello Theorical computation')
 

if __name__=="__main__":
    Window.clearcolor = get_color_from_hex('#101216')
    TuringApp().run()
