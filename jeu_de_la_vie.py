#!/usr/bin/python
# -*- coding : utf-8 -*-

#Author: medkader16@gmail.com (just an example not final version)
import Tkinter
import random
import numpy
import time

nb=20
nbRandomeCell=100
col=["red","blue","green","black","yellow"]

color="red"
default_color="white"
#matrice=[nb][nb]
matrice=numpy.zeros((nb, nb),dtype=object)
copyMatrice=numpy.zeros((nb, nb))
window,bok=None,None

#La cellule ne
def colorButton(button):
	indice=random.randrange(0,len(col))
	button["bg"] = col[indice]
	button["activebackground"] = color

#La pauvre cellule est morte
def killButton(button):
	button["bg"] = default_color
	button["activebackground"] = default_color
	
#Retourne 1 si la cellule est vivante 0 sinon
def countCell(boutton):
	if(boutton["bg"] == default_color): return 0
	return 1

#Verification des voisin
def neighbour(cell):
	number=0
	x=cell[0]
	y=cell[1]
	size=nb-1
	
	#En haut
	if(y==0):
		#Coin gauche
		if(x==0):
			number=countCell(matrice[1][0])+countCell(matrice[1][1])+countCell(matrice[0][1])
		#Coin droit
		elif(x==size):
			number=countCell(matrice[size-1][0])+countCell(matrice[size-1][size-1])+countCell(matrice[size][size-1])
		#En haut sauf coin
		else:
			number=countCell(matrice[x-1][0])+countCell(matrice[x+1][0])+countCell(matrice[x-1][1])+countCell(matrice[x][1])+countCell(matrice[x+1][1])
			
	#En bas
	elif(y==size):
		#Coin gauche
		if(x==0):
			number=countCell(matrice[0][size-1])+countCell(matrice[1][size-1])+countCell(matrice[1][size])
		#Coin droit
		elif(x==size):
			number=countCell(matrice[size][size-1])+countCell(matrice[size-1][size-1])+countCell(matrice[size-1][size])
		#En haut sauf coin
		else:
			number=countCell(matrice[x-1][size])+countCell(matrice[x+1][size])+countCell(matrice[x-1][size-1])+countCell(matrice[x][size-1])+countCell(matrice[x+1][size-1])
	#Cote gauche
	elif(x==0):	
		number=countCell(matrice[x][y-1])+countCell(matrice[x][y+1])+countCell(matrice[x+1][y-1])+countCell(matrice[x+1][y])+countCell(matrice[x+1][y+1])
	#Cote droit
	elif(x==size):
		number=countCell(matrice[x][y-1])+countCell(matrice[x][y+1])+countCell(matrice[x-1][y-1])+countCell(matrice[x-1][y])+countCell(matrice[x-1][y+1])
	#Cellule millieu
	else:
		number=countCell(matrice[x-1][y-1])+countCell(matrice[x][y-1])+countCell(matrice[x+1][y-1])+countCell(matrice[x-1][y])+countCell(matrice[x+1][y])+countCell(matrice[x-1][y+1])+countCell(matrice[x][y+1])+countCell(matrice[x+1][y+1])

	return number

#Remplissage des nouveaux etas des cellules
def fillCopy():

	for x in range(nb):
		for y in range(nb):
			kafla=matrice[x][y]
			
			#Dans le casou la cellule est vivante
			if(countCell(kafla)==0):
				if(neighbour((x,y))==3):
					copyMatrice[x][y]=1
				else:
					copyMatrice[x][y]=0
			#Dans le cas d'une cellule vivante
			else:
				if((neighbour((x,y))==2) or (neighbour((x,y))==3) ):
					copyMatrice[x][y]=1
				else:
					copyMatrice[x][y]=0

#Coloriage des nouveaux etas des cellules
def colorMatrice():
	time.sleep(.8)
	for x in range(nb):
		for y in range(nb):
			kafla=matrice[x][y]
			if(copyMatrice[x][y]==1):
				colorButton(kafla)
			else:
				killButton(kafla)

#Generation aleatoir de case
def randomCell(nbCell):
	liste=[]
	i=0
	while(i<=nbCell):
		xr=random.randrange(0,nb)
		xy=random.randrange(0,nb)
		if(xr,xy) not in liste:
			liste.append((xr,xy))
			colorButton(matrice[xr][xy])
			i=i+1	
		
#Main tkinter pour le GUI	
def main(n=nb):
	global window
	global bok
	window = Tkinter.Tk()
	last_clicked = [None]
    
	#Matrice de boutton
	
	for x in range(n):
		for y in range(n):
			b = Tkinter.Button(window, bg=default_color, activebackground=default_color)
			b.grid(column=x, row=y)
			# creating the callback with "b" as the default parameter bellow "freezes" its value pointing
			# to the button created in each run of the loop.
			b["command"] = lambda b=b: click(b, last_clicked)
			matrice[x][y]=b
	#Configuration initial pour teste, puis randome		
	colorButton(matrice[1][1])
	colorButton(matrice[1][2])
	colorButton(matrice[1][3])
	##################################################
	#grenouille
	randomCell(nbRandomeCell)
		
	bok = Tkinter.Button(window, text="OK", command=moi)
	bok.grid(column=nb, row=nb)
	
	return window
	
#Lorsque nous cliquons sur une case
def click(button, last_clicked):
	#Retourner la valeur par defaut en blanc du dernier buton
	if last_clicked[0]:
		last_clicked[0]["bg"] = default_color
		last_clicked[0]["activebackground"] = default_color
	#Attendre 5 seconde
	#time.sleep(5)
    
	#Colorier le boutton actuelle en rouge
	button["bg"] = color
	button["activebackground"] = color
	last_clicked[0] = button

#Mise a jour de la prochaine iteration
def moi():
	global window
	#Remplissage des nouvelles valeur
	fillCopy()
	#Recoloriage de la matrice
	colorMatrice()
	window.update()
	moi()
	#window.after_idle(moi)
	
w = main()
#w.after_idle(moi)
Tkinter.mainloop()

