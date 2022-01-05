import os

from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel

import Global
import main

os.environ['KIVY_IMAGE'] = 'pil,sdl2'

# kivy program
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()
screen_helper = """
ScreenManager:
    HomeScreen:
    FileScreen:
    Par1Screen:
    Par2Screen:
    ResultScreen:
    ItScreen:
  

<CustomDropDown>:
    Button:
        text: 'LU Decomposition'
        size_hint_y: None
        height: 44
        on_release: root.select('LU Decomposition')

    Button:
        text: 'gauss_elimination'
        size_hint_y: None
        height: 44
        on_release: root.select('gauss_elimination')
    Button:
        text: 'gauss jordan'
        size_hint_y: None
        height: 44
        on_release: root.select('gauss jordan')
    Button:
        text: 'gauss seidel'
        size_hint_y: None
        height: 44
        on_release: root.select('gauss seidel')                       
    
<HomeScreen>:
    name: 'home'

    Image: 
        source: "image.png"
        pos_hint: {'x':0,'y':0.5}
        size_hint: (1,0.5)
    Label:
        text: "Enter the equation"
        font_size: 18
        pos_hint: {'center_x':0.5,'center_y':0.46}
        color : "#135466"
    TextInput:
        id: input
        multiline: False
        padding_y: (20,20)
        pos_hint: {'center_x':0.5,'center_y':0.37}
        size_hint: (0.5,0.1)   
        on_text: app.data = self.text
    Button:
        id: button
        text: "Next"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.5,'center_y':0.09}
        background_color : (1.0, 0.0, 0.0, 1.0)
        on_press:  root.callback() 
        on_release:   app.callback()
    Button:
        id: button
        text: "Or read from file"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.85,'center_y':0.09}
        background_color : (1.0, 0.0, 0.0, 1.0)
        on_press:  root.manager.current = 'file'
            
        
    
<FileScreen>:
    name:'file'
    Label:
        text: "Choose a file"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.25,'center_y':0.7}
        color : "#000000"  
    FileChooserIconView:
        id: filechooser
        canvas.before:
            Color:
                rgb: 0.13,0,0
            Rectangle:
                pos: self.pos
                size: self.size
        on_selection: root.selected(filechooser.selection)

    
<Par1Screen>:
    name: 'par'
    Label:
        text: "X-Lower"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.25,'center_y':0.7}
        color : "#000000"  
    Label:
        text: "X-Upper"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.75,'center_y':0.7}
        color : "#000000"  
    TextInput:
        id: xl
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.25,'center_y':0.6}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text    
    TextInput:
        id: xu
        font_size: 25
        
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.75,'center_y':0.6}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text    
    Label:
        id: lbl
        text: "Percision"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.25,'center_y':0.35}
        color : "#000000"  
    Label:
        text: "Max Iterations"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.75,'center_y':0.35}
        color : "#000000"
        
    TextInput:
        id: es
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.25,'center_y':0.25}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text    
    TextInput:
        id: imax
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.75,'center_y':0.25}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text      
    Button:
        id: button
        text: "Find root"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.5,'center_y':0.09}
        background_color : (1.0, 0.0, 0.0, 1.0)
        on_press:  root.callback()       
        on_release: root.manager.current = 'result'       

<Par2Screen>:
    name: 'par2'
    Label:
        text: "Xi"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.25,'center_y':0.7}
        color : "#000000"  

    TextInput:
        id: xi
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.25,'center_y':0.6}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text    

    Label:
        id: lbl
        text: "Percision"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.25,'center_y':0.35}
        color : "#000000"  
    Label:
        text: "Max Iterations"
        font_size: 18
        font_style: "H1"
        pos_hint: {'center_x':0.75,'center_y':0.35}
        color : "#000000"
        
    TextInput:
        id: es
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.25,'center_y':0.25}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text    
    TextInput:
        id: imax
        font_size: 25
        multiline: False
        padding_y: (10,10)
        padding_x: (80,20)
        pos_hint: {'center_x':0.75,'center_y':0.25}
        size_hint: (0.25,0.1)   
        on_text: app.data = self.text      
    Button:
        id: button
        text: "Find root"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.5,'center_y':0.09}
        background_color : (1.0, 0.0, 0.0, 1.0)
        on_press:  root.callback()       
        on_release: root.manager.current = 'result' 
                             
                    
        
<ResultScreen>:
    name: 'result'   
    Label:
        id: lbl1
        text: ''
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.7,'center_y':0.8}
        color : "#013543"
    Label:
        text: 'Result:'
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.2,'center_y':0.8}
        color : "#013543"        
        
    Label:
        id: lbl2
        text: ''
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.7,'center_y':0.7}
        color : "#013543" 
    Label:
        text: 'Error Approximations:'
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.2,'center_y':0.7}
        color : "#013543"                 
        
    Label:
        id: lbl3
        text: ''
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.7,'center_y':0.6}
        color : "#013543"  
    Label:
        text: 'No. of Iterations:'
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.2,'center_y':0.6}
        color : "#013543"                  
    Label:
        id: lbl4
        text: ''
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.7,'center_y':0.5}
        color : "#013543"  
    Label:
        text: 'Runtime:'
        font_size: 25
        font_style: "H1"
        pos_hint: {'center_x':0.2,'center_y':0.5}
        color : "#013543"                          
                
    Button:
        id: button
        text: "See iterations"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.5,'center_y':0.09}
        background_color : (1.0, 0.0, 0.0, 1.0)   
        on_release: root.manager.current = 'it'     


<ItScreen>:
    name: 'it'
    Button:
        id: button
        text: "go back"
        size_hint: (0.2,0.09)
        pos_hint: {'center_x':0.5,'center_y':0.07}
        background_color : (1.0, 0.0, 0.0, 1.0)   
        on_press: root.manager.current = 'result' 
    

<ExampleViewer>:
    viewclass: 'Button'  # defines the viewtype for the data items.
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    size_hint: (1,0.85)
    pos_hint: {'center_x':0.5,'center_y':0.55}
  
    RecycleBoxLayout:
        color:(0, 0.7, 0.4, 0.8)
        default_size: None, dp(56)
  
        # defines the size of the widget in reference to width and height
        default_size_hint: 1, None 
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical' # defines the orientation of data items       
"""


