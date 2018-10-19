# coding=utf-8
import xlrd
import sys
import xml.dom.minidom

print sys.getdefaultencoding()
reload(sys)  # 就是这么坑爹,否则下面会报错
sys.setdefaultencoding('utf-8')  # py默认是ascii。。要设成utf8


# excel中 数据格式如下:
# 测试集 子模块 用例名称 前提 步骤编号 操作步骤 预期结果
# XX系统/V2.4/后台	设置	 用例名称  前提  1	"操作步骤"	"预期结果"
# XX系统/V2.4/后台	设置			        2	"操作步骤2"	"预期结果2"


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)  # xlrd 操作excel的外部库
        return data
    except Exception, e:
         print str(e)


def add_Element(doc, testSuit, suitText1, k):
    locals()['testSuit' + str(k)] = doc.createElement('testsuite')
    locals()['testSuit' + str(k)].setAttribute('name', suitText1[k])
    if k == 1:
        testSuit.appendChild(locals()['testSuit' + str(k)])
        testSuit = locals()['testSuit' + str(k)]
    else:
        j = k - 1
        locals()['testSuit' + str(j)].appendChild(locals()['testSuit' + str(k)])
        testSuit = locals()['testSuit' + str(k)]
    return testSuit


def excel_table_byindex(file, by_index=0):
    data = open_excel(file)  # 打开excel

    table = data.sheets()[by_index]

    nRows = table.nrows

    doc = xml.dom.minidom.Document()  # 打开xml对象
    xmain = doc.createElement('testsuite')
    doc.appendChild(xmain)

    for nrow in range(0, nRows):  # 遍历每一行
        if nrow == 0:
            continue

        suitText1 = table.cell(nrow, 0).value  # 第一列的值(模块)
        suitText1 = suitText1.split('/')
        if nrow == 1:
            xmain.setAttribute('name', suitText1[0])  # 设置属性name的值
        for k in range(0, len(suitText1)):
            if k == 0:
                if nrow == 1:
                    testSuit = xmain
                continue
            if nrow == 1:
                testSuit = add_Element(doc, testSuit, suitText1, k)
            elif nrow != 1:
                onePreTest = table.cell(nrow - 1, 0).value
                onePreTest = onePreTest.split('/')
                preSuitName = ""
                if len(onePreTest) == len(suitText1) and onePreTest[k] != suitText1[k]:
                    locals()['testSuit' + str(k)] = doc.createElement('testsuite')
                    locals()['testSuit' + str(k)].setAttribute('name', suitText1[k])
                    if k == 1:
                        xmain.appendChild(locals()['testSuit' + str(k)])
                        testSuit = locals()['testSuit' + str(k)]
                    else:
                        j = k - 1
                        locals()['testSuit' + str(j)].appendChild(locals()['testSuit' + str(k)])
                        testSuit = locals()['testSuit' + str(k)]
                elif len(onePreTest) < len(suitText1):
                    testSuit = add_Element(doc, testSuit, suitText1, k)

        suitText2 = table.cell(nrow, 1).value  # 第二列的值(子模块)
        if nrow != 1:
            suitPreText2 = table.cell(nrow - 1, 1).value
            if suitText2 != suitPreText2:
                locals()['testSuit' + str(len(suitText1))] = doc.createElement('testsuite')  # 生成节点
                locals()['testSuit' + str(len(suitText1))].setAttribute('name', suitText2)  # 设置属性name的值(用例名称)
            elif suitText2 == suitPreText2:
                preTest1 = table.cell(nrow - 1, 0).value
                preTest1 = preTest1.split('/')
                if testSuit.getAttribute('name') != preTest1[-1]:
                    locals()['testSuit' + str(len(suitText1))] = doc.createElement('testsuite')  # 生成节点
                    locals()['testSuit' + str(len(suitText1))].setAttribute('name', suitText2)  # 设置属性name的值(用例名称)
        else:
            locals()['testSuit' + str(len(suitText1))] = doc.createElement('testsuite')  # 生成节点
            locals()['testSuit' + str(len(suitText1))].setAttribute('name', suitText2)  # 设置属性name的值(用例名称)
        testSuit.appendChild(locals()['testSuit' + str(len(suitText1))])

        name = table.cell(nrow, 2).value  # 第三列的值(用例名称的值)
        if name != "":
            item = doc.createElement('testcase')  # 生成节点
            item.setAttribute('name', name)  # 设置属性name的值(用例名称)
            locals()['testSuit' + str(len(suitText1))].appendChild(item)

        # summaryText = table.cell(nrow, 2).value  # 第三列的值(用例摘要)
        # summary = doc.createElement('summary')  # 生成子节点
        # sText = doc.createCDATASection(summaryText)
        # summary.appendChild(sText)
        # item.appendChild(summary)

        if name != "":
            preText = table.cell(nrow, 3).value  # 第四列的值 (用例前提)
            preconditions = doc.createElement('preconditions')  # 生成子节点
            pText = doc.createCDATASection('<p>' + preText + '</p>')
            preconditions.appendChild(pText)
            item.appendChild(preconditions)

        if name != "":
            steps = doc.createElement("steps")
        step = doc.createElement("step")
        steps.appendChild(step)
        item.appendChild(steps)

        # stepNumber = table.cell(nrow, 4).value  # 第五列的值(步骤编号)
        if name != "":
            step_number = doc.createElement('step_number')  # 生成子节点
            stepNo = doc.createCDATASection(str(1))
            step_number.appendChild(stepNo)
            step.appendChild(step_number)
        elif name == "":
            stepNumber = table.cell(nrow, 4).value
            step_number = doc.createElement('step_number')  # 生成子节点
            stepNo = doc.createCDATASection(str(stepNumber))
            step_number.appendChild(stepNo)
            step.appendChild(step_number)

        actText = table.cell(nrow, 5).value  # 第六列的值(操作步骤)
        actions = doc.createElement('actions')  # 生成子节点
        actText = actText.split('\n')
        actionText = ''
        for act in actText:
            actionText = actionText + '<p>' + act + '</p>'
        aText = doc.createCDATASection(actionText)
        actions.appendChild(aText)
        step.appendChild(actions)

        expText = table.cell(nrow, 6).value  # 第七列的值(预期结果)
        expectedResults = doc.createElement('expectedresults')  # 生成子节点
        expText = expText.split('\n')  # 使用换行符分割字符串
        expTexts = ''
        for exp in expText:
            expTexts = expTexts + '<p>' + exp + '</p>'
        result = doc.createCDATASection(expTexts)
        expectedResults.appendChild(result)
        step.appendChild(expectedResults)

        # xmain.appendChild(testSuit2)

    fileList = file.split('.')
    outFile = file.replace(fileList[-1], 'xml')
    f = open(outFile, 'w')  # xml文件输出路径
    f.write(doc.toprettyxml())
    f.close()

#excel文件路径
#excel_table_byindex(u'D:/test.xlsx', by_index = 0)
# if __name__ == "__main__":
#      value1 = raw_input(u'please input excelFile(D:/ldt/testcase.xlsx):')
#      try:
#          value2 = int(raw_input(u'please input sheet index(first sheet is 0):'))
#      except BaseException:
#          value2 = int(0)
#      print value2
#      excel_table_byindex(value1, by_index=value2)
