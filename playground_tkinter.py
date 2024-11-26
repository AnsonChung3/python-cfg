import tkinter as tk

root = tk.Tk()
root.title = ("Playground Tkinter!")

sidebar_fr = tk.Frame(root)
sidebar_fr.grid(row=0, column=0, rowspan=1)

test_lb_left = tk.Label(sidebar_fr, text="Sidebar")
test_lb_left.grid(row=0, column=0)

main_display_fr = tk.Frame(root)
main_display_fr.grid(row=0, column=1, rowspan=2)

test_lb_right = tk.Label(main_display_fr, text="Main display")
test_lb_right.grid(row=0, column=0)

root.mainloop()