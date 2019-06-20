#-*- coding:utf-8 -*-

import xlsxwriter
work_book = xlsxwriter.Workbook('sesason_report.xlsx')
work_sheet = work_book.add_worksheet()

titleStyle = work_book.add_format({'border':1, 'align':'center', 'bg_color':'cccccc', 'font_size':12, 'bold':True})
nameStyle = work_book.add_format({'border':1, 'align':'center', 'bg_color':'yellow', 'font_size':12, 'bold':True})
dataStyle = work_book.add_format({'align':'center', 'font_size':12, 'bold':True, 'border':1})

title = [u'业务明细',u'一月份', u'二月份', u'三月份', u'四月份']
bname = [u'新马泰七日游', u'马尔代夫七日游', u'迪拜七日黄金之旅']

work_sheet.write_row('A1', title, titleStyle)
work_sheet.write_column('A2',bname, nameStyle)
work_sheet.set_column('A:E', 15)

data = [[181, 242, 287, 323], [208, 234, 277, 254], [150, 168, 203, 245]]
work_sheet.write_row('B2', data[0], dataStyle)
work_sheet.write_row('B3', data[1], dataStyle)
work_sheet.write_row('B4', data[2], dataStyle)

chart = work_book.add_chart({'type':'column'})
chart.set_title({'name':u'一季度旅游情况明细'})

for i in ['B', 'C', 'D', 'E']:
    chart.add_series({
     'categories':'=Sheet1!$A$2:$A$4',
     'values':'=Sheet1!$'+i+'$2:$' + i + '$4',
     'name':'=Sheet1!$' + i + '$1'
    }
    )

chart.set_size({'width':800, 'height':500})
chart.set_y_axis({'name':u'人次/月'})
chart.set_style(34)

work_sheet.insert_chart('A7', chart)

work_book.close()


































