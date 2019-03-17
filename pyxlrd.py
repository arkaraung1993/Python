
#Intall xlrd module
#Put Excel file
import xlrd
book = xlrd.open_workbook("namesdemo.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("WorkSheet name(s): {0}".format(book.sheet_names()))
sh1 = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh1.name, sh1.nrows, sh1.ncols))
for rx in range(sh1.nrows):
    print(sh1.row(rx))
