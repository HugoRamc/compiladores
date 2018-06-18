from LR1struct import *

edo1 = LR1struct(['Ep', '.', 'E'],"$")
edo2 = LR1struct(['Ep', '.', 'E'],"$")

def isInCerradura(item,cerraduraDone):
	flag = False
	for it in cerraduraDone:
		if item.item == it.item and item.simbolos == it.simbolos:
			flag = True
			return flag
	return flag

if isInCerradura(edo1,[edo1,edo2]):
	print("si esta")
else:
	print("no esta")

