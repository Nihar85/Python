import pyodbc
cnxn=pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                    "Server=MYDELLINSPIRON;"
                    "Database=EmpDB;"
                    "Trusted_Connection=yes;")
