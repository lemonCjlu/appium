import  xlrd

def get_excel_value_byrow(filename):
    #读取excel的sheet及行数
    workbook = xlrd.open_workbook(filename)
    sheet1 = workbook.sheet_by_index(0)
    nrows = sheet1.nrows

    #去除不执行的行
    l = list()
    for i in range(nrows):
        if sheet1.row_values(i)[5] == "yes":
            l.append(sheet1.row_values(i))
            
    return l
   


def get_execute_case_bycol(filename):
    #获取每列的内容
    case_list = get_excel_value_byrow(filename)
    cols_list =  list(zip(*case_list))
    return  cols_list


