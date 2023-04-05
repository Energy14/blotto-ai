import tkinter as tk
window = tk.Tk()
window.geometry("600x600")
window.title("Blotto War")
tcR = tk.Label(window, text="3", font=("Arial", 20))
tcR.pack()

bf1Frame = tk.Frame(window, width=200, height=200, bg='red')
bf1Frame.pack(side=tk.LEFT)
bf2Frame = tk.Frame(window, width=200, height=200, bg='green')
bf2Frame.pack(side=tk.LEFT)
bf3Frame = tk.Frame(window, width=200, height=200, bg='blue')
bf3Frame.pack(side=tk.LEFT)

bf1R = tk.Label(bf1Frame, text="2", bg='red', font=("Arial", 20))
bf1R.place(relx=0.5, rely=0.5,anchor='center')
bf2R = tk.Label(bf2Frame, text="3", bg='green', font=("Arial", 20))
bf2R.place(relx=0.5, rely=0.5,anchor='center')
bf3R = tk.Label(bf3Frame, text="4",bg='blue', font=("Arial", 20))
bf3R.place(relx=0.5, rely=0.5,anchor='center')

tcB = tk.Label(window, text="5", font=("Arial", 20))
tcB.pack()

bf1Frame.pack_propagate(0)
window.mainloop()