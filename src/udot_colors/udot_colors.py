import pprint

_udot_colors_dict = {
    "primary": {
        "light_blue": "#5A87C6",
        "orange": "#E86924",
        "dark_blue": "#0B2444",
    },
    "secondary": {
        "light_green": "#ABC746",
        "mustard": "#F5A31B",
        "medium_blue": "#09549C",
        "tan": "#C7A25A",
        "turquoise": "#55CCD4",
        "red": "#E8261A",  # Only use to highlight something strong or negative
    },
    "tertiary": {
        "red_rock": "#C7776D",
        "brown": "#7A5B1F",
        "tacao": "#F7AA74",
        "purple": "#8A52A1",
        "dark_green": "#6B7A31",
        "yellow": "#DED843",
    },
    "grays": {
        "dark_gray": "#454545",
        "gray": "#888888",
        "light_gray": "#EEEEEE",
        "white": "#FFFFFF",
    },
}


def get_color(*cols):
    all_colors = {_udot_colors_dict[c] for c in _udot_colors_dict.keys()}
    return [all_colors[c] for c in cols]


def get_color_category(*cols):
    return [_udot_colors_dict[c] for c in cols]


def list_udot_colors(*cols):
    red_msg = "Only use red to highlight something strong or negative"
    if len(cols) < 1:
        pprint.pprint(red_msg)
        pprint.pprint(_udot_colors_dict)
    else:
        if any([c == "secondary" for c in cols]):
            print(red_msg)
        for c in cols:
            print(c + ":")
            pprint.pprint(_udot_colors_dict[c])