class FileScreen(Screen):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        # print("selected: %s" % filename[0])
        f = open(filename[0], "r")
        Global.EQN = f.readline()
        Global.EQN = Global.EQN.replace('\n', '')
        Global.MY_DATA = f.readline()
        if Global.MY_DATA == 'Bisection\n' or Global.MY_DATA == 'False Position\n' or Global.MY_DATA == 'Secant\n':
            xr = ''
            xl = float(f.readline())
            xu = float(f.readline())
            es = float(f.readline())
            imax = int(f.readline())
            print(Global.EQN)
            print(xl)
            print(xu)
            print(es)
            print(imax)
            print(Global.MY_DATA)
            if (Global.MY_DATA == 'Bisection\n'):

                (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.bisection(xl, xu, es,
                                                                                                             imax)
            elif (Global.MY_DATA == 'False Position\n'):
                (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.false_position(xl,
                                                                                                                  xu,
                                                                                                                  es,
                                                                                                                  imax)
            elif (Global.MY_DATA == 'Secant\n'):

                (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.secant(xl, xu, es,
                                                                                                          imax)

            Global.MY_DATA = str(xr)
            print(Global.MY_DATA)
            # screen2_instance.set_viewer()
            it_instance = self.parent.get_screen('it')
            it_instance.set_viewer()

            result_instance = self.parent.get_screen('result')
            result_instance.change_label()
            self.manager.current = 'result'
        elif (Global.MY_DATA == 'Fixed Point\n' or Global.MY_DATA == 'Newton-Raphson\n'):
            xr = ''
            xi = float(f.readline())
            es = float(f.readline())
            imax = int(f.readline())
            if (Global.MY_DATA == 'Fixed Point\n'):
                (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.fixed_point(xi, es,
                                                                                                               imax)
            elif (Global.MY_DATA == 'Newton-Raphson\n'):
                (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.newton_raphson(xi,
                                                                                                                  es,
                                                                                                                  imax)
            Global.MY_DATA = str(xr)
            it_instance = self.parent.get_screen('it')
            it_instance.set_viewer()

            result_instance = self.parent.get_screen('result')
            result_instance.change_label()
            self.manager.current = 'result'


class ItScreen(Screen):

    def set_viewer(self):
        self.viewer = ExampleViewer()
        self.add_widget(self.viewer)


class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in Global.OUT_ITERATIONS]


class Tab(TabbedPanel):
    pass


class CustomDropDown(DropDown):
    pass


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()

        # Creating a self widget button
        self.mainbutton = Button(text='Choose Method',
                                 size_hint_x=0.5, size_hint_y=0.1, background_color=(1.0, 0.0, 0.0, 1.0),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.23}
                                 )

        # Added button to FloatLayout so inherits this class
        self.add_widget(self.mainbutton)

        # Adding actions
        # If click
        self.mainbutton.bind(on_release=self.dropdown.open)

        # root.select on_select called
        self.dropdown.bind(on_select=lambda \
                instance, x: setattr(self.mainbutton, 'text', x))

    def callback(self):
        Global.MY_DATA = self.mainbutton.text
        Global.EQN = self.ids.input.text
        return


class Par2Screen(Screen):
    def callback(self):
        xr = ''
        xi = float(self.ids.xi.text)
        es = ''
        imax = ''
        if self.ids.es.text != '':
            es = float(self.ids.es.text)
        if self.ids.imax.text != '':
            imax = int(self.ids.imax.text)
        if Global.MY_DATA == 'Fixed Point':
            (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.fixed_point(xi, es, imax)
        elif Global.MY_DATA == 'Newton-Raphson':
            (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.newton_raphson(xi, es,
                                                                                                              imax)
        Global.MY_DATA = str(xr)
        it_instance = self.parent.get_screen('it')
        it_instance.set_viewer()

        result_instance = self.parent.get_screen('result')
        result_instance.change_label()


class Par1Screen(Screen):
    def callback(self):
        xr = ''
        xl = float(self.ids.xl.text)
        xu = float(self.ids.xu.text)
        es = ''
        imax = ''
        if (self.ids.es.text != ''):
            es = float(self.ids.es.text)
        if (self.ids.imax.text != ''):
            imax = int(self.ids.imax.text)
        print(Global.MY_DATA)
        if (Global.MY_DATA == 'Bisection'):
            (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.bisection(xl, xu, es,
                                                                                                         imax)
        elif (Global.MY_DATA == 'False Position'):
            (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.false_position(xl, xu,
                                                                                                              es, imax)
        elif (Global.MY_DATA == 'Secant'):

            (xr, Global.OUT_EA, Global.OUT_ITS, Global.OUT_ITERATIONS, Global.OUT_TIME) = main.secant(xl, xu, es, imax)

        Global.MY_DATA = str(xr)

        # screen2_instance.set_viewer()
        it_instance = self.parent.get_screen('it')
        it_instance.set_viewer()

        result_instance = self.parent.get_screen('result')
        result_instance.change_label()


class ResultScreen(Screen):

    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

    # self.tab = Tab()
    # self.add_widget(self.tab)

    def change_label(self):
        self.ids.lbl1.text = str(Global.MY_DATA)
        self.ids.lbl2.text = str(Global.OUT_EA)
        self.ids.lbl3.text = str(Global.OUT_ITS)
        self.ids.lbl4.text = str(Global.OUT_TIME)
    # def set_viewer(self):
    #   self.viewer = ExampleViewer()
    #  self.add_widget(self.viewer)


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultScreen(name='result'))


class RootFinder(App):
    Window.clearcolor = (1, 1, 1, 1)
    data = StringProperty('')

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def callback(self):
        method = Global.MY_DATA
        print(method)
        if (method == 'Fixed Point' or method == 'Newton-Raphson'):
            self.root.current = 'par2'
        else:
            self.root.current = 'par'


if __name__ == "__main__":
    RootFinder().run()
# root.manager.get_screen('result').label.text = str(self.text)
