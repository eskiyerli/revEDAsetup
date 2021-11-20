""" 
    Copyright (C) Revolution Semiconductor - All Rights Reserved
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential
    Written by Murat Eskiyerli <eskiyerli@revsemi.com>, July 2020
"""

import os
import pathlib
import sys

import ui
import wx
installPath= pathlib.Path('/opt/xyceGUI')
sys.path.insert(0, str(installPath.joinpath("wxmplot")))
sys.path.insert(0, str(installPath.joinpath("callbacks")))
sys.path.insert(0, str(installPath.joinpath("reveda")))

import reveda as rv
import reveda.revsimgui as rsgui
import reveda.symbolGenerator as sg
import reveda.utilities as ut

gui = cvar.uiptr
prefix = "/home/caduser/"

# projectPath variable is defined here. Simulation directories etc will be under this.
projectPath = prefix

# create wxpython app

app = wx.App()
app.SetExitOnFrameDelete(False)

app.MainLoop()
menu = gui.createMenu("Utilities")

gui.createMenuItem(
    menu,
    gui.createAction("Renumber Instances", "ut.renumberInstances()"),
)
gui.createMenuItem(
    menu,
    gui.createAction("Text Editor", "ut.openEditor()"),
)
gui.createMenuItem(
    menu,
    gui.createAction("Terminal", "ut.openTerminal()"),
)

menu = gui.createMenu("RevEDA")
gui.createMenuItem(
    menu,
    gui.createAction("Simulation", "rsgui.revEDA()"),
)
gui.createMenuItem(
    menu,
    gui.createAction("Generate Verilog-A Symbol", "sg.revSymGen()"),
)


designLibs = ["XyceLib", "behaviouralLib", "sky130Devices"]

libList = []
for designLib in designLibs:
    libList.append(ui.library(designLib))
    libList[-1].dbOpenLib(projectPath + designLib)
gui.updateLibBrowser()
