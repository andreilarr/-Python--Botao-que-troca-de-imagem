from graphics import *

def main():

    win = GraphWin("Fotos", 500, 400)
    cachorro = Image(Point(350,250), "cachorro1.png")
    cachorro.draw(win)
    botao = Image(Point(100,150), "botao.png")
    botao.draw(win)
    while win.closed == False:
        mouse = win.checkMouse()
        if (mouse != None):
            if mouse==(100, 147) or mouse==(98, 149) or mouse==(102, 145) or mouse==(103, 145) or mouse==(101, 151) or mouse==(99, 145):
                cachorro.undraw()
                cachorro2 = Image(Point(350,250), "cachorro2.png")
                cachorro2.draw(win)
            print(mouse)

main()