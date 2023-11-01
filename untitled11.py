from tkinter import *

root=Tk()
root.title("Country Capitals")
root.geometry("400x400")


enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)
enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.6, anchor = CENTER)

country_list = Label(root)
capital_list = Label(root)
country_random = Label(root)
capital_random = Label(root)

capital = []
country = []

def addcountry():
    country_name = enter_country.get()
    country.append(country_name)
    country_list["text"] = "Your Countries are : " + str(country)
    
def addcapital():
     capital_name = enter_capital.get()
     capital.append(capital_name)
     capital_list["text"] = "Your Capitals are : " + str(capital)

root.mainloop()