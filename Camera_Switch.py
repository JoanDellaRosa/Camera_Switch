import maya.cmds as cmds

def switch_cameras():
    cameras = ["|persp", "|front", "|side", "|top"]

    current_panel = cmds.getPanel(withFocus=True)

    current_camera = cmds.modelEditor(current_panel, query=True, camera=True)

    current_index = cameras.index(current_camera)

    next_index = (current_index + 1) % len(cameras)
    
    next_camera = cameras[next_index]

    cmds.lookThru(next_camera)

switch_cameras()
