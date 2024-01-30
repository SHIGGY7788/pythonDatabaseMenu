import customtkinter
import mysql.connector
import sys

# Appearence Modes
customtkinter.set_appearance_mode("Dark")
customtkinter.set_appearance_mode("blue")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
)
cursor = mydb.cursor()
if mydb.is_connected():
    print("connected")

else:
    sys.exit("Could not connect to database")

active_databases = []
cleaned_databases = []
bad_chars = ["(", ")", ","]


def run():
    dbInput = dbInputEntry.get("0.0", "end")
    cursor.execute(dbInput)
    dbOutputEntry.configure(state="normal")
    dbOutputEntry.delete("0.0", "end")
    for x in cursor:
        dbOutputEntry.insert("0.0", f'{x}\n')
    dbOutputEntry.configure(state="disabled")
    dbInputEntry.delete("0.0", "end")
    listDatabases()


def listDatabases():
    dblistText.configure(state="normal")
    active_databases = []

    cursor.execute("SHOW DATABASES")
    dblistText.delete("0.0", "end")
    for x in cursor:
        active_databases.append(x)

    # Remove bad_chars from each string in active_databases
    cleaned_databases = [s[0].translate(str.maketrans("", "", "".join(bad_chars))) for s in active_databases]

    for i in cleaned_databases:
        dblistText.insert("end", f"{i} \n")
    dblistText.configure(state="disabled")
    print("Got Database list")



# App Setup
app = customtkinter.CTk()
app.title("Databases")
app.geometry("1600x800")

# Default Font
defaultFont = customtkinter.CTkFont(family="Monospace", size=20, weight="bold", underline=True)

# Menu Setup
dblist = customtkinter.CTkFrame(
    master=app,
    width=200,
    height=700,
    fg_color="transparent"
)
dblistText = customtkinter.CTkTextbox(
    master=app,
    width=200,
    height=700,
    corner_radius=10,
    state="disabled"
)
dblistTitle = customtkinter.CTkLabel(
    master=dblist,
    text="Databases",
    width=15,
    height=5,
    font=defaultFont
)
dblistRefresh = customtkinter.CTkButton(
    master=app,
    text="Refresh",
    command=listDatabases,
)
dbInputFrame = customtkinter.CTkFrame(
    master=app,
    width=1300,
    height=350,
    corner_radius=10,
    fg_color="transparent",
)
dbInputEntry = customtkinter.CTkTextbox(
    master=dbInputFrame,
    width=1300,
    height=350,
    corner_radius=10,
    font=("Seriff", 15),
    wrap="word"
)
dbOutputFrame = customtkinter.CTkFrame(
    master=app,
    width=1300,
    height=350,
    corner_radius=10,
    fg_color="transparent",
)
dbOutputEntry = customtkinter.CTkTextbox(
    master=dbOutputFrame,
    width=1300,
    height=350,
    corner_radius=10,
    font=("Seriff", 15),
    state="disabled",
    wrap="word"
)
dbRUN = customtkinter.CTkButton(
    master=app,
    width=150,
    height=15,
    corner_radius=10,
    font=("Seriff", 15),
    fg_color="gray",
    hover_color="black",
    text="RUN",
    command=run
)
dbOutputEntry.place(relx=0, rely=0, anchor="nw")
dbOutputFrame.place(relx=0.15, rely=0.5)
dbInputEntry.place(relx=0, rely=0, anchor="nw")
dbInputFrame.place(relx=0.15, rely=0.02)
dblist.place(relx=0.005, rely=0.01)
dblistTitle.place(relx=0, rely=0)
dblistText.place(relx=0, rely=0.05)
dblistRefresh.place(relx=0.015, rely=0.925)
dbRUN.place(relx=0.50, rely=0.95)

listDatabases()

app.mainloop()
