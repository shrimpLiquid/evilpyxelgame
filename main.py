import pyxel  
class App:
    def __init__(self):
        pyxel.init(60, 60,fps=6)

        pyxel.run(self.update, self.draw)
        

    def update(self):
        pass

        
    def draw(self):
        pyxel.cls(pyxel.frame_count%16)

        

                
        

App()