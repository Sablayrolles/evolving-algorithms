# -*- coding: utf-8 -*-

DEBUG = False

def getTopLevelParentClassAfterObject(var):
    global DEBUG
    
    # recuperer le type d'un object sa classe mère meme si il y a des hiérarchies de classes
    if DEBUG:
        print(str(var.__class__.__mro__[-2]))
        print(str(var.__class__.__mro__[-2]).split("."))
        print(str(var.__class__.__mro__[-2]).split(".")[-1])
        print(str(var.__class__.__mro__[-2]).split(".")[-1][:-2])
    
    return str(var.__class__.__mro__[-2]).split(".")[-1][:-2]
