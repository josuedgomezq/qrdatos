from pickle import FALSE
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3

lista=[]

Builder.load_file('main.kv')
class MyGridLayout(Widget):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__()

    def leer(self):
        
        #conexion con la base de datos
        try:
            conexion = sqlite3.connect('basedatos.db')
    
            
        except sqlite3.Error as error:
            print('Se ha producido un error al crear la conexión:', error)
        
        
        zbarcam=self.zbarcam
        id=str(zbarcam.symbols)
        zbarcam.stop()
        zbarcam.resolution=(700,700)
        zbarcam.index=0
        sql = "SELECT * FROM usuario WHERE id = ?;" # selecciono el valor clave de la base de datos, para realizar una busqueda de una lista especifica

        cursor = conexion.cursor()
        cursor.execute(sql, ([id]))
    
        registros = cursor.fetchall()
    
        for r in registros:
            print("registro")
            print(r)
            self.ids.registro.text=f'Registro {r}'
        
        
        

    def press(self):

        lista1=[]
        print('base1')
        try:
            conexion = sqlite3.connect('basedatos.db')
    
            
        except sqlite3.Error as error:
            print('Se ha producido un error al crear la conexión:', error)
        
        #se uso la receta pyqt 881
        '''sql = CREATE TABLE usuario(
            id INTEGER NOT NULL
        );
    
      
        
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()'''
       
        
        zbarcam=self.zbarcam
        id=str(zbarcam.symbols)
        
        
        if(zbarcam.symbols==[]):
            print( 'Uno o más campos están vacíos')        
        
        
        print("id")
        print(id)
        lista.append(str(zbarcam.symbols))

        print(lista)
        x=len(lista)
        print(x)
        if lista[x-2]==lista[x-1]:
            a=str(1)
            self.ids.name_label.text=f'igual {a}'
        else:
            b=2
            self.ids.name_label.text=f'diferente {b}'
        
        c=str(212)
        print(c)
        sql = 'INSERT INTO usuario VALUES (?);'

        cursor = conexion.cursor()
        cursor.execute(sql, ([id]))
    
        conexion.commit()
            
        if conexion:
            conexion.close()
            
        zbarcam.start()

              


class QrApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    QrApp().run()