import xlrd, xlsxwriter, os


def concate(newfile, data_row):
    total_data = []
    for filename in os.listdir():
        if filename.endswith('xlsx'):
            workbook = xlrd.open_workbook(filename)
            worksheet = workbook.sheets()[0]
            result = worksheet.row_values(data_row)
            result = [str(r) for r in result]
            total_data.append(result)

    workbook = xlsxwriter.Workbook(newfile)
    worksheet = workbook.add_worksheet()
    rows = 0
    for row in total_data:
        cols = 0
        for number in row:
            worksheet.write(rows, cols, number)
            print(rows, cols, number)
            cols += 1
        rows += 1

    workbook.close()


row = int(input('你想要获取文件的哪一行？'))
filename = input('你想给新生成的文件取个什么名字？（可直接回车默认是data.xlsx）') or 'data.xlsx'
concate(filename, row-1)
print('新的文件%s已经生成！！！' % filename)
input()