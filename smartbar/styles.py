




# BAR STYLES
bar_styles = { # [Foreground, Background]
    "normal": {
        "BAR": {
            "+": [None, None],
            "-": [None, None],
        },
        "DESC": [None, None],
        "CUR": [None, None],
        "TOTAL": [None, None],
        "PERCENT": [None, None],
        "SPEED": [None, None],
        "ETA": [None, None],
    },
    
    "simple": {
        "BAR": {
            "+": [0x7533F0, None],
            "-": [0x474747, None],
        },
        "DESC": [None, None],
        "CUR": [None, None],
        "TOTAL": [None, None],
        "PERCENT": [None, None],
        "SPEED": [None, None],
        "ETA": [None, None],
    },
    
    "contrast": {
        "BAR": {
            "+": [0xFFFFFF, 0x007ACC],
            "-": [0xCCCCCC, 0x1E1E1E],
        },
        "DESC": [0xFFD700, None],
        "CUR": [0x00FF00, None],
        "TOTAL": [0x00FFFF, None],
        "PERCENT": [0xFF00FF, None],
        "SPEED": [0xFFA500, None],
        "ETA": [0xFF4500, None],
    },

    "dark": {
        "BAR": {
            "+": [0x00FF00, 0x000000],
            "-": [0x444444, 0x000000],
        },
        "DESC": [0xAAAAAA, None],
        "CUR": [0x888888, None],
        "TOTAL": [0x666666, None],
        "PERCENT": [0x999999, None],
        "SPEED": [0x777777, None],
        "ETA": [0x555555, None],
    },

    "mono": {
        "BAR": {
            "+": [0xFFFFFF, None],
            "-": [0x888888, None],
        },
        "DESC": [0xAAAAAA, None],
        "CUR": [0xAAAAAA, None],
        "TOTAL": [0xAAAAAA, None],
        "PERCENT": [0xAAAAAA, None],
        "SPEED": [0xAAAAAA, None],
        "ETA": [0xAAAAAA, None],
    },

    "matrix": {
        "BAR": {
            "+": [0x00FF00, 0x000000], 
            "-": [0x003300, 0x000000], 
        },
        "DESC": [0x00FF00, None],
        "CUR": [0x00FF00, None],
        "TOTAL": [0x00FF00, None],
        "PERCENT": [0x00FF00, None],
        "SPEED": [0x009900, None],
        "ETA": [0x009900, None],
    },

    "solarized": {
        "BAR": {
            "+": [0x268BD2, 0x002B36],
            "-": [0x586E75, 0x002B36],
        },
        "DESC": [0xB58900, None],
        "CUR": [0x859900, None],
        "TOTAL": [0x2AA198, None],
        "PERCENT": [0xD33682, None],
        "SPEED": [0x6C71C4, None],
        "ETA": [0xCB4B16, None],
    },

    "gruvbox": {
        "BAR": {
            "+": [0xFABD2F, 0x282828], 
            "-": [0x3C3836, 0x282828],
        },
        "DESC": [0xFE8019, None],
        "CUR": [0xB8BB26, None],
        "TOTAL": [0xB8BB26, None],
        "PERCENT": [0xFABD2F, None],
        "SPEED": [0x8EC07C, None],
        "ETA": [0x83A598, None],
    },

    "nord": {
        "BAR": {
            "+": [0x88C0D0, 0x2E3440], 
            "-": [0x4C566A, 0x2E3440],
        },
        "DESC": [0x81A1C1, None],
        "CUR": [0xA3BE8C, None],
        "TOTAL": [0xA3BE8C, None],
        "PERCENT": [0x88C0D0, None],
        "SPEED": [0x5E81AC, None],
        "ETA": [0xBF616A, None],
    },

    "dracula": {
        "BAR": {
            "+": [0xBD93F9, 0x282A36], 
            "-": [0x44475A, 0x282A36],
        },
        "DESC": [0xFF79C6, None],
        "CUR": [0x50FA7B, None],
        "TOTAL": [0x50FA7B, None],
        "PERCENT": [0xBD93F9, None],
        "SPEED": [0x8BE9FD, None],
        "ETA": [0xFFB86C, None],
    },

    "firewatch": {
        "BAR": {
            "+": [0xFF6B35, 0x1E1E24],
            "-": [0x4A4E69, 0x1E1E24],
        },
        "DESC": [0xF7B32B, None],
        "CUR": [0x6FFFE9, None],
        "TOTAL": [0x6FFFE9, None],
        "PERCENT": [0xFF6B35, None],
        "SPEED": [0xA9BCD0, None],
        "ETA": [0xE36414, None],
    },

    "monochrome": {
        "BAR": {
            "+": [0xFFFFFF, 0x000000],  
            "-": [0x555555, 0x000000],
        },
        "DESC": [0xCCCCCC, None],
        "CUR": [0xCCCCCC, None],
        "TOTAL": [0xCCCCCC, None],
        "PERCENT": [0xFFFFFF, None],
        "SPEED": [0x888888, None],
        "ETA": [0x888888, None],
    },

    "pastel": {
        "BAR": {
            "+": [0xFFB3BA, 0xFAF3F3], 
            "-": [0xDADADA, 0xFAF3F3],
        },
        "DESC": [0xBAE1FF, None],
        "CUR": [0xFFDFBA, None],
        "TOTAL": [0xFFDFBA, None],
        "PERCENT": [0xB28DFF, None],
        "SPEED": [0xAFF8DB, None],
        "ETA": [0xFFFFBA, None],
    },
    "neon": {
        "BAR": {
            "+": [0x39FF14, 0x000000],
            "-": [0x0F0F0F, 0x000000],
        },
        "DESC": [0xFF00FF, None],
        "CUR": [0x00FFFF, None],
        "TOTAL": [0xFFFF00, None],
        "PERCENT": [0xFF3131, None],
        "SPEED": [0x39FF14, None],
        "ETA": [0xFF1493, None],
    },
    "sunset": {
        "BAR": {
            "+": [0xFF5E5B, 0x2C061F],
            "-": [0x8C1C13, 0x2C061F],
        },
        "DESC": [0xFFBA08, None],
        "CUR": [0xFAA307, None],
        "TOTAL": [0xF48C06, None],
        "PERCENT": [0xE85D04, None],
        "SPEED": [0xDC2F02, None],
        "ETA": [0x9D0208, None],
    },
    "forest": {
        "BAR": {
            "+": [0x228B22, 0x013220],
            "-": [0x556B2F, 0x013220],
        },
        "DESC": [0xA2D149, None],
        "CUR": [0x6B8E23, None],
        "TOTAL": [0x9ACD32, None],
        "PERCENT": [0x32CD32, None],
        "SPEED": [0x8FBC8F, None],
        "ETA": [0x2E8B57, None],
    },
    "vaporwave": {
        "BAR": {
            "+": [0xFF77FF, 0x2D1B3A],
            "-": [0x7F5A83, 0x2D1B3A],
        },
        "DESC": [0xFF77FF, None],
        "CUR": [0x77DDFF, None],
        "TOTAL": [0x77DDFF, None],
        "PERCENT": [0xCBA6F7, None],
        "SPEED": [0xFEC8D8, None],
        "ETA": [0xD291BC, None],
    },
    "terminal": {
        "BAR": {
            "+": [0x00FF00, 0x000000],
            "-": [0x003300, 0x000000],
        },
        "DESC": [0x00FF00, None],
        "CUR": [0x00FF00, None],
        "TOTAL": [0x00FF00, None],
        "PERCENT": [0x00FF00, None],
        "SPEED": [0x00FF00, None],
        "ETA": [0x00FF00, None],
    }
}

