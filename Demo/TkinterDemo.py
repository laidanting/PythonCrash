#encoding=utf-8
import Tkinter

root = Tkinter.Tk()

#创建三个 Label 分别添加到root窗体中
#Label是一种用来显示文字或者图片的组件
la1 = Tkinter.Label(root, text='请输入需要访问的起始id：')
la1.pack(anchor='w')
la2 = Tkinter.Label(root, text='请输入访问的id数量：')
la2.pack(anchor='w')
la3 = Tkinter.Label(root, text='请输入访问的次数：')
la3.pack(anchor='w')
Tkinter.Entry(root, width=30).pack(anchor='nw', after=la1)
Tkinter.Entry(root, width=30).pack(anchor='nw', after=la2)
Tkinter.Entry(root, width=30).pack(anchor='nw', after=la3)

root.title('window with command') #主窗口标题
root.geometry('400x200')  #主窗口大小，中间的为英文字母x
root.mainloop()
