# -*- coding: utf-8 -*-

def getTopLevelParentClassAfterObject(var):
    # recuperer le type d'un object sa classe mère meme si il y a des hiérarchies de classes
    return str(var.__class__.__mro__[-2]).split(".")[1][:-2]