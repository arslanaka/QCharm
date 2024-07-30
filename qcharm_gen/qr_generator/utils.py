from tkinter.colorchooser import askcolor


def choose_color(root, title="Choose color"):
    color = askcolor(title=title, parent=root)[1]
    return color if color else "black"
