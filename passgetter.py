# -*- coding: utf-8 -*-
def getCreds():
    with open(input("enter the league path: "), 'r+') as file:
        text = file.read()
        port = text[19:24]
        pw = text[25:47]
    return [port, pw]