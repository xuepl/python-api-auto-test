
import xlrd


def read_excel_dict(file):
    l = []
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    print(sheet1)
    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in range(1, sheet1.nrows):
        # l.append(sheet1.row_values(i))
        d = {}
        for j in range(sheet1.ncols):
            d[sheet1.row_values(0)[j]] = sheet1.row_values(i)[j]
        l.append(d)

    print(l)
    return l


def read_excel_list(file):
    l = []
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    # print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    # print(sheet1)
    # print(sheet1.name, sheet1.nrows, sheet1.ncols)

    for i in range(1, sheet1.nrows):
        # l.append(sheet1.row_values(i))
        d = []
        for j in range(sheet1.ncols):
            d = sheet1.row_values(i)
        l.append(d)

    # print(l)
    return l


if __name__ == '__main__':
    excel_list = read_excel_list("../document/test.xlsx")

    idsList = []
    len1 = len(excel_list)
    for i in range(len1):
        a = excel_list[i].pop()
        idsList.append(a)

    # read_excel_dict("../document/test.xlsx")
    # idsList = []
    # len1 = len(excel_list)
    # for i in range(len1):
    #     idsList.append(excel_list[i].pop())

    print(excel_list)
    print(idsList)
