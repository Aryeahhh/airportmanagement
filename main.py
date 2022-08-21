import mysql.connector 
import tkinter as tk
import tkinter.font as font
import pandas as pd
from tkinter import messagebox

top = tk.Tk()
top.geometry("295x55")
db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Arya@01072005")
cursor = db.cursor()
def flight_csv():
    query = pd.read_sql_query("select * from airportmanagement.flight",con = db)
    df = pd.DataFrame(query)
    df.to_csv("flight.csv")
def passenger_csv():
    query = pd.read_sql_query("select * from airportmanagement.passenger",con = db)
    df = pd.DataFrame(query)
    df.to_csv("passenger.csv")
    
def flight_details():
    
    global flight_no,source,destination,departure_time,arrival_time,fare
    print(Flight_no.get())
    try:
        flight_no = int(Flight_no.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid flight no.")
        return
    try:
        source = str(Source.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid source.")
        return
    try:
        destination = str(Destination.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid destination.")
        return
    try:
        departure_time = str(Departure_Time.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid departure time.")
        return
    try:
        arrival_time = str(Arrival_Time.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid arrival time.")
        return
    try:
        fare = int(Fare.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid fare.")
        return
    cursor.execute("INSERT INTO flight VALUES (%s,%s,%s,%s,%s,%s)",(flight_no,source,destination,departure_time,arrival_time,fare))
    db.commit()
    print("Flight details inserted successfully")
def passenger_details():
    global passenger_id,name,age,flight_no
    try:
        passenger_id = int(Passenger_Id.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid passenger id.")
        return
    try:
        name = str(Name.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid name.")
    try:
        age = int(Age.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid age.")
        return
    try:
        flight_no = int(Flight_No.get())
    except ValueError:
        messagebox.showerror("Error","Enter a valid flight no.")
        return
    cursor.execute("INSERT INTO passenger VALUES (%s,%s,%s,%s)",(passenger_id,name,age,flight_no))
    db.commit()
    print("Passenger details inserted successfully")

    

    
f = font.Font(family='Helvetica', size=20, weight='bold')
try:
    cursor.execute("create database AirportManagement")
    cursor.execute("use AirportManagement")
    cursor.execute("create table Flight(Flight_No varchar(10),Source varchar(10),Destination varchar(10),Departure_Time datetime,Arrival_Time datetime,Fare varchar(10))")
    cursor.execute("create table Passenger(Passenger_Id varchar(10),Name varchar(10),Age varchar(10), Flight_No varchar(10))")
except:
    print("Database already exists")
    cursor.execute("use AirportManagement")
    print("Database selected")
def new_flight():
    global Flight_no,Source,Destination,Departure_Time,Arrival_Time,Fare
    new_flight_window = tk.Toplevel(top)
    new_flight_window.geometry("750x300")
    new_flight_window.title("New Flight")
    def flight_no_del(e):
        Flight_no.delete(0,"end")
    def source_del(e):
        Source.delete(0,"end")
    def destination_del(e):
        Destination.delete(0,"end")
    def departure_time_del(e):
        Departure_Time.delete(0,"end")
    def arrival_time_del(e):
        Arrival_Time.delete(0,"end")
    def fare_del(e):
        Fare.delete(0,"end")
    
    Flight_no = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Flight_no.insert(0,"Must be an integer")
    Flight_no.grid(row = 0,column = 1)

    Flight_no.bind("<FocusIn>",flight_no_del)
    tk.Label(new_flight_window,text = "Flight No: ",font = f).grid(row = 0,column = 0)
    Source = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Source.insert(0,"Must be a string")
    Source.grid(row = 1,column = 1)

    Source.bind("<FocusIn>",source_del)
    tk.Label(new_flight_window,text = "Source: ",font = f).grid(row = 1,column = 0)
    Destination = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Destination.insert(0,"Must be a string")
    Destination.grid(row = 2,column = 1)

    Destination.bind("<FocusIn>",destination_del)
    tk.Label(new_flight_window,text = "Destination: ",font = f).grid(row = 2,column = 0)
    Departure_Time = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Departure_Time.insert(0,"Must be in a 'YYYY-MM-DD HH:MM:SS' format")
    Departure_Time.grid(row = 3,column = 1)

    Departure_Time.bind("<FocusIn>",departure_time_del)
    tk.Label(new_flight_window,text = "Departure Time: ",font = f).grid(row = 3,column = 0)
    Arrival_Time = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Arrival_Time.insert(0,"Must be in a 'YYYY-MM-DD HH:MM:SS' format")
    Arrival_Time.grid(row = 4,column = 1)

    Arrival_Time.bind("<FocusIn>",arrival_time_del)
    tk.Label(new_flight_window,text = "Arrival Time: ",font = f).grid(row = 4,column = 0)
    Fare = tk.Entry(new_flight_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Fare.insert(0,"Must be an integer")
    Fare.grid(row = 5,column = 1)

    Fare.bind("<FocusIn>", fare_del)
    tk.Label(new_flight_window,text = "Fare: ",font = f).grid(row = 5,column = 0)
    btn = tk.Button(new_flight_window,text = "Submit",command = lambda:[flight_details()],font = font.Font(family='Helvetica', size=16, weight='bold')).grid(row = 6,column = 1)
    btn2 = tk.Button(new_flight_window,text = "Export as CSV",command = flight_csv,font = font.Font(family='Helvetica', size=16, weight='bold')).grid(row = 6,column = 0)
def new_passenger():
    global Passenger_Id,Name,Age,Flight_No
    new_passenger_window = tk.Toplevel(top)
    new_passenger_window.geometry("750x200")
    new_passenger_window.title("New Passenger")
    def passenger_id_del(e):
        Passenger_Id.delete(0,"end")
    def name_del(e):
        Name.delete(0,"end")
    def age_del(e):
        Age.delete(0,"end")
    def flight_no_del(e):
        Flight_No.delete(0,"end")
    
    Passenger_Id = tk.Entry(new_passenger_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Passenger_Id.insert(0,"Must be an integer")
    Passenger_Id.grid(row = 0,column = 1)

    Passenger_Id.bind("<FocusIn>",passenger_id_del)
    tk.Label(new_passenger_window,text = "Passenger Id: ",font = f).grid(row = 0,column = 0)
    Name = tk.Entry(new_passenger_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Name.insert(0,"Must be a string")
    Name.grid(row = 1,column = 1)

    Name.bind("<FocusIn>",name_del)
    tk.Label(new_passenger_window,text = "Name: ",font = f).grid(row = 1,column = 0)
    Age = tk.Entry(new_passenger_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Age.insert(0,"Must be an integer")
    Age.grid(row = 2,column = 1)

    Age.bind("<FocusIn>",age_del)
    tk.Label(new_passenger_window,text = "Age: ",font = f).grid(row = 2,column = 0)
    Flight_No = tk.Entry(new_passenger_window,width=40,font = font.Font(family='Helvetica', size=16, weight='bold'))
    Flight_No.insert(0,"Must be an integer")
    Flight_No.grid(row = 3,column = 1)

    Flight_No.bind("<FocusIn>",flight_no_del)
    tk.Label(new_passenger_window,text = "Flight No: ",font = f).grid(row = 3,column = 0)
    btn = tk.Button(new_passenger_window,text = "Submit",command = lambda:[passenger_details()],font = font.Font(family='Helvetica', size=16, weight='bold')).grid(row = 4,column = 1)
    btn2 = tk.Button(new_passenger_window,text = "Export as CSV",command = passenger_csv,font = font.Font(family='Helvetica', size=16, weight='bold')).grid(row = 4,column = 0)
b = tk.Button(top, text ="Flights",command = new_flight,font = f)
b2 = tk.Button(top, text ="Passengers",command = new_passenger,font = f)
b2.grid(row = 0,column = 1)
b.grid(row = 0,column = 0)

top.mainloop()
    
