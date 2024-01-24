import tkinter

import customtkinter

# Appearence Modes
customtkinter.set_appearance_mode("Dark")
customtkinter.set_appearance_mode("blue")

# App Setup
app = customtkinter.CTk()
app.title("Databases")
app.geometry("1600x800")

# Default Font
defaultFont = customtkinter.CTkFont(family="Monospace", size=20, weight="bold", underline=True)

# Database List
dblist = customtkinter.CTkFrame(
    master=app,
    width=200,
    height=700,
    corner_radius=10
)

dblistTitle = customtkinter.CTkLabel(
    master=dblist,
    text="Databases",
    width=15,
    height=5,
    font=defaultFont
)
dblist.place(relx=0.005, rely=0.01)
dblistTitle.place(relx=0, rely=0)


# Input Area
dbInputFrame = customtkinter.CTkFrame(
    master=app,
    width=1300,
    height=350,
    corner_radius=10,
)
dbInputEntry = customtkinter.CTkEntry(
    master=dbInputFrame,
    width=1300,
    height=350,
    corner_radius=10,
    placeholder_text="Enter Database Name",
    font=("Seriff", 15),
    justify=customtkinter.LEFT,
)

dbInputEntry.place(relx=0, rely=0, anchor="nw")
dbInputFrame.place(relx=0.15, rely=0.02)



app.mainloop()
