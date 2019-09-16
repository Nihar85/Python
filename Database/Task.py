import xlrd
workbook=xlrd.open_workbook(r"C:\Users\Admin\Desktop\Emp_Data.xlsx")
worksheet=workbook.sheet_by_name('Emp_Details')
print(worksheet.nrows)
print(worksheet.ncols)

for i in range(1,worksheet.nrows):
    






