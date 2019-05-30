import os
import sys


def get_case_dir(dir_name):
    #拆分目录，获取最后位的目录列表
    dir_list = dir_name.split("""\\""")
    file_name_list = dir_list[-1].split(".")
    print(dir_list)
    
    #拼接目录，获取用例目录
    try:
        case_name_dir = os.getcwd() + "\\" +"Data\\caselist" + "\\"  + dir_list[-2]+ "\\" + file_name_list[-2] + ".xls"
    except:
        case_name_dir = "Not Found xls"
        
    return  case_name_dir


def get_properity_dir(dir_name):
    #拆分目录，获取最后位的目录列表
    dir_list = dir_name.split("""\\""")
    file_name_list = dir_list[-1].split(".")
    
    #拼接目录，获取属性目录
    try:
        property_name = os.getcwd() + "\\" +"Data\\properities" + "\\"  + dir_list[-2] + "\\" + file_name_list[-2] + ".properties"
    except:
        property_name = "Not Found xls"
        
    return  property_name