def hex_to_ansi(hex_color):
    if hex_color is None:
        return None, None
    if isinstance(hex_color, int):
        hex_color = f"{hex_color:06x}"
    if hex_color.startswith("0x"):
        hex_color = hex_color[2:]
    if len(hex_color) != 6:
        raise ValueError("Hex color must be 6 characters long (RGB)")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    code = 16 + 36 * (r // 43) + 6 * (g // 43) + (b // 43)
    return code, code

def style_text(text, fg_bg_pair):
    fg, bg = fg_bg_pair
    seq = ""
    if fg is not None:
        fg_code = hex_to_ansi(fg)[0]
        seq += f"\033[38;5;{fg_code}m"
    if bg is not None:
        bg_code = hex_to_ansi(bg)[1]
        seq += f"\033[48;5;{bg_code}m"
    return f"{seq}{text}\033[0m" if seq else text


def check_bar_style_syntax(bar_style):
    example_style = {
        "BAR": {
            "+": [0xFFFFFF, 0x000000],
            "-": [0x888888, None],
        },
        "DESC": [0xAAAAAA, None],
        "CUR": [0xAAAAAA, None],
        "TOTAL": [0xAAAAAA, None],
        "PERCENT": [0xAAAAAA, None],
        "SPEED": [0xAAAAAA, None],
        "ETA": [0xAAAAAA, None],
    }

    def err(msg):
        raise ValueError(f"{msg}\n\nExample style:\n{example_style}")

    if not isinstance(bar_style, dict):
        err("Bar style must be a dictionary.")

    if "BAR" not in bar_style or not isinstance(bar_style["BAR"], dict):
        err("Bar style must contain a 'BAR' key with a dictionary value.")

    for key in ["+", "-"]:
        if key not in bar_style["BAR"]:
            err(f"'BAR' must contain a '{key}' key.")
        if not isinstance(bar_style["BAR"][key], list):
            err(f"'BAR' key '{key}' must be a list.")

    required_keys = ["DESC", "CUR", "TOTAL", "PERCENT", "SPEED", "ETA"]
    for key in required_keys:
        if key not in bar_style:
            err(f"Bar style must contain a '{key}' key.")
        if not isinstance(bar_style[key], list):
            err(f"Bar style key '{key}' must be a list.")

    return True