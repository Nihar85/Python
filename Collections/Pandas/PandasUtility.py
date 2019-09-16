import pandas as pd
emp_wages={"Employee Name":["Rahul","Arun","Varun","Karan"],
           "Location":["KPHB","JNTU","Miyapur","BHEL"],
           "Salary":["10000","20000","30000","40000"]
           }
structured_data=pd.DataFrame(emp_wages)
print(structured_data.loc[structured_data["Salary"]>="30000"])

