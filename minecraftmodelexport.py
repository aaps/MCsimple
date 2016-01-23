import bpy
import string
import pdb
import time
import math 
import operator
import ast
import os

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty

dbg = False

bl_info = {
    "name": "Minecraft mejiggest (*.mcmo)",
    "description": "This addon allows you to export to single block minecraft meshes",
    "author": "Aat Karelse",
    "version": (0, 1, 0),
    "blender": (2, 6, 3),
    #"api": ???,
    "location": "File > Export > minecraft model",
    "warning": "Alpha",
    # "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/Import-Export/WarCraft_MDL",
    # "tracker_url": "http://projects.blender.org/tracker/index.php?func=detail&aid=29552",
    "category": "Import-Export"}