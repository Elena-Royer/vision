import os, sys
import platform
import mainLinux
import mainWin
from configure      import colors, init
from configure	    import clear, moveCursor
from pathlib		import Path
from fileType	    import fileType as FT
from fileType	    import readfile as RT
from configure      import screenConfig, colors, init
 

def visionEditor( ):
    # bg color 
    c_bg                   = init.init.bold + colors.bg.rgb(10, 10, 10)
    # fg color 
    c_fg                   = init.init.bold + colors.fg.rbg(255, 255, 255)
    # building color 
    color                  = c_bg + c_fg
    # get root path 
    root	= os.path.abspath(os.curdir)

    # path parent
    s = Path(__file__).resolve().parents[2]

    # get system name
    system  = platform.system()

    # get arguments 
    arg	 = sys.argv

    # coustomized terminal 
    terminal = "monokai"
    
    # get screen coordinate (x_max, y_max)
    max_x, max_y  = screenConfig.cursorMax()
    
    # set color 
    color = colors.fg.rbg(255,0,0) + init.init.bold+init.init.blink
    reset = init.init.reset
    c_bg  = colors.bg.white_L
    
    # initilization of writeData
    writeData = {"data" : [], "FileName" : None, "action" : False}
        
    if system in ['Windows', "Linux", "MacOS"]: 
        if   len(arg) == 1 : 
            termios, language   = "none", "unknown"
            data				= {"writing" : [""], "string" : [""], "input" : [], "color" : {"color" : [color], "m" : [0], "n" : [0], "locked": [False]}}
        elif len(arg) == 2 : 
            if arg[1]: 
                ext = FT.file(arg[1])
                if ext is not None : 
                    termios, language = terminal, ext
                    if system == "Windows" :  name = root + f"\\{arg[1]}"
                    else:  name = root + f"/{arg[1]}"
                    
                    #if os.stat(name) == 0 :  data = RT.readFile(fileName=name, termios=termios, language=language)
                    #else:  data = {} 
                    
                    data					= RT.readFile(fileName=name, termios=termios, language=language)
                    writeData["FileName"]   = arg[1]
                    writeData["data"]	    = data['string'].copy()
                    writeData["action"]	    = True     
                else: termios, language = "none", "unknown"
            else : termios, language = "none", "unknown"
        elif len(arg) == 3 : pass 

        if max_x > 50:
            if max_y > 20 :
                if   system == "Windows"	: mainWin.IDE(termios=termios, lang=language).VISION(importation=data, writeData =  writeData, path = root)
                elif system == "Linux"	    : mainLinux.IDE(termios=termios, lang=language).VISION(importation=data, writeData =  writeData, path = root)
                else: 
                    string = f" VISION is not distributed for {system} platform "
                    print(c_bg + color + string + reset)
            else: 
                string = f" Increase the width of screen at least 20  : width = {max_y} "
                print(c_bg + color + string + reset)
        else:
            string = f" Increase the height of screen at least 50 : height = {max_x} "
            print(c_bg + color + string + reset)
    else: pass

    
if __name__ == '__main__':
    sys.stdout.write(clear.clear.screen(2)+moveCursor.cursor.TO(0,0))
    visionEditor()