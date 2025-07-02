# What is SQL..? 
SQL is Structured Query Language, which is a computer language for storing, manipulating and retrieving data 
stored in relational database. 
SQL is the standard language for Relation Database System. All relational database management systems like 
MySQL, MS Access, Oracle, Sybase, Informix, postgres and SQL Server use SQL as standard database 
language. 
#  Servers
The computer (or system) that stores and runs your databases.
It’s the top-level container where all databases live.
# Databases
A collection of schemas and tables that store related data.
We write queries to interact with data inside a database.
#  Schemas
A logical structure inside a database that organizes tables, views, and other database objects.
Schemas help manage and group related objects.
#  Tables
A collection of rows and columns that hold actual data.
Just like a sheet in Excel, it's where we store and query real information.
# What is a Field..?
A field is a column in a table.
It stores a specific type of data for each record (row).
# What is a Record (Row)?
A record is a row in a table — also called an entry.
It contains all the field values for one item/person.
# Basic Querying :-
- Create Database :-
  - The CREATE DATABASE command is used to make a new DATABASE.
  - Syntax :- CREATE DATABASE databasename;
- CREATE TABLE :-
   - The CREATE TABLE command is used to make a new table in the database.
   - Syntax :- CREATE TABLE tablename ( column1 datatype, column2 datatype );
- INSERT :-
   - The INSERT  command is used to insert new records (rows) into the table.
   - Syntax :- INSERT INTO tablename (column1, column2) VALUES (value1, value2)
- SELECT :-
   - The SELECT command is used to fetch or view data from a table.
   - Syntax :- select * from databasename;
- WHERE Clause :-
   - The WHERE clause is used in SQL to filter rows from a table.
   - It helps you get only the rows that match a specific condition.
   - Syntax :- SELECT columns FROM tablename WHERE condition;
- UPDATE :-
   - The UPDATE command is used to change existing data in a table.
   - Syntax :- UPDATE table_name SET column = value WHERE condition;
- ALTER :-
   - The ALTER TABLE command is used to modify the table structure, like:
       - Add a new column :-
           - To store additional information that was not originally in the table.
           - Syntax :- ALTER TABLE table_name ADD column_name datatype;
       - Modify a column :-
           - To change the data type, size, or other properties of an existing column.
           - Syntax :- ALTER TABLE table_name MODIFY column_name new_datatype;
       - Rename a column :-
           - To make the column name more meaningful or accurate.
           - Syntax :- ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
       - Delete a column :-
           - To remove unnecessary or outdated columns from the table.
           - Syntax :- ALTER TABLE table_name DROP COLUMN column_name;
# SQL Functions :-
SQL has many built-in functions for performing processing on string or numeric data.

 - COUNT() :-
     - Returns the number of rows (or non-NULL values) in a column.
     - Syntax :- SELECT COUNT(column_name) FROM table_name;
 - AVG() :-
     - Returns the average of numeric values in a column.
     - Syntax :- SELECT AVG(column_name) FROM table_name;
 - SUM() :-
     - Returns the total sum of values in a numeric column.
     - SELECT SUM(column_name) FROM table_name;
 - MAX() :-
     - Returns the maximum (highest) value from a column.
     - Syntax :- SELECT MAX(column_name) FROM table_name;
 - MIN() :-
     - Returns the minimum (lowest) value from a column.
     - Syntax :- SELECT MIN(column_name) FROM table_name;
 - SQRT() :-
     - Returns the square root of a number.
     - Syntax :- SELECT SQRT(number);
 - RAND() :-
     - Returns a random decimal number between 0 and 1.
     -  Syntax :- SELECT RAND();
 - CONTACT() :-
     - Joins (concatenates) two or more strings into one.
     - Syntax :- SELECT CONCAT(string1, string2, ...) AS full_text;
# SQL WildCard :- 
Wildcards are special characters used in SQL with the LIKE operator to search for data that matches a pattern — instead of exact value.

 -  LIKE :- 

      - The LIKE operator is used to compare a value to similar values using wildcard operators. 

   1) (%) ==>  Use % for flexible match
   2) (_) ==>  Use _ for fixed character match

















  

                  

 
