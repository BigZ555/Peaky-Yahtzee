from tkinter import*
import random

#from tkextrafont import Font


bigz = Tk()
bigz.geometry("1920x1080")
bigz.attributes('-fullscreen', True)
bigz.resizable(False, False)
bigz.iconbitmap(default='assets/peakyhat.ico')
bigz.title("YAHTZEE")

#Fontok
afont = 'RomanWoodTypeJNL 55'
bfont = 'RomanWoodTypeJNL 45'
cfont = 'RomanWoodTypeJNL 30'
tablazatfont = 'RomanWoodTypeJNL 25'
rangfont = 'RomanWoodTypeJNL 40'


WIDTH, HEIGHT = 1920, 1080

fajlhely = 'assets/adatok.txt'

#szinek
betuszin = "#3b4b54"
barnas = '#44372b'
fejlecalattbezs = '#807556'
szurkebetu = '#6d6d6d'
fejlecszin = "#393632"
szurke = '#6d6d6d'
tablazatalap = '#5d553d'
#kepek
bg = PhotoImage(file = 'assets/bg.png')
bg2 = PhotoImage(file = 'assets/bg1.png')
peakyhat = PhotoImage(file = 'assets/menu.png')
menu2 = PhotoImage(file = 'assets/menurajta.png')
kilep1 = PhotoImage(file='assets/kilep_.png')
kilep2 = PhotoImage(file='assets/kileprajta_.png')
k1 = PhotoImage(file = 'assets/k1.png')
k2 = PhotoImage(file = 'assets/k2.png')
k3 = PhotoImage(file = 'assets/k3.png')
k4 = PhotoImage(file = 'assets/k4.png')
k5 = PhotoImage(file = 'assets/k5.png')
k6 = PhotoImage(file = 'assets/k6.png')
szabnyil = PhotoImage(file = 'assets/nyil.png')
szabnyil2 = PhotoImage(file = 'assets/nyilrajta.png')

kockak = [k1,
          k2,
          k3,
          k4,
          k5,
          k6]

kombinaciok = [
    "Tetszoleges",
    "Pár",
    "Drill",
    "Két pár",
    "Kis póker",
    "Full",
    "Kis sor",
    "Nagy sor",
    "Nagy póker"
]

kmbinaciok = [
    "Tetszoleges kombináció",
    "Pár - egyformaérték",
    "Drill - 3 egyforma érték",
    "Két pár - 2-2 egyforma érték",
    "Kis póker - 4 egyforma érték",
    "Full - 2 egyforma + 3 egyforma érték",
    "Kis sor (1,2,3,4,5)",
    "Nagy sor (2,3,4,5,6)",
    "Nagy póker - 5 egyforman érték"
    ]

pntertekek = [
    "az 5 kocka pontértékeinek összege",
    "a két egyforma érték összege",
    "a három egyforma érték összege",
    "a két-két egyforma érték összege",
    "a négy egyforma érték összege",
    "az értékek összege",
    "15 pont",
    "20 pont",
    "50 pont"
    ]

lehkombinaciok = [
    "Tetszoleges",
    "Pár",
    "Drill",
    "Két pár",
    "Kis póker",
    "Full",
    "Kis sor",
    "Nagy sor",
    "Nagy Póker"
    ]

gombok_lista = []
jatdobszam = []

canvas = Canvas(bigz, width = WIDTH, height = HEIGHT)
canvas.pack()

jatekospontszam = 0
shelbypontszam = 0

kov = True
dupla = False
tripla = False
nagysork = False
kissork = False
ketpaar = True
par1, par2 = 0,0
yahtzee = False
tripla = False
kvintupla = False


def kezdes():
    global entry1
    canvas.create_image(0,0,anchor = NW, image = bg, tags = "kezd")
    entry1 = Entry(canvas, width=20, font = 'Arial 40', bg =barnas, fg=szurkebetu)
    entry1.place(x = 250, y = 780)
    entry1.insert(0, "játékosnév")
    entry1.bind('<FocusIn>', entry_focus_in)
    entry1.bind('<FocusOut>', entry_focus_out)
    canvas.bind_all('<Return>', lambda event: main(event))

def entry_focus_in(event):
    if entry1.get() == "játékosnév":
        entry1.delete(0, 'end')
        entry1.config(fg = "gray")

def entry_focus_out(event):
    if entry1.get() == '':
        entry1.insert(0, "játékosnév")
        entry1.config(fg = "gray")

def main(event):
    global jatekosnev
    jatnev = entry1.get()
    if len(jatnev) > 16:
        jatekosnev = jatnev[0:15]
    else:
        jatekosnev = jatnev
    entry1.destroy()
    canvas.delete()
    graffelulet()


def szvggomb(x,y,text,bcolor,fcolor,cmd):     
    gomb1 = Button(canvas,text=text, 
                        font='Arial 10',
                        width=27, 
                        height=1, 
                        fg='#262626', 
                        border=0, 
                        bg=fcolor, 
                        activeforeground='#262626', 
                        activebackground=bcolor, 
                        command=cmd)
    gomb1.place(x=x,y=y)


