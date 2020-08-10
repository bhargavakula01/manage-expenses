# manage-expenses
- Tkinter application that manages expense using a PostgreSQL database

# What I learned
- I learned how to use the Tkinter GUI in order to construct a simplistic user interface to allow people to log expenses.
- I learned how to use the Psycopg2 to execute sql commands using python scripts
- I learned how to do proper file handling, specifically loading and saving to a file

# Resources that I used to help me with this project
- https://stackoverflow.com/questions/13793399/passing-table-name-as-a-parameter-in-psycopg2
- https://tableplus.com/blog/2018/04/postgresql-how-to-export-table-to-csv-file-with-header.html

# How to create a csv file of your expenses
- create a csv file and name it
- perform this query in psql
    - \copy (SELECT * FROM [table name]) TO '/Users/bhargav/desktop/my-expenses/[csv file name].csv' with csv header;

# Future Improvements
I plan to use a django framework in order to allow user to access their expenses on a web browser
