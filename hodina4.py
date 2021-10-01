w = 3
h = 3
pole = [" "]*w*h
pole2 = [" "]*w*h
p = "-"
mainloop = True
xd = 0
gox = True
goo = True

def result(): 
    for c in range(h):
        r = ""
        for i in range(w):
            if i != w-1:
                r += pole[c*w+i]+"|"
            else:
                r += pole[c*w+i]
                print(r)
        if c != h-1:
            print(p*(w*2-1))
    return
            
def check():
    for checking in range (w*h):
        if pole[checking] != " ":
            if pole2[checking] == "1":
                if (pole[checking-1] == pole[checking] == pole[checking+1]):
                    print("Vyhral", pole[checking])
                    return False
            if pole2[checking] == "2":
                if (pole[checking-w] == pole[checking] == pole[checking+w]):
                    print("Vyhral", pole[checking])
                    return False
            if pole2[checking] == "3":
                if (pole[checking-w] == pole[checking] == pole[checking+w]):
                    print("Vyhral", pole[checking])
                    return False
                if (pole[checking-1] == pole[checking] == pole[checking+1]):
                    print("Vyhral", pole[checking])
                    return False
                if (pole[checking-w-1] == pole[checking] == pole[checking+w+1]):
                    print("Vyhral", pole[checking])
                    return False
                if (pole[checking+w-1] == pole[checking] == pole[checking-w+1]):
                    print("Vyhral", pole[checking])
                    return False
    return True

def init():
    for height in range(h):
        if height != 0:
            if height != h-1:
                pole2[w*height] = "2"
                pole2[(w*(height+1))-1] = "2"
    for p2 in range(w*h):
        if p2 == 0:
            pole2[p2] = "0"
        if p2 == (w-1):
            pole2[p2] = "0"
        if p2 == (w*(h-1)):
            pole2[p2] = "0"
        if p2 == w*h-1:
            pole2[p2] = "0"
        if w-1 > p2 > 0:
            pole2[p2] = "1"
        if w*h-1 > p2 > (w*(h-1)):
            pole2[p2] = "1"
        if pole2[p2] == " ":
            pole2[p2] = "3"
    return

def playx(x,y):
    if pole[(((w*(x-1))+y)-1)] == " ":
        pole[(((w*(x-1))+y)-1)] = "x"
        return False
    else:
        print("Miesto je zabrané skús ešte raz!")
        return True

def playo(x,y):
    if pole[(((w*(x-1))+y)-1)] == " ":
        pole[(((w*(x-1))+y)-1)] = "o"
        return False
    else:
        print("Miesto je zabrané skús ešte raz!")
        return True

init()

while mainloop:
    if xd == 0:
        while gox:
            gox = playx(int(input("Zadaj X súradnicu: ")), int(input("Zadaj Y súradnicu: ")))
        result()
        mainloop = check()
        xd = 1
        gox = True
    else:
        while goo:
            goo = playo(int(input("Zadaj X súradnicu: ")), int(input("Zadaj Y súradnicu: ")))
        result()
        mainloop = check()
        xd = 0
        goo = True