def kilepra(event):
    kilepgomb.config(image=kilep2)

def kileple(event):
    kilepgomb.config(image = kilep1)

def menura(event):
    menugomb.config(image=menu2)

def menule(event):
    menugomb.config(image=peakyhat)

def kilepes():
    bigz.destroy()

def kilepes2(event):
    bigz.destroy()

def dobra(event):
    canvas.delete("dob")
    canvas.create_line(29, 862, 29, 938, fill="white",  width = 3,tags="dob")
    canvas.create_line(115, 862, 115, 938, fill="white",width = 3,tags="dob")
    canvas.create_line(29, 862, 115, 862, fill="white", width = 3,tags="dob")
    canvas.create_line(29, 938, 115, 938, fill="white", width = 3,tags="dob")

def doble(event):
    canvas.delete("dob")
    canvas.create_line(29, 862, 29, 938, fill=szurke,  width = 3,tags="dob")
    canvas.create_line(115, 862, 115, 938, fill=szurke,width = 3,tags="dob")
    canvas.create_line(29, 862, 115, 862, fill=szurke, width = 3,tags="dob")
    canvas.create_line(29, 938, 115, 938, fill=szurke, width = 3,tags="dob")

def menubezar():
    menugomb.config(command=menu)
    canvas.delete("menu")
    mn1.destroy()

def menubezar2(event):
    menugomb.config(command=menu)
    canvas.delete("menu")
    mn1.destroy()

def menugombok(x,y, text, cmd):
    gomb1 = Button(mn1,
                   text = text, 
                   bg= fejlecalattbezs,
                   fg = "white",
                   font ='RomanWoodTypeJNL 40',
                   compound='top',
                   command= cmd,
                   height = 0, 
                   width = 27,
                   border= 0
                   )
    gomb1.place(x = x, y = y)

def gomboktorles():
    kilepgomb.destroy()
    dobasgomb.destroy()
    menugomb.destroy()

def ujjatek():
    global kockak, shelbypontszam, jatekospontszam, lehkombinaciok, parancsok
    #mn1.destroy()   
    jatekospontszam = 0
    shelbypontszam = 0
    kockak = [k1,
          k2,
          k3,
          k4,
          k5,
          k6]
    lehkombinaciok = [
        "Tetszoleges",
        "Pár",
        "Drill",
        "Két pár",
        "Kis póker",
        "Full",
        "Kis sor",
        "Nagy sor",
        "Nagy Póker"
        ]

    shelbylehet = [
        "Tetszoleges",
        "Pár",
        "Drill",
        "Két pár",
        "Kis póker",
        "Full",
        "Kis sor",
        "Nagy sor",
        "Nagy Póker"
        ]
    parancsok = [
        tetszoleges,
        par,
        drill,
        ketpar,
        kispoker,
        full,
        kissor,
        nagysor,
        nagypoker
        ]
    gombtorles()
    gomboktorles()
    kezdes()

def gomb(x, y, text, bcolor, fcolor, cmd):
    global gombok
    gombok = Button(canvas, 
                    text = text, 
                    width = 20, 
                    height = 1, 
                    fg = fcolor,
                    font=cfont,
                    border=0, 
                    bg=bcolor, 
                    activeforeground='#262626', 
                    activebackground="white",
                    command=cmd)
    gombok.place(x=x,y=y)
    gombok_lista.append(gombok)

def kilepesgombra(event):
    canvas.delete("veggomb2")
    vegcanvas.create_rectangle(849, 526, 750, 591, fill="white", outline='', tags = 'veggomb2')

def kilepesgomble(event):
    canvas.delete("veggomb2")
    vegcanvas.create_rectangle(849, 526, 750, 591, fill=szurke, outline='', tags = 'veggomb2')

def ujjatekgombra(event):
    canvas.delete("veggomb1")
    vegcanvas.create_rectangle(26, 526, 136, 591, fill="white", outline='', tags = 'veggomb1')

def ujjatekgomble(event):
    canvas.delete("veggomb1")
    vegcanvas.create_rectangle(26, 526, 136, 591, fill=szurke, outline='', tags = 'veggomb1')

def visszagombra(event):
    canvas.delete("veggomb3")
    vegcanvas.create_rectangle(396, 526, 481, 591, fill="white", outline='', tags = 'veggomb3')

def visszagomble(event):
    canvas.delete("veggomb3")
    vegcanvas.create_rectangle(396, 526, 481, 591, fill=szurke, outline='', tags = 'veggomb3')

def vegkilepes(event):
    veg.destroy()
    menu()

def okgombra(event):
    rangcanvas.delete("okgomb")
    rangcanvas.create_rectangle(202, 132, 298, 188, fill="white", tags = "okgomb")

    
def okgomble(event):
    rangcanvas.delete("okgomb")
    rangcanvas.create_rectangle(202, 132, 298, 188, fill=szurke, tags = "okgomb")    

def felkerulttorles(event):
    felrang.destroy()

def felkerultranglistara():
    global rangcanvas, felrang
    felrang = Frame(bigz, width = 500, height = 200, bd = 0, bg = fejlecszin)
    felrang.place(x = WIDTH//2, y = HEIGHT//2, anchor = 'center')
    rangcanvas = Canvas(felrang, width = 500, height = 200, bg = fejlecszin)
    rangcanvas.pack()
    rangcanvas.create_rectangle(202, 132, 298, 188, fill=szurke, tags = "okgomb")
    okgomb = Button(felrang, text = "ok", font = tablazatfont, bd = 0, bg = fejlecalattbezs, fg="white", command=lambda:(felrang.destroy()))
    okgomb.place(x = 250, y = 160, anchor = 'center', width = 90, height = 50)
    okgomb.bind('<Enter>', okgombra)
    okgomb.bind('<Leave>', okgomble)
    felrang.bind_all('<Return>', felkerulttorles)

def eredmenybetoltes():
    score = 0
    global vegcanvas, veg
    x, y = 20,100
    veg = Frame(bigz, width=875, height=600, bg=fejlecszin)
    veg.place(x=550, y=250)
    vegcanvas = Canvas(veg, width=874, height=599, bg=fejlecszin, highlightthickness=3,
                       highlightbackground=fejlecalattbezs, relief='flat')
    vegcanvas.pack()
    try:
        with open("data.txt", "r") as file:
            data = [line.strip() for line in file]
    except FileNotFoundError:
        data = []
    for i, entry in enumerate(data):
        if i <10:
            name_start = entry.find("Jatekos:") + len("Jatekos:")
            name_end = entry.find(",pontszam")
            name = entry[name_start:name_end]

            score_start = entry.find("pontszam:") + len("pontszam:")
            score = entry[score_start:]

            rank_start = entry.find("Rank:") + len("Rank:")
            rank_end = entry.find(",Jatekos")
            rank = entry[rank_start:rank_end]
            Label(veg, bg=fejlecszin, fg='white', text=f"{rank}. {name} {score}", font=rangfont).place(x=x, y=y, anchor=NW)
            y = y + 80
            if i == 4:
                x, y = 437.5,100
    print(len(lehkombinaciok))
    if int(jatekospontszam) >= int(score) and len(lehkombinaciok) == 0:
        felkerultranglistara()
    
    Label(veg, bg=fejlecszin, fg='white', text='Vége a játéknak', font=bfont).place(x=437.5, y=16, anchor=N)
    vegcanvas.create_rectangle(26, 526, 136, 591, fill=szurke, outline='', tags = 'veggomb1')
    vegcanvas.create_rectangle(849, 526, 750, 591, fill=szurke, outline='', tags = 'veggomb2')
    vegcanvas.create_rectangle(396, 526, 481, 591, fill=szurke, outline='', tags = 'veggomb3')
    ujjatekgomb = Button(veg, text = "új játék", font = tablazatfont,bg = fejlecalattbezs, fg = "white", bd = 0, command=lambda: (veg.destroy(), ujjatek()))
    ujjatekgomb.place(x = 30, y = 530, anchor = NW)
    kilepesgomb = Button(veg, text = "kilépés", font =  tablazatfont, bg = fejlecalattbezs, fg = "white", bd = 0, command=kilepeskerdes)
    kilepesgomb.place(x = 845, y = 530, anchor = NE)
    visszagomb = Button(veg, text = "vissza", font = tablazatfont, bd = 0, bg = fejlecalattbezs, fg = "white", command = lambda:(veg.destroy(), menu()))
    visszagomb.place(x = 437.5, y = 530, anchor = N)
    ujjatekgomb.bind('<Enter>', ujjatekgombra)
    ujjatekgomb.bind('<Leave>', ujjatekgomble)
    kilepesgomb.bind('<Enter>', kilepesgombra)
    kilepesgomb.bind('<Leave>', kilepesgomble)
    visszagomb.bind('<Enter>', visszagombra)
    visszagomb.bind('<Leave>', visszagomble)
    veg.bind_all('<Escape>', vegkilepes)
    menugomb.config(command=None)
    kilepgomb.config(command=None)
    dobasgomb.config(command=None)

#400 477
def eredmenymentes(ujnyertes):
    try:
        with open("data.txt", "r") as file:
            data = [line.strip() for line in file]
    except FileNotFoundError:
        data = []

    data.append(f"Rank:0,Jatekos:{ujnyertes['nev']},pontszam:{ujnyertes['pont']}")

    rendezett_adat = sorted(data, key=lambda x: int(x.split(":")[-1]), reverse=True)

    rankozott_adat = [f"Rank:{i + 1},{player.split(',', 1)[1]}" for i, player in enumerate(rendezett_adat)]

    with open("data.txt", "w") as file:
        file.write("\n".join(rankozott_adat))

    print("Data updated and saved.")


def gameover():
    ujnyertes = {"nev": jatekosnev, "pont": jatekospontszam}
    eredmenymentes(ujnyertes)
    eredmenybetoltes()

def menu():
    global mn1
    mn1 = Frame(bigz, width = 875, height = 600, bg=fejlecszin)
    mn1.place(x = 550, y=250)
    menucanvas = Canvas(mn1, width = 874, height = 599, bg = fejlecszin,highlightthickness= 3, highlightbackground=fejlecalattbezs, relief='flat')
    menucanvas.pack()
    Label(mn1, bg = fejlecszin, fg = 'white',text = jatekosnev, font = tablazatfont).place(x = 31, y = 16)
    Label(mn1, bg = fejlecszin, anchor = NW, justify = 'center', fg = 'white',text = 'menu', font = bfont).place(x = 358, y = 16)
    Label(mn1, bg = fejlecszin, anchor = NW, justify = 'center', fg = 'white',text = 'BigZ Soft v 1.0', font = 'RomanWoodTypeJNL 12').place(x = 785, y = 575)
    #keretek
    x1, x2 = 160, 710
    y1, y2 = 117, 214
    for i in range(4):
        menucanvas.create_rectangle(x1, y1, x1 + 4, y2 + 5, fill = 'white', outline = "")
        menucanvas.create_rectangle(x1, y1, x2, y1 + 4, fill = 'white', outline = "")
        menucanvas.create_rectangle(x1, y2, x2, y2 + 5, fill = 'white', outline = "")
        menucanvas.create_rectangle(x2, y1, x2 + 4, y2 + 5, fill = 'white', outline = "")
        y1, y2 = y1 + 120, y2 + 120

    menugombok(163.5, 120.5, 'Vissza', menubezar)
    menugombok(163.5, 240.5, 'Ranglista', lambda: (eredmenybetoltes(), mn1.destroy()))
    menugombok(163.5, 360.5, 'új játék', lambda:(ujjatek(), mn1.destroy()))
    menugombok(163.5, 480.5, 'szabályzat', szabalyzat)
    menugomb.config(command=menubezar)
    canvas.bind_all('<Escape>', menubezar2)

def szabbezar(event):
    mn2.destroy()
    menu()

def szabbezar2():
    mn2.destroy()
    menu()

def visszgombra(event):
    visszgomb.config(image = szabnyil2)

def visszgomble(event):
    visszgomb.config(image = szabnyil)

def szabalyzat():
    global mn2, visszgomb
    mn1.destroy()
    y = 120
    mn2 = Frame(bigz, width = 875, height = 600, bg = fejlecszin)
    mn2.place(x = 550, y = 250)
    szabcanvas = Canvas(mn2, width = 874, height = 599, bg = fejlecszin,highlightthickness= 3, highlightbackground=fejlecalattbezs, relief='flat')
    szabcanvas.pack()
    Label(mn2, bg = fejlecszin, fg = 'white',text = 'szabályzat', font = bfont).place(x = 302, y = 16)
    for i in range(0,9):
        Label(mn2, bg = fejlecszin, fg = 'white',text = kmbinaciok[i], font = tablazatfont).place(x = 10, y = y)
        Label(mn2,bd = 0, bg = fejlecszin,  fg = 'white',text = pntertekek[i], font = tablazatfont).place(anchor = NE,x = 865, y = y)
        y = y + 50
    visszgomb = Button(mn2, image = szabnyil, bd = 0, bg = fejlecszin, activebackground=fejlecszin, command= szabbezar2)
    visszgomb.place(x = 20, y = 20)
    visszgomb.bind('<Enter>', visszgombra)
    visszgomb.bind('<Leave>', visszgomble)
    canvas.bind_all('<Escape>', szabbezar)

def jatpontszamiras(jatekospontszam):
    x = 170 + len(jatekosnev)*23.2
    canvas.delete("pontszam")
    text1 = "Pontszám: " + str(jatekospontszam)
    text2 = "pontszám: " + str(shelbypontszam)
    canvas.create_text(x + 20, 35, font = afont, anchor = W,fill = "white", text= text1, tags="pontszam")
    canvas.create_text(1290, 35, font = afont, anchor = W,fill = "white", text= text2, tags="pontszam")

def tablazatvillogas():
    for i in range(3):
        canvas.delete("tablazat")
        canvas.create_line(1060, 450, 1060, 906, fill="white", width = 5, tags = "tablazat")             #kulon minden line hogy amikor ertekeket ir be a tablazatba akkor feheren fog
        canvas.create_line(1685, 450, 1685, 906, fill="white", width = 5, tags = "tablazat")             #villogni a keret
        canvas.create_line(1059, 451, 1688, 451, fill="white", width = 5, tags = "tablazat")
        canvas.create_line(1058, 906, 1688, 906, fill="white", width = 5, tags = "tablazat")
        canvas.update()
        canvas.after(60)
        canvas.delete("tablazat")
        canvas.create_line(1060, 450, 1060, 906, fill=szurke, width = 5, tags = "tablazat")             #kulon minden line hogy amikor ertekeket ir be a tablazatba akkor feheren fog
        canvas.create_line(1685, 450, 1685, 906, fill=szurke, width = 5, tags = "tablazat")             #villogni a keret
        canvas.create_line(1059, 451, 1688, 451, fill=szurke, width = 5, tags = "tablazat")
        canvas.create_line(1058, 906, 1688, 906, fill=szurke, width = 5, tags = "tablazat")
        canvas.update()
        canvas.after(60)

def nemra(event):
    canvas.delete("keret")
    kicanvas.create_rectangle(37, 97, 111, 174, fill="white", outline='', tags = "keret")

def nemle(event):
    canvas.delete("keret")
    kicanvas.create_rectangle(37, 97, 111, 174, fill=szurke, outline='', tags = "keret")

def igenra(event):
    canvas.delete("keret2")
    kicanvas.create_rectangle(384, 97, 463, 174, fill="white", outline='', tags = "keret2")

def igenle(event):
    kicanvas.create_rectangle(384, 97, 463, 174, fill=szurke, outline='', tags = "keret2")
    canvas.delete("keret2")

def kilepkerdeszar():
    canvas.delete("torol")
    kilepgomb.config(command=kilepeskerdes)
    kilepfr.destroy()


def kilepkerdeszar2(event):
    canvas.delete("torol")
    kilepgomb.config(command=kilepeskerdes)
    kilepfr.destroy()


def kilepeskerdes():
    global igengomb, nemgomb, kilepfr, kicanvas
    canvas.create_rectangle(WIDTH//2-255, HEIGHT//2 - 105, WIDTH//2+255, HEIGHT//2+105, fill=fejlecalattbezs, tags="torol")
    kilepgomb.config(command=kilepkerdeszar)
    kilepfr = Frame(bigz, width = 500, height = 200, bg = fejlecszin)
    kilepfr.place(x = WIDTH//2, y = HEIGHT//2, anchor = 'center')
    kicanvas = Canvas(kilepfr, width = 500, height = 200, bg =fejlecszin)
    kicanvas.pack()
    biztos = Label(kilepfr, text = "biztosan kilépsz?", font = cfont, bg = fejlecszin, fg = "white")
    biztos.place(x = 250, y = 30, anchor = 'center')
    nemgomb = Button(kilepfr, text = "Nem", font = cfont, bd = 0, bg = fejlecalattbezs, fg = "white", activebackground="green", command = kilepkerdeszar)
    nemgomb.place(x = 40, y = 100, anchor = NW)
    igengomb = Button(kilepfr, text = "igen", font = cfont, bd = 0, bg = fejlecalattbezs, fg = "white", activebackground="red", command = kilepes)
    igengomb.place(x = 460, y = 100, anchor = NE)
    kicanvas.create_rectangle(37, 97, 111, 174, fill=szurke, outline='', tags = "keret")
    kicanvas.create_rectangle(384, 97, 463, 174, fill=szurke, outline='', tags = "keret2")
    kilepgomb.config(command=kilepkerdeszar)
    nemgomb.bind('<Enter>', nemra)
    nemgomb.bind('<Leave>', nemle)
    igengomb.bind('<Enter>', igenra)
    igengomb.bind('<Leave>', igenle)
    kilepfr.bind_all('<Escape>', kilepkerdeszar2)
    kilepfr.bind_all('<Return>', kilepes2)
    for i in range(5):
        canvas.delete("keret")
        kicanvas.create_rectangle(37, 97, 111, 174, fill="white", outline='', tags = "keret")
        canvas.update()
        canvas.after(60)
        canvas.delete("keret")
        kicanvas.create_rectangle(37, 97, 111, 174, fill=szurke, outline='', tags = "keret")
        canvas.update()
        canvas.after(60)
 



def graffelulet():
    global kilepgomb, dobasgomb, menugomb, jatekosnev, kov
    x,y = 170 + len(jatekosnev)*23.2, 260
    canvas.create_image(0,0, anchor = NW, image = bg2)
    #fejlec
    canvas.create_rectangle(5,0,WIDTH - 5, 90, fill= fejlecszin, outline=fejlecalattbezs, width = 5)
    menugomb = Button(canvas, image= peakyhat, border = 0, bg = fejlecszin, activebackground= fejlecszin, command = menu)
    menugomb.place(x = 18, y = 5)
    kilepgomb = Button(canvas, image = kilep1, border = 0, bg = fejlecszin, activebackground= fejlecszin, command=kilepeskerdes)
    kilepgomb.place(x = WIDTH - 95, y = 5)
    canvas.create_rectangle(116, 10, 119,80, fill=fejlecalattbezs,outline = '' )
    canvas.create_text(1616, 35, text = "shelby", anchor = W, fill="white", font=afont)
    canvas.create_text(138, 35, text = jatekosnev, anchor = W, fill="white", font=afont)
    
    canvas.create_rectangle(x, 10, x+3, 80, fill=fejlecalattbezs, outline= '')
    jatpontszamiras(jatekospontszam)
    
    canvas.create_rectangle(1600, 10, 1603, 80, fill=fejlecalattbezs, outline= '')
    canvas.create_text(25, 182, text=jatekosnev + ':', fill="white", font = bfont, anchor = NW)
    canvas.create_text(WIDTH - 10, 182, text="shelby:", fill="white", font = bfont, anchor = NE)
    canvas.create_line(29, 862, 29, 938, fill=szurke,  width = 3,tags="dob")
    canvas.create_line(115, 862, 115, 938, fill=szurke,width = 3,tags="dob")
    canvas.create_line(29, 862, 115, 862, fill=szurke, width = 3,tags="dob")
    canvas.create_line(29, 938, 115, 938, fill=szurke, width = 3,tags="dob")
    dobasgomb = Button(text = "dobás",width=5,height = 0,border = 0, fg='white',activeforeground="white", font = cfont, bg=fejlecszin, activebackground=fejlecszin, command=dobas)
    dobasgomb.place(x = 32, y = 865)
    canvas.create_line(WIDTH//2, 120, WIDTH//2, 1050, fill = "white", width = 3)


    #tablazat
    canvas.create_line(1060, 450, 1060, 906, fill=szurke, width = 5, tags = "tablazat")             #kulon minden line hogy amikor ertekeket ir be a tablazatba akkor feheren fog
    canvas.create_line(1685, 450, 1685, 906, fill=szurke, width = 5, tags = "tablazat")             #villogni a keret
    canvas.create_line(1059, 451, 1688, 451, fill=szurke, width = 5, tags = "tablazat")
    canvas.create_line(1058, 906, 1688, 906, fill=szurke, width = 5, tags = "tablazat")
    canvas.create_rectangle(1063, 454, 1683, 904 , fill=tablazatalap, outline='')
    #elvalaszto vonalak
    y = 505
    for i in range(9):
        canvas.create_rectangle(1074, y, 1674, y+3, fill="white", outline = '')
        canvas.create_rectangle(1238, 465, 1241, 895, fill="white", outline='')
        canvas.create_rectangle(1509, 465, 1512, 895, fill="white", outline='')
        y = y + 44
    #kombinaciok
    y = 508
    for i in range(0,9):
       canvas.create_text(1080, y, anchor = NW, fill = 'white', text = kombinaciok[i], font=tablazatfont )
       y = y + 44
    #nevek
    canvas.create_text(1550, 455,anchor = NW,fill = 'white', font = cfont, text = 'SHELBY')
    canvas.create_text(1375, 455,anchor = N,fill = 'white', font = cfont, text = jatekosnev)

    
    kilepgomb.bind('<Enter>', kilepra)
    kilepgomb.bind('<Leave>', kileple)
    menugomb.bind('<Enter>', menura)
    menugomb.bind('<Leave>', menule)
    dobasgomb.bind('<Enter>', dobra)
    dobasgomb.bind('<Leave>', doble)

    for i in range(6):
        img = random.choice(kockak)
        kockak.remove(img)
        canvas.create_image(25, 260, anchor = NW, image = img)
        canvas.create_image(WIDTH-25, 260, anchor = NE, image = img)
        canvas.create_image(25, 380, anchor = NW, image = img)
        canvas.create_image(WIDTH-25, 380, anchor = NE, image = img)
        canvas.create_image(25, 500, anchor = NW, image = img)
        canvas.create_image(WIDTH-25, 500, anchor = NE, image = img)
        canvas.create_image(25, 620, anchor = NW, image = img)
        canvas.create_image(WIDTH-25, 620, anchor = NE, image = img)
        canvas.create_image(25, 740, anchor = NW, image = img)
        canvas.create_image(WIDTH-25, 740, anchor = NE, image = img)
        canvas.after(120)
        canvas.update()
    kov = True

def kockakrajzolas(jatdobszam, sheldobszam):
    y = 260
    x1, x2 = 25, WIDTH - 25
    for i in range(0, 5):
        if jatdobszam[i] == 1:
            kep1 = k1
        elif jatdobszam[i] == 2:
            kep1 = k2
        elif jatdobszam[i] == 3:
            kep1 = k3
        elif jatdobszam[i] == 4:
            kep1 = k4
        elif jatdobszam[i] == 5:
            kep1 = k5
        elif jatdobszam[i] == 6:
            kep1 = k6
        canvas.create_image(x1, y, anchor = NW, image = kep1, tags="kockak")
        y = y + 120
    y = 260
    for i in range(0, 5):
        if sheldobszam[i] == 1:
            kep2 = k1
        elif sheldobszam[i] == 2:
            kep2 = k2
        elif sheldobszam[i] == 3:
            kep2 = k3
        elif sheldobszam[i] == 4:
            kep2 = k4
        elif sheldobszam[i] == 5:
            kep2 = k5
        elif sheldobszam[i] == 6:
            kep2 = k6
        canvas.create_image(x2, y, anchor = NE, image = kep2, tags="kockak")
        y = y + 120

def tetszoleges():
    global kov, jatekospontszam
    x = 1360
    y = 507
    lehkombinaciok.remove(tetszolegesszvg)
    gombtorles()
    parancsok.remove(tetszoleges)
    ertek = sum(jatdobszam)
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatekospontszam = jatekospontszam + ertek
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def par():
    x, y = 1360, 551
    global kov, dupla, jatekospontszam
    gombtorles()
    lehkombinaciok.remove(parszvg)
    parancsok.remove(par)
    if dupla == True:
        ertek = dszam*2
    else:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)    
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def drill():
    x,y = 1360, 595
    global kov, tripla, jatekospontszam
    gombtorles()
    lehkombinaciok.remove(drillszvg)
    parancsok.remove(drill)
    if tripla == True:
        ertek = tszam*3
    elif tripla == False:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white",font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def ketpar():
    global kov, ketpaar, jatekospontszam, par1, par2
    x, y = 1360, 639
    gombtorles()
    lehkombinaciok.remove(ketparszvg)
    parancsok.remove(ketpar)
    if ketpaar == True:
        ertek = par1*2 + par2*2
    else:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()


def kispoker():
    global kov, jatekospontszam, kvintupla
    x, y = 1360, 683
    gombtorles()
    lehkombinaciok.remove(kvintszvg)
    parancsok.remove(kispoker)
    if kvintupla == True:
        ertek = dszam * 4
    elif kvintupla == False:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N, fill = "white",font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def full():                                         #tripla dupla hibák
    global kov, jatekospontszam
    x, y = 1360, 727
    gombtorles()
    lehkombinaciok.remove(fullszvg)
    parancsok.remove(full)
    if fullk == True:
        ertek = sum(jatdobszam)
    else:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)    
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def kissor():
    global kov, jatekospontszam
    x, y = 1360, 771
    gombtorles()
    lehkombinaciok.remove(kissorszvg)
    parancsok.remove(kissor)
    if kissork ==  True:
        ertek = 15
    else:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N, fill = "white",font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

def nagysor():
    global kov, jatekospontszam
    x,y = 1360, 815
    gombtorles()
    lehkombinaciok.remove(nagysorszvg)
    parancsok.remove(nagysor)
    if nagysork ==  True:
        ertek = 20
    else:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()
  
def nagypoker():
    global kov, jatekospontszam
    x = 1360
    y = 859
    gombtorles() 
    lehkombinaciok.remove(nagypszvg)
    parancsok.remove(nagypoker)
    if yahtzee == True:
        ertek = 50
    elif yahtzee == False:
        ertek = 0
    jatekospontszam = jatekospontszam + ertek
    canvas.create_text(x,y, text=ertek,anchor = N,fill = "white", font=tablazatfont)
    tablazatvillogas()
    jatpontszamiras(jatekospontszam)
    if len(lehkombinaciok) != 0:
        kov = True
    else:
        kov = False
        gameover()

parancsok = [
    tetszoleges,
    par,
    drill,
    ketpar,
    kispoker,
    full,
    kissor,
    nagysor,
    nagypoker
]

def visszaallitas():
    global dupla, tripla, kvintupla, yahtzee, kissork, nagysork, ketpaar, fullk
    dupla = False
    tripla = False
    kvintupla = False
    yahtzee = False
    kissork = False
    nagysork = False
    ketpaar = False
    fullk = False
    
def lehetosegek(jatismell):
    global dszam, yahtzee, kvintupla, tripla, dupla, kissork, nagysork, fullk, par1, par2,ketpaar ,tszam, nagypszvg, fullszvg,lehkombinaciok,ketparszvg, tetszolegesszvg, parszvg, drillszvg, kvintszvg, nagysorszvg, kissorszvg
    x1, x2 = 222, 617
    y, y2 = 313, 360
    dszam, tszam, kvint = 0,0,0
    duplak = []
    kissorszamok = {1,2,3,4,5}
    nagysorszamok = {2,3,4,5,6}
    visszaallitas()
    for i in range(1,7):
        if (jatismell[i] == 5):
            dszam = i
            yahtzee = True
        if (jatismell[i] > 3):
            dszam = i
            kvint = i
            kvintupla = True
        if (jatismell[i] > 2):
            dszam = i
            tszam = i
            tripla = True
        if (jatismell[i] > 1):
            dszam = i
            duplak.append(i)
            dupla = True
            
    if set(jatdobszam) == kissorszamok:
        kissork = True
        kissorszvg = "Kis sor: + 15 pont"
    else:
        kissork = False
        kissorszvg = "Kis sor: + 0 pont"
    
    if set(jatdobszam) == nagysorszamok:
        nagysork = True
        nagysorszvg = "Nagy sor: + 20 pont"
    else:
        nagysork = False
        nagysorszvg = "Nagy sor: + 0 pont"

    if (3 in jatismell) and (2 in jatismell):
        fullk = True
        fullszvg = "Full: +" + str(sum(jatdobszam)) + "pont"
    else:
        fullk = False
        fullszvg = "Full: + 0pont"


    if len(duplak) == 2:
        ketpaar = True
        par1 = duplak[0]
        par2 = duplak[1]
        ketparszvg = "Két pár: +" + str(par1*2 + par2*2)
    else:
        ketpaar = False
        ketparszvg = "Két pár: + 0pont" 


    tetszolegesszvg = "Tetszoleges: +" + str(sum(jatdobszam)) + "pont"
    if dupla == True:
        parszvg = "Pár: +" + str(dszam*2) + "pont"
    else:
        parszvg = "Pár: + 0 pont"

    if tripla == True:
        drillszvg = "Drill: +" + str(tszam*3) + "pont"
    else:
        drillszvg = "Drill: + 0 pont"
    
    if kvintupla ==  True:
        kvintszvg = "Kis póker: +" + str(kvint*4) + "pont"

    else :
        kvintszvg = "Kis póker: + 0 pont"
    
    if yahtzee == True:
        nagypszvg = "Nagy Póker: + 50 pont"
    else:
        nagypszvg = "Nagy Póker: + 0 pont"

    for i in range(len(lehkombinaciok)):
        lehkomb = lehkombinaciok[i]
        if lehkomb[:3] == "Tet":
            lehkombinaciok[i] = tetszolegesszvg
        elif lehkomb[:3] == "Pár":
            lehkombinaciok[i] = parszvg
        elif lehkomb[:3] == "Dri":
            lehkombinaciok[i] = drillszvg
        elif lehkomb[:5] == "Kis p":
            lehkombinaciok[i] = kvintszvg
        elif lehkomb[:5] == "Kis s":
            lehkombinaciok[i] = kissorszvg
        elif lehkomb[:6] == "Nagy s":
            lehkombinaciok[i] = nagysorszvg
        elif lehkomb[:5] == "Két p":
            lehkombinaciok[i] = ketparszvg
        elif lehkomb[:3] == "Ful":
            lehkombinaciok[i] = fullszvg
        elif lehkomb[:6] == "Nagy P":
            lehkombinaciok[i] = nagypszvg
    
    if len(lehkombinaciok) >= 6 and len(lehkombinaciok)%2 == 0:
        for i in range(0,len(lehkombinaciok), 2):
            canvas.create_rectangle(x1-5, y-5, x1 + 311, y+76, fill=szurke, outline="", tags = "lehgomb")
            canvas.create_rectangle(x2-5, y2-5, x2 + 311, y2+76, fill=szurke, outline="", tags = "lehgomb")
            gomb(x1, y, lehkombinaciok[i],tablazatalap, "white", parancsok[i])
            gomb(x2, y2, lehkombinaciok[i+1],tablazatalap, "white", parancsok[i+1])
            y,y2 = y + 100, y2 + 100

    elif len(lehkombinaciok) >= 6 and len(lehkombinaciok)%2 != 0:
            for i in range(0,len(lehkombinaciok)-1, 2):
                canvas.create_rectangle(x1-5, y-5, x1 + 311, y+76, fill=szurke, outline="", tags = "lehgomb")
                canvas.create_rectangle(x2-5, y2-5, x2 + 311, y2+76, fill=szurke, outline="", tags = "lehgomb")
                gomb(x1, y, lehkombinaciok[i],tablazatalap, "white", parancsok[i])
                gomb(x2, y2, lehkombinaciok[i+1],tablazatalap, "white", parancsok[i+1])       
                y,y2 = y + 100, y2 + 100
            canvas.create_rectangle(x1-5, y-5, x1 + 311, y+76, fill=szurke, outline="", tags = "lehgomb")
            gomb(x1, y, lehkombinaciok[-1],tablazatalap, "white",parancsok[-1])

    elif len(lehkombinaciok) < 6:
        for i in range(0, len(lehkombinaciok)):
            canvas.create_rectangle(x1-5, y-5, x1 + 311, y+76, fill=szurke, outline="", tags = "lehgomb")
            gomb(x1, y, lehkombinaciok[i],tablazatalap, "white", parancsok[i])
            y = y + 100

def gombtorles():
    for gombok in gombok_lista:
        gombok.destroy()
    gombok_lista.clear()
    canvas.delete("lehgomb")


shelbylehet = [
    "Tetszoleges",
    "Pár",
    "Drill",
    "Két pár",
    "Kis póker",
    "Full",
    "Kis sor",
    "Nagy sor",
    "Nagy Póker"
    ]

def shelbygondol(shelismell):
    duplak = []
    
    for i in range(1,7):
        if (shelismell[i] == 5):
            print("Kvintupla" +str(i) + ":"  + str(i*5) + "pont")
            shelbylehet.remove("Nagy Póker")
        elif (shelismell[i] == 4):
            print("Kvadpla" + str(i) + ":"   + str(i*4) + "pont")
            shelbylehet.remove("Nagy Póker")
        elif (shelismell[i] == 3):
            print("Tripla" +str(i) + ":"  + str(i*3) + "pont")
            dszam = i
            sheltripla = True
        elif (shelismell[i] == 2):
            print("Dupla" +str(i) + ":"   + str(i*2) + "pont")
            dszam = i
            duplak.append(i)
            sheldupla = True
    
def dobas():
    global jatdobszam,sheldobszam, kov

    if kov == True:
        jatdobszam = []
        jatismell = [0,0,0,0,0,0,0]
        sheldobszam = []
        shelismell = [0,0,0,0,0,0,0]
        for i in range(5):
            szam1 = random.randint(1,6)
            szam2 = random.randint(1,6)
            jatdobszam.append(szam1)
            sheldobszam.append(szam2) 
            jatismell[szam1]+=1
            shelismell[szam2]+=1     
        kockakrajzolas(jatdobszam, sheldobszam)
        lehetosegek(jatismell)
        #shelbygondol(shelismell)
        kov = False

kezdes()
#gameover()
#hiba ketpar 
5
bigz.mainloop()


#adat betöltés folytatása hogy ne irja ki adatok elott a tipusait!!