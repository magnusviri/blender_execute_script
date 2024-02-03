# Blender Scripts

I plan on putting my python Blender scripts here.

## exec_addon.py

This script executes a script. Kind of redundant? Well, as far as I can tell, Blender doesn't have a menu or hotkey to run scripts. You have to open the Text Editor and then open the script in Blender then click the "run" button. I don't think that button has a hotkey either.

But exec_addon.py registers itself as an Add On so if you install it then it will always load and add itself to the bottom of the Render Menu (I know, it's the wrong menu, I don't know where to put it yet). I believe I can automatically assign it a hotkey, but I'm too new to Blender to know what good one to pick. Right now I manually assigned it cntl-alt-x (for execute). I am putting it GitHub and will show it to some people and see what they think.

So what script does exec_addon.py execute? First, it looks in the directory of the blend file. If it finds a file with the same name as the blend file, but ends in .py, it will execute that. So, if the blend file is "filename.blend", then exec_addon.py will look for "filename.py" and execute it.

If it doesn't find that file, then it will look in it's text data for a text named the same ("filename.py" if the blend file is "filename.blend"). If it's there, it is executed.

If one isn't there, exec_addon.py will execute bpy.data.texts[0] if it exists. Maybe not a good idea? IDK. Maybe it should look for the first text that ends in ".py"? Maybe it should execute all scripts that end in ".py"? IDK.

The purpose of looking for a file on the filesystem first is because I believe most people would rather edit scripts outside of BLender. So that's what it checks and executes first.

If your blend file doesn't have bpy.data.texts[0], then it prints a message to the console and exits. I don't know if Blender allows me to show a message. If it does, then that would be preferable to printing to the console. I'm still new to Blender so I don't know.
