bl_info = {
    "name": "Execute Script",
    "description": "Execute a script, the file with the same as the blend file but with .py instead of .blend, either in the same directory as the blend file, or saved in bpy.data.texts, or run bpy.data.texts[0]",
    "author": "James Reynolds",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Render > Execute Script",
    "warning": "", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/magnusviri/blender_scripts",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Developer",
}

# https://developer.blender.org/docs/handbook/addons/addon_meta_info/
# Add On Example: https://docs.blender.org/api/current/info_quickstart.html
# Performance tuning: https://docs.blender.org/api/current/info_best_practice.html

import bpy
import time
import bpy
import os

def main(context):
    time_start = time.time()
    filepath = os.path.dirname(bpy.data.filepath)
    filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
    scriptname = filename+".py"
    scriptpath = os.path.join(filepath, scriptname)
    if os.path.exists(scriptpath):
        exec(compile(open(scriptpath).read(), scriptpath, 'exec'))
    elif scriptname in bpy.data.texts:
        script = bpy.data.texts[scriptname]
        exec(script.as_string())
    elif len(bpy.data.texts) > 0:
        script = bpy.data.texts[0]
        exec(script.as_string())
    else:
        print("No script found")
    print("My Script Finished: %.4f sec" % (time.time() - time_start))


class ExecuteScript(bpy.types.Operator):
    """Exec"""
    bl_idname = "screen.execute_script"
    bl_label = "Execute Script"

    @classmethod
    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ExecuteScript.bl_idname, text=ExecuteScript.bl_label)


def register():
    bpy.utils.register_class(ExecuteScript)
    bpy.types.TOPBAR_MT_render.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ExecuteScript)
    bpy.types.TOPBAR_MT_render.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.execute_script()