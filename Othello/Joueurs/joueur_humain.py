#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    while True:
        coup=input("Entrez un coup:")
	if coup in jeu[2]:
            break
    return coup
