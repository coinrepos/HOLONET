import os

ANIMATION_FOLDER = "C:\\Projects\\HOLONET\\output_files"

def list_available_animations():
    """Lists all Mixamo animations stored in the output_files folder."""
    return [file for file in os.listdir(ANIMATION_FOLDER) if file.endswith(".fbx")]

def get_animation_file(animation_name):
    """Gets the full path of a requested animation."""
    animation_path = os.path.join(ANIMATION_FOLDER, animation_name)
    if os.path.exists(animation_path):
        return {"animation_file": animation_path}
    else:
        return {"error": f"Animation '{animation_name}' not found."}
