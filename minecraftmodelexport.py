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
    "name": "Minecraft block model exporter (*.mcmd)",
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

class DataExporter:
    
    def run(self, filepath, context):
        print(filepath, context)


class MineCraftExport(bpy.types.Operator, ExportHelper):
    '''Export to minecraft block model'''
    bl_idname = "something.minecraft"
    bl_label = "Export to mcmd"
    # mc ep
    
    filename_ext = ".mcmd"
    
    filter_glob = StringProperty(
            default="*.mcmd",
            options={'HIDDEN'}
            )
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        de = DataExporter()
        return de.run(self.filepath, context)



def menu_func_export(self, context):
    self.layout.operator(MineCraftExport.bl_idname, text="Mcmo export (.mcmd)")

def register():
    bpy.utils.register_class(MineCraftExport)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(MineCraftExport)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()

    bpy.ops.something.minecraft('INVOKE_DEFAULT')