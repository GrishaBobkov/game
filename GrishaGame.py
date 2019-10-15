from tkinter import*
from random import*
import time
import math

root=Tk()
root.geometry('800x620')
canv=Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors=['red', 'green', 'blue']

def bul(x, y):
	r=5
	canv.create_oval(x-r, y-r, x+r, y+r, fill='red', width=0)
	
def delete_bul(x, y):
	r=5
	canv.create_oval(x-r, y-r, x+r, y+r, fill='white', width=0)

def Stone(x, y, r):
	canv.create_oval(x-r, y-r, x+r, y+r, fill='brown', width=0)
	
def delete_Stone(x, y, r):
	canv.create_oval(x-r, y-r, x+r, y+r, fill='white', width=0)

def cannon(color, x, y):
	canv.create_oval(750, 550, 850, 650, fill=color, width=0)
	canv.create_line(800-100*(800-x)/math.sqrt((800-x)*(800-x)+(600-y)*(600-y)), 600-100*(600-y)/math.sqrt((800-x)*(800-x)+(600-y)*(600-y)), 800, 600, fill=color, width=10)

def enemy(x, y):
	r=10
	canv.create_oval(x-r, y-r, x+r, y+r, fill='blue', width=0)

def delete_enemy(x, y):
	r=10
	canv.create_oval(x-r, y-r, x+r, y+r, fill='white', width=0)

def enemymove():
	global enemyX, enemyY, Nenemy, stoneX, stoneY, stoneR, speed, Nstone, Score, tt
	kk=0
	for j in range(0, Nenemy):
		delete_enemy(enemyX[j], enemyY[j])
		ux=randint(-2, 4)+j
		uy=randint(-1, 5)
		uu=0
		for i in range(0, Nstone):
			if (enemyX[j]+ux-stoneX[i])*(enemyX[j]+ux-stoneX[i])+(enemyY[j]+uy-stoneY[i])*(enemyY[j]+uy-stoneY[i])<(stoneR[i]+10)*(stoneR[i]+10):
				uu=1
				if enemyY[j]<stoneY[i]:
					enemyX[j]=enemyX[j]
					enemyY[j]=enemyY[j]-5
				else:
					enemyX[j]=enemyX[j]
					enemyY[j]=enemyY[j]+5
		if uu==0:
			enemyX[j]=enemyX[j]+ux
			enemyY[j]=enemyY[j]+uy
		enemy(enemyX[j], enemyY[j])
		if enemyX[j]<800 and enemyY[j]<600:
			kk=1
	if kk==0 or tt>600:
		for j in range(0, Nenemy):
			enemyX[j]=0
			enemyY[j]=0
		tt=0
		speed=speed+1
		for i in range(0, Nstone):
			delete_Stone(stoneX[i], stoneY[i], stoneR[i])
		Nstone=4
		stoneX=[randint(100, 700), randint(100, 700), randint(100, 700), randint(100, 700)]  #Создание координат препятствий
		stoneY=[randint(100, 500), randint(100, 500), randint(100, 500), randint(100, 500)]
		stoneR=[randint(30, 70), randint(30, 70), randint(30, 70), randint(30, 70)]
		canv.create_rectangle(0, 0, 800, 600, fill='white')
		for i in range(0, Nstone):
			Stone(stoneX[i], stoneY[i], stoneR[i])
	tt=tt+1
	if speed>10:	
		l['text']='Игра окончена! Ваш результат   '+str(Score)
	else:
		root.after(int(110-10*speed), enemymove)
		
def Flybullet():
	global Xb, Yb, tb, Xtarget, Ytarget, enemyX, enemyY, Score, speed, crash
	if crash==0:
		delete_bul(Xb, Yb)
	Xb=800-(800-Xtarget)*tb/33
	Yb=600-(600-Ytarget)*tb/33
	for i in range(0, Nstone):
		if (Xb-stoneX[i])*(Xb-stoneX[i])+(Yb-stoneY[i])*(Yb-stoneY[i])<(stoneR[i]+5)*(stoneR[i]+5):
			crash=1
	for i in range(0, Nenemy):
		if (Xb-enemyX[i])*(Xb-enemyX[i])+(Yb-enemyY[i])*(Yb-enemyY[i])<225:
			delete_enemy(enemyX[i], enemyY[i])
			enemyX[i]=2000
			Score=Score+speed
			ggg='ваш счет:    '+ str(Score)
			l['text']=ggg
			crash=1
	if crash==0 and tb<32:
		bul(Xb, Yb)
	if tb<32:
		lll['text']='Идет перезарядка'
	else:
		lll['text']='Орудие  готово  к  выстрелу'
	cannon('black', Xtarget, Ytarget)
	tb=tb+1
	if tb<33:
		root.after(33, Flybullet)

def shoot(event):
	global Xtarget, Ytarget, tb, Xb, Yb, crash, StartPlay
	if tb>32 and StartPlay==1:
		cannon('white', Xtarget, Ytarget)
		Xtarget=event.x
		Ytarget=event.y
		while Xtarget>0 and Ytarget>0:
			Xtarget=Xtarget*1.1-80
			Ytarget=Ytarget*1.1-60
		tb=0
		crash=0
		Xb=800
		Yb=600
		cannon('black', Xtarget, Ytarget)
		Flybullet()

def startgame(event):
	global stoneX, stoneY, stoneR, Nstone, StartPlay
	canv.create_rectangle(0, 0, 800, 600, fill='white')
	for i in range(0, Nstone):
		Stone(stoneX[i], stoneY[i], stoneR[i])
	StartPlay=1
	cannon('black', Xtarget, Ytarget)
	enemymove()

Score=0
speed=5
StartPlay=0

Xb=800  #координаты пули
Yb=600
tb=35
crash=0
Xtarget=400
Ytarget=300

tt=0

Nenemy=5
enemyX=[0, 0, 0, 0, 0]  #создание координат противника
enemyY=[0, 0, 0, 0, 0] 

Nstone=4
stoneX=[randint(100, 700), randint(100, 700), randint(100, 700), randint(100, 700)]  #Создание координат препятствий
stoneY=[randint(100, 500), randint(100, 500), randint(100, 500), randint(100, 500)]
stoneR=[randint(30, 70), randint(30, 70), randint(30, 70), randint(30, 70)]

canv.create_text(350, 300, text='Цель  игры  стрелять  по  движущимся  синим  шарам.')
canv.create_text(350, 320, text='Красные  большие  шары - препятствия.  Выстрел - ')
canv.create_text(350, 340, text='щелчок  мыши.  Когда  все  шары  пройдут  мимо  вас')
canv.create_text(350, 360, text='или  умрут  под  вашим  огнем  или  ваша  дуэль  ')
canv.create_text(350, 380, text='затянется  на  достаточно  большое  время.  Начнется ')
canv.create_text(350, 400, text='новый  раунд.  Игра - несколько  раундов')
canv.create_text(350, 480, text='Готовы? Нажмите Tab+пробел!')
l=Label(root, bg='blue', fg='white', width=100)
l['text']='ваш счет:   0'
l.pack()
lll=Label(root, bg='blue', fg='white', width=100)
lll['text']='Орудие  готово  к  выстрелу'
lll.pack()
canv.bind('<space>', startgame)
canv.bind('<Button-1>', shoot)
mainloop()
