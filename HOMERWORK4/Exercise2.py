a = {"RED": (255,0,0),"BLUE":(0,0,255),"BLACK":(3,1,1),"WHITE":(255,255,255),"YELLOW":(255,255,0),"GREEN":(0,255,0),"ORANGE":(255,165,0),"PINK":(255,192,203)}
print("Введите название цвета для получения его RGB:")
b = input()
print("RGB для вашего цвета {} равен: {}".format(b,a.get(b)))