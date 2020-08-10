from tkinter import *
import psycopg2
from psycopg2 import sql


# Each month I will do expenses
# the month/year will be the name of the database on postgreSQL
# will help to check if that month has already been created
table_title_dates = []
totalamount = 0


# load from file method
#loads table names into a list. Method to store table names after closing application
def loadFromFile():
    file = open('tableDates.txt', 'r')
    f1 = file.readlines()
    for x in f1:
        table_title_dates.append(x)
    file.close()

# save to file method
#method to save table names to a txt file.
def saveToFile(table_name):
    table_title_dates.append(table_name)
    file = open('tableDates.txt', 'a')
    file.write(table_name + "\n")
    file.close()


# helps to find any table name within the list
# Uses linear search
def find_table_title(table_name_input):
    for x in table_title_dates:
        if(x == table_name_input):
            return x
    return None


# this function will create a new database on postgreSQL
def main():
    loadFromFile()
    strvalue = find_table_title(table_entry.get())
    if(len(table_title_dates) == 0 or strvalue == None):
        saveToFile(table_entry.get())
        create_expense_table(table_entry.get())
        update_expense_table(table_entry.get(), place_entry.get(), itemsbought_entry.get(), total_spent_entry.get(), category_entry.get())
    else:
        update_expense_table(table_entry.get(), place_entry.get(), itemsbought_entry.get(), total_spent_entry.get(), category_entry.get())
    month_sum(table_entry.get())

#this method will create a new table within postgresql
def create_expense_table(tablename):
    connection = psycopg2.connect(dbname= 'expenses', user= 'postgres', password = 'rajabaru', host= 'localhost', port= '5432')
    cursor = connection.cursor()
    print('database connected...')
    cursor.execute(sql.SQL("CREATE TABLE {}(place text, items_bought text, total_amount_spent integer, category text);").format(sql.Identifier(tablename)))
    print("table created")
    connection.commit()
    connection.close()

#updates information within a particular table
def update_expense_table(table_name, place, items, spent, category):
    connection = psycopg2.connect(dbname= 'expenses', user= 'postgres', password = 'rajabaru', host= 'localhost', port= '5432')
    cursor = connection.cursor()
    print('database connected...')
    cursor.execute(sql.SQL("INSERT INTO {}(place, items_bought, total_amount_spent, category) VALUES (%s, %s, %s, %s);").format(sql.Identifier(table_name)),[place, items, int(spent), category])
    print('expenses updated')
    connection.commit()
    connection.close()

#this method will calculate the sum of the expenses.
def month_sum(table_name):
    connection = psycopg2.connect(dbname= 'expenses', user= 'postgres', password = 'rajabaru', host= 'localhost', port= '5432')
    cursor = connection.cursor()
    print("database connected...")
    cursor.execute(sql.SQL("SELECT category,sum(total_amount_spent) FROM {} GROUP BY category;").format(sql.Identifier(table_name)))
    totalamount = cursor.fetchall()
    #cursor.execute(query,(table_name))
    sumspent_listbox.delete(0,END)
    sumspent_listbox.insert(END,totalamount)
    connection.commit()
    connection.close()

#this is the GUI for the application using Tkinter
# need to place widgets within a grid
root = Tk()

frame = Frame(root)
frame.pack()

tablename_label = Label(frame, text= 'table name(month-year : x-xxxx)')
table_entry = Entry(frame)
tablename_label.grid(row= 0, column= 0)
table_entry.grid(row= 0, column= 1)

place_label = Label(frame, text= 'place')
place_entry = Entry(frame)
place_label.grid(row= 1, column= 0)
place_entry.grid(row= 1, column= 1)

itemsbought_label = Label(frame, text= 'Items Bought')
itemsbought_entry = Entry(frame)
itemsbought_label.grid(row= 2, column= 0)
itemsbought_entry.grid(row= 2, column= 1)

total_spent_label = Label(frame, text= 'total spent')
total_spent_entry = Entry(frame)
total_spent_label.grid(row= 3, column= 0)
total_spent_entry.grid(row= 3, column= 1)

category_label = Label(frame, text= 'category')
category_entry = Entry(frame)
category_label.grid(row= 4, column= 0)
category_entry.grid(row= 4, column= 1)

enter_info = Button(frame, text= 'enter information', command= main)
enter_info.grid(row= 5, column= 1)


sumspent_label = Label(frame, text= 'total spent this month')
sumspent_label.grid(row= 7, column= 1)
sumspent_listbox = Listbox(frame)
sumspent_listbox.grid(row= 8, column= 1)

root.mainloop()