import customtkinter
from CTkTable import *

app = customtkinter.CTk()
app.title("WORDCLOCK")
app.geometry("700x600")

uhr =   [["E","S","","I","S","C","H","","F","Ü","F"],
         ["Z","E","H","","V","I","E","R","T","E","L"],
         ["Z","W","I","N","Z","G","","V","O","R",""],
         ["A","B","","","H","A","L","B","I","",""],
         ["E","I","S","Z","W","E","I","","D","R","Ü"],
         ["V","I","E","R","I","","","F","Ü","F","I"],
         ["S","E","C","H","S","I","S","I","B","N","I"],
         ["A","C","H","T","I","","","N","Ü","N","I"],
         ["Z","E","H","N","I","","","Ö","L","F","I"],
         ["Z","W","Ö","L","F","I","","","","",""],
         ["","","","","","","B","L","Z","R","S"],
         ["","","","","","","","","","",""],
         ["","","",".",".",".",".",".","","",""]]

table = CTkTable(master=app, row=13, column=11, font=customtkinter.CTkFont(family="Consolas", size=40), values=uhr)
table.pack(expand=True, fill="both", padx=20, pady=20)

app.mainloop()