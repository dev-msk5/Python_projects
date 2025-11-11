def add_setting(settings: dict, tupl: tuple):
    key, value = tupl
    key = str(key).lower()
    value = str(value).lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, tupl: tuple):
    key, value = tupl
    key = str(key).lower()
    value = str(value).lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        
def delete_setting(settings: dict, key: str):
    key = str(key).lower()
    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    items = "\n".join(f"{k.capitalize()}: {v}" for k, v in settings.items())
    return "Current User Settings:\n" + items +'\n'

test_settings = {'hmm': 1, "theme": "yes", "meswagew": "hjkaebda"}
