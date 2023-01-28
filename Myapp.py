from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
KV="""
MDScreen:
     MDBoxLayout:
          orientation:"vertical"
          MDTopAppBar:
               title:'Myapp'
          tela:
<Card>:
     orientation:'vertical'
     id:card
     size_hint:.9,.9
     pos_hint:{'center_x':.5,'center_y':.5} 
     MDLabel:
          text:"OLÁ MUNDO"        
          halign: "center"
     MDIconButton:
          icon:"close"
          pos_hint:{'center_x':.5} 
          on_release:root.fecha()
         
<tela>:
     MDFloatLayout:
          MDRaisedButton:
               text:'clique em mim'
               pos_hint:{'center_x':.5,'center_y':.5}
               on_release:root.Crad()

"""
class tela(MDFloatLayout):
    def Crad(self):
        self.add_widget(Card())
class Card(MDCard):
    def fecha(self):
        self.parent.remove_widget(self)
class Myapp(MDApp):
   def build(self):
        return Builder.load_string(KV)
if __name__ =='__main__':        
     Myapp().run()        