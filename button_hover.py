import tkinter

def on_enter(e):
    hoverStyle = {'foreground': 'black', 'bg': 'RoyalBlue3', 'activebackground':
'gray71', 'activeforeground': 'gray71'}
    e.configure(**hoverStyle)

def on_leave(button):
    defaultStyle = {'fg': 'black', 'bg': 'RoyalBlue1', 'activebackground':
'RoyalBlue3', 'activeforeground': 'black'}
    button.configure(**defaultStyle)