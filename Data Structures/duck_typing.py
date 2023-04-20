from abc import ABC, abstractmethod


class TexBox:
    def draw(self):
        print("TexBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
texbox = TexBox()
draw([ddl, texbox])