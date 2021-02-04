# -*- coding: UTF8 -*-

import time
import pickle

muistikirja = []

muistio = "muistio.dat"

error = "Virhe tiedostossa, luodaan uusi "

#moduli tryOpen, joka testaa onko tiedostoa olemassa. Palauttaa True or False
def tryOpen(m):
	try:
		tiedosto = open(m, "r")
		tiedosto.close()
		return True
	except IOError:
		return False
	
def makeFile(m):
	tiedosto = open(m, "w")
	tiedosto.close()
		
#moduli readFile, joka avaa tiedoston luettavaksi. Tallentaa tiedon muistikirja listaan.
def readFile(m):
	tiedosto = open(m, "r")
	text = tiedosto.read()
	muistikirja.append(text)
	tiedosto.close()
		
#moduli writeFile(), joka avaa tiedoston kirjoitusta varten. Kirjoittaa tiedostossa olevan tiedon päälle uuden listan. 
def writeFile(m):
	tiedosto = open(m, "w")
	for i in muistikirja:
		tiedosto.write(i)
	tiedosto.close()

#moduli writeEntry(), joka kirjoittaa uuden merkinnän muistikirja listaan ja kutsuu writeFile modulia, jolla kirjoittaa tiedostoon.
def writeEntry(m):
	text = input("Kirjoita uusi merkintä:")
	muistikirja.append(text + ":::" + time.strftime("%X %x"))
	writeFile(m)
	
#moduli editEntry(), joka avaa valmiin merkinnän tiedostossa ja muokkaa sitä.
def editEntry(m):
	print("Listalla on ",len(muistikirja)," merkintää.")
	index = int(input("Mitä niistä muutetaan?:"))
	print(muistikirja[index-1])
	edit = input("Anna uusi teksti:")
	muistikirja[index-1] = edit + ":::" + time.strftime("%X %x")
	writeFile(m)
#moduli deleteEntry, joka avaa tiedoston kirjoitusta varten ja poistaa merkinnän
def deleteEntry(m):
	print("Listalla on ",len(muistikirja)," merkintää.")
	index = int(input("Mitä niistä poistetaan?:"))
	print("Poistettiin merkintä ",muistikirja[index-1])
	muistikirja.pop(index-1)
	writeFile(m)
	
def saveAndExit(m):
	tiedosto = open(m, "wb")
	pickle.dump(muistikirja, tiedosto)
	tiedosto.close
	
def main():
	if tryOpen(muistio):
		readFile(muistio)
	else: 
		print(error + muistio + ".")
		makeFile(muistio)
	while True:
		print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta\n")
		valinta = int(input("Mitä haluat tehdä?:"))
		if valinta == 1:
			for i in muistikirja:
				print(i)
		elif valinta == 2:
			writeEntry(muistio)
		elif valinta == 3:
			editEntry(muistio)
		elif valinta == 4:
			deleteEntry(muistio)
		elif valinta == 5:
			saveAndExit(muistio)
			print("Lopetetaan.")
			break
		else: 
			print("Virheellinen valinta.")
			continue

if __name__ == "__main__":
	main()