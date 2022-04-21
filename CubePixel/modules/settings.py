import os
import json
from types import SimpleNamespace


def default_settings():
    setting_dict = {
        "settings": {
            "vsync": False,
            "borderless": False,
            "fullscreen": False,
            "render_distance": 2
        },

        "world": {
            "chunk_with": 15,
            "amp": 16,
            "amp_multiplier": 2
        }
    }

    with open("settings.json", "w+") as s:
        json.dump(setting_dict, s, indent=4)


def load_settings():
    with open("settings.json") as data:
        return json.load(data, object_hook=lambda d: SimpleNamespace(**d))


if not os.path.isfile("settings.json"):
    default_settings()
settings = load_settings()
