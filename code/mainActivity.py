# coding=utf-8

import Tkinter
from Tkinter import Frame
from Tkinter import StringVar
from ExcelToXml import excel_table_byindex
import tkMessageBox

class tkDemo(Frame):

    def __init__(self):
        self.top = Tkinter.Tk()
        self.text1 = StringVar()
        self.text2 = StringVar()

    def gen_activity(self):
        # 设置窗口的尺寸大小
        self.top.wm_geometry('530x380+500+150')
        # 不允许 改变 窗口的宽和高
        self.top.wm_resizable(False, False)
        # 设置窗口标题
        self.top.title('Excel to Xml')

        message = '描述： 用于将excel表格中的测试用例转换成可导入testlink的xml文件，\n' \
                  '其中第一个参数是文件绝对路径和名称包含后缀名（如：D:/test.xlsx）\n' \
                  '第二个参数是sheet的位置（如第一个sheet则输入值为0，第二个sheet则输入值为1）\n' \
                  'excel文件的模板为：测试集 子模块 用例名称 前提 步骤编号 操作步骤 预期结果\n' \
                  '其中如果多层测试集则测试集之间用“/”分隔'

        Tkinter.Label(self.top, text=message, justify=Tkinter.LEFT, font=("宋体", 10),fg='red' ) \
            .pack(padx=2, pady=10, side=Tkinter.TOP, anchor=Tkinter.N)
        frame1 = self.gen_frame()
        # 添加接收区文字标签
        L2 = Tkinter.Label(frame1, text='请输入文件地址：', width=20, justify=Tkinter.LEFT, font=("宋体", 11), ) \
            .pack(padx=2, pady=10, side=Tkinter.LEFT, anchor=Tkinter.N)
        # 添加接收区的文本框
        txt1 = Tkinter.Entry(frame1, width=45, textvariable=self.text1).pack(padx=2, pady=10, side=Tkinter.LEFT, anchor=Tkinter.N)

        frame2 = self.gen_frame()
        # 添加接收区文字标签
        L3 = Tkinter.Label(frame2, text='sheet(默认：0)：', width=20, justify=Tkinter.LEFT, font=("宋体", 11), ) \
            .pack(padx=2, pady=10, side=Tkinter.LEFT, anchor=Tkinter.N)
        # 添加接收区的文本框
        txt2 = Tkinter.Entry(frame2, width=45, textvariable=self.text2).pack(padx=2, pady=10, side=Tkinter.LEFT, anchor=Tkinter.N)

        frame3 = self.gen_frame()
        button1 = Tkinter.Button(frame3, text='确定', command=self.command_convert) \
            .pack(side=Tkinter.RIGHT, anchor=Tkinter.N, padx=2, pady=4)
        button2 = Tkinter.Button(frame3, text="Exit", command=self.top.destroy) \
            .pack(side=Tkinter.RIGHT, anchor=Tkinter.N, padx=2, pady=4)
        self.top.mainloop()

    def command_convert(self):
        value1 = self.text1.get()
        value2 = self.text2.get()
        if value2 == '':
            value2 = 0
        else:
            try:
                value2 = int(value2)
            except Exception:
                value2 = 0
        try:
            excel_table_byindex(value1, by_index=value2)
            tkMessageBox.showinfo('转换成功', '文件已生成 请前往原文件路径查看')
        except Exception, e:
            tkMessageBox.showinfo('转换失败',e.message)


    def gen_frame(self):
        # 设置容器
        frame = Tkinter.Frame(self.top, height=40, width=60, relief=Tkinter.RIDGE, bd=5, borderwidth=4)
        # 设置填充和布局
        frame.pack(fill=Tkinter.X, ipady=2, expand=False)

        return frame


if __name__ == '__main__':
    tkDemo().gen_activity()