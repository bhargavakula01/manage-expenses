from tkinter import *
import psycopg2

# Each month I will do expenses
# the month/year will be the name of the database on postgreSQL
# will help to check if that month has already been created
table_title_dates = []

# this function will create a new database on postgreSQL

def mainMethod():
    for x in table_title_dates:
        if(x == table_entry.get()):
            update_expense_table()
        else:
            table_title_dates.append(table_entry.get())
            create_expense_table()
            update_expense_table()
        month_sum()

#this method will create a new table within postgresql
def create_expense_table():
    connection = psycopg2.connect(dbname= 'expenses', user= 'postgres', password = 'rajabaru', host= 'localhost', port= '5432')
    cursor = connection.cursor()
    print('database connected...')
    query= "CREATE TABLE %s(date text, place text, items_bought text, total_amount_spent text, category text);" #<-- %s is a placeholder allowing the user to input any value 
    cursor.execute(query,(table_entry.get()))
    print("table created")
    connection.commit()
    connection.close()

#updates information within a particular table
def update_expense_table():
    connection = psycopg2.connect(dbname= 'expenses', user= 'postgres', password = 'rajabaru', host= 'localhost', port= '5432')
    cursor = connection.cursor()
    print('database connected...')
    query = "INSERT INTO %s(date, place, items_bought, total_amount_spend, category) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query,(table_entry.get(), place_entry.get(), itemsbought_entry.get(), total_spent_entry.get(), category_entry.get()))
    print('expenses updated')
    connection.commit()
    connection.close()

def month_sum():
    #this method will calculate the sum of the expenses.
   


#this is the GUI for the application using Tkinter
# need to place widgets within a grid
root = Tk()

frame = Frame(root)
frame.pack()

tablename_label = Label(frame, text= 'table name(month/year : x/xxxx)')
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

enter_info = Button(frame, text= 'enter information', command= lambda: mainMethod())
enter_info.grid(row= 5, column= 1)

sumspent_label = Label(frame, text= 'total spent this month')
sumspent_label.grid(row= 7, column= 1)
sumspent_listbox = Listbox(frame)
sumspent_listbox.grid(row= 8, column= 1)




root.mainloop()